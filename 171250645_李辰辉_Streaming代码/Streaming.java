package streaming;

import com.clearspring.analytics.util.Lists;
import com.mongodb.spark.MongoSpark;
import org.apache.log4j.Level;
import org.apache.log4j.Logger;
import org.apache.spark.SparkConf;
import org.apache.spark.api.java.JavaRDD;
import org.apache.spark.api.java.JavaSparkContext;
import org.apache.spark.sql.SparkSession;
import org.apache.spark.streaming.Duration;
import org.apache.spark.streaming.Durations;
import org.apache.spark.streaming.api.java.JavaDStream;
import org.apache.spark.streaming.api.java.JavaPairDStream;
import org.apache.spark.streaming.api.java.JavaStreamingContext;
import org.bson.Document;
import scala.Tuple2;
import java.util.ArrayList;
import java.util.List;


public class Streaming {
    public static void main(String[] args) {

        // 创建 JavaStreamingContext
        Logger.getLogger("org.apache.spark").setLevel(Level.ERROR);
        Logger.getLogger("org.eclipse.jetty.server").setLevel(Level.OFF);

        SparkSession sparkSession=SparkSession.builder().master("local[4]").appName("Streaming")
                .config("spark.mongodb.output.uri", "mongodb://root:root@01-cwy:27017/admin")
                .config("spark.mongodb.output.database","sparkstreaming")
                .config("spark.mongodb.output.collection","sscollection")
                .getOrCreate();
        JavaSparkContext javaSparkContext=new JavaSparkContext(sparkSession.sparkContext());

        //SparkConf sc=new SparkConf().setAppName("Streaming").setMaster("local[4]");

        JavaStreamingContext jsc=new JavaStreamingContext(javaSparkContext, new Duration(3000));


        /*
        After a context is defined, you have to do the following.
            1.Define the input sources by creating input DStreams.
            2.Define the streaming computations by applying transformation and output operations to DStreams.
            3.Start receiving data and processing it using streamingContext.start().
            4.Wait for the processing to be stopped (manually or due to any error) using streamingContext.awaitTermination().
            5.The processing can be manually stopped using streamingContext.stop().
        */

        String hdfsPath="hdfs://02-lch:9000/StreamingSource/";
        String localFilePath="file:///home/lch/桌面/PachongFiles/";
        JavaDStream<String> input=jsc.textFileStream(hdfsPath);
        input=input.filter( s-> s.length()>0 );

        input.print();

        ArrayList< JavaDStream<String> > medias=new ArrayList<>(); //媒体分别过滤
        for(int i=0;i<Data.media.length;i++){
            final int index=i;
            medias.add( input.filter( s -> s.contains(Data.media[index]) ) );

        }

        for(int i=0;i<medias.size();i++){
            //对每一种媒体，进行处理
            JavaDStream<String> mediai=medias.get(i);
            //mediai.print();
            //针对每一种type要过滤出来
            ArrayList<JavaDStream<String>> types=new ArrayList<>();//某一个类别的媒体下 不同的type
            for(int j=0;j<Data.type.length;j++){
                final int index=j;
                types.add( mediai.filter( s-> s.contains(Data.type[index]) ) );
            }

            for(int k=0;k<types.size();k++){
                JavaDStream<String> typei=types.get(k);
                //不同的时间要过滤
                ArrayList<JavaDStream<String>> times=new ArrayList<>();  //某一个类别的媒体下，某一个type下，不同的时间

                for(int l=0;l<Data.time.length;l++){
                    final int index2=l;
                    times.add( typei.filter( s-> s.contains(Data.time[index2]) )  );
                }
                //TODO: times中是 具体媒体+具体类别+具体时间 下的 一系列 string 了，现在需要将它们的popularity算出来

                for(int l=0;l<times.size();l++){

                    JavaDStream<String> timei=times.get(l);
                    timei.print();
                    //{"media": "新浪", "type": "milite", "time": "20191008", "cmtnum": 127, "patnum": 1250, "textlen": 560, "imgnum": 5}
                    JavaPairDStream<String,Double> popularity=timei.mapToPair(
                            s->{
                                String key="";
                                Double value=0.0;
                                String regex=", ";
                                String[] data=s.split(regex);
                                key+= (data[0]+regex+data[1]+regex+data[2]+regex);
                                //System.out.println(s);

                                value= Data.calPopularity( Integer.parseInt(data[3].split(": ")[1]), Integer.parseInt(data[4].split(": ")[1]),Integer.parseInt(data[5].split(": ")[1]),Integer.parseInt(data[6].split(": ")[1].replace("}","").replaceAll("\"",""))  );

                                return new Tuple2<>(key,value);
                            }
                    );
                    popularity=popularity.reduceByKey( (i1,i2) -> i1+i2 );
                    //mix.print();

                    //TODO: 1.将JavaPairDStream 转成 JavaRDD<Document>    2. MongoSpark.save()

                    JavaDStream<String> popularity_flat=popularity.flatMap(
                            kv->{
                                List<String> list= Lists.newArrayList();
                                list.add( kv._1 + "&" + kv._2  );
                                return list.iterator();
                            }
                    );
                    //popularity_flat.print();
                    popularity_flat.foreachRDD(
                            rdd->{
                                JavaRDD<Document> jd=rdd.map(
                                        s->{
                                            String json="";
                                            String[] data=s.split("&");
                                            json+= (data[0]+ "\"popularity\": "+Double.parseDouble(data[1]) +"}");
                                            //System.out.println("----------------------------------------------");
                                            //System.out.println(json);
                                            return Document.parse(json);
                                        }
                                );
                                //jd.collect();
                                MongoSpark.save(jd);
                            }
                    );


                }


            }



        }




        jsc.start();

        try {
            jsc.awaitTermination();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }


    }
}
