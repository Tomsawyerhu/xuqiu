package streaming;

public class Data {
    static String[] media = {"netease","sina"};
    static String[] type = {"ent","tech","finance","milite","world","sports","edu","gov"};
    static String[] time = {"2019-10-08","2019-10-09","2019-10-10","2019-10-11","2019-10-12","2019-10-13"};

    static double calPopularity(int cmtnum,int patnum,int textlen,int imgnum){
       double res=0.0;
       //计算
        res= (cmtnum*5+patnum*1) / (textlen + imgnum * 300 + 10.0);
       return res;
    }
}
