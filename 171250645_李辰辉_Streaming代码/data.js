let MongoClient = require('mongodb').MongoClient
let url = 'mongodb://root:root@01-cwy:27017/sparkstreaming?authSource=admin'

const DB_NAME = 'sparkstreaming'
const COLLECTION_NAME = 'sscollection'

exports.getData = (type) => {
  switch (type) {
    case '0':
      return getWebsiteData('netease')
    case '1':
      return getWebsiteData('sina')
    case '2':
      return getComparingData()
    default:
      return null
  }
}
const getWebsiteData = (media) => new Promise(
  (resolve, reject) => {
    getRawData(DB_NAME, COLLECTION_NAME, { media }).then(res => {
      let titleText = `${media}折线图`
      let xAxisData = ['2019-10-08', '2019-10-09', '2019-10-10', '2019-10-11', '2019-10-12', '2019-10-13']
      let legendData = ['ent', 'tech', 'finance', 'milite', 'world', 'sports', 'edu', 'gov']
      let series = []
      for (let i = 0; i < legendData.length; i++) {
        let type = legendData[i]
        let popularityList = res.filter(item => item.type == type)
          .sort((a, b) => new Date(a.time).valueOf() - new Date(b.time).valueOf())
          .map(v => v.popularity)

        series.push({
          name: type,
          type: 'line', // 让前端画‘折线图’
          data: popularityList,
        })
      }
      // 送走这波数据（直接用于前端展示）
      resolve({ titleText, xAxisData, legendData, series, })
    })
  }
)

const getComparingData = () => new Promise(
  (resolve, reject) => {
    getRawData(DB_NAME, COLLECTION_NAME).then(res => {
      const media = ['netease', 'sina']
      let titleText = `数据汇总折线图`
      let xAxisData = ['2019-10-08', '2019-10-09', '2019-10-10', '2019-10-11', '2019-10-12', '2019-10-13']
      let legendData = media
      let series = []

      for (let i = 0; i < media.length; i++) {
        let currentMedia = media[i]
        let currentMediaData = res.filter(item => item.media == currentMedia)
        let popularityList = []
        for (let j = 0; j < xAxisData.length; j++) {
          const sum = currentMediaData.filter(item => item.time == xAxisData[j]) // 某天
            .map(v => v.popularity)
            .reduce((acc, v) => acc + v, 0) // 这天的和
          popularityList.push(sum)
        }
        series.push({
          name: currentMedia,
          type: 'line',
          data: popularityList, // 6天的和
        })
      }
      resolve({ titleText, xAxisData, legendData, series, })
    })
  }
)

const getRawData = (dbName, collectionName, whereStr = {}) => new Promise(
  (resolve, reject) => {
    MongoClient.connect(url, { useNewUrlParser: true }, (err, db) => {
      if (err) { reject(err); throw err }

      let dbase = db.db(dbName)
      dbase.collection(collectionName).find(whereStr).toArray((err, res) => {
        if (err) { reject(err); throw err }
        db.close()
        resolve(res)
      })
    })
  }
)

// 插入测试数据
const insertMockData = () => {
  const data = [
    { "media": "netease", "type": "ent", "time": "2019-10-08", "popularity": 130.86 },
    { "media": "netease", "type": "tech", "time": "2019-10-08", "popularity": 125.80 },
    { "media": "netease", "type": "finance", "time": "2019-10-08", "popularity": 102.24 },
    { "media": "netease", "type": "milite", "time": "2019-10-08", "popularity": 304.53 },
    { "media": "netease", "type": "world", "time": "2019-10-08", "popularity": 40.32 },
    { "media": "netease", "type": "sports", "time": "2019-10-08", "popularity": 303.3 },
    { "media": "netease", "type": "edu", "time": "2019-10-08", "popularity": 40.26 },
    { "media": "netease", "type": "gov", "time": "2019-10-08", "popularity": 103.914 },
    { "media": "sina", "type": "ent", "time": "2019-10-08", "popularity": 208.4 },
    { "media": "sina", "type": "tech", "time": "2019-10-08", "popularity": 50.73 },
    { "media": "sina", "type": "finance", "time": "2019-10-08", "popularity": 108.46 },
    { "media": "sina", "type": "milite", "time": "2019-10-08", "popularity": 200.3 },
    { "media": "sina", "type": "world", "time": "2019-10-08", "popularity": 1303.91 },
    { "media": "sina", "type": "sports", "time": "2019-10-08", "popularity": 5066.87 },
    { "media": "sina", "type": "edu", "time": "2019-10-08", "popularity": 90.14 },
    { "media": "sina", "type": "gov", "time": "2019-10-08", "popularity": 10.179 },
  ].map(v => { v.time = '2019-10-13'; return v })

  MongoClient.connect(url, { useNewUrlParser: true }, function (err, db) {
    if (err) throw err;

    var dbase = db.db("sparkstreaming");
    dbase.createCollection('sscollection', function (err, res) {
      if (err) throw err;

      dbase.collection("sscollection").insertMany(data, function (err, res) {
        if (err) throw err;
        console.log("插入的文档数量为: " + res.insertedCount);
        db.close();
      });

    });

  });
}
// insertMockData()
