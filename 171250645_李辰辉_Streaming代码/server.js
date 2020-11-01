let http = require('http')
let fs = require('fs')
let url = require('url')
let data = require('./data')

// 创建http服务器
http.createServer((request, response) => {
  // 解析请求，包括文件名
  let pathname = url.parse(request.url).pathname;
  // 输出请求的文件名
  console.log("Request for " + pathname + " received.");
  // api路径简易正则

  /**
   * 以下硬编码临时处理
   */

  const dataRegex = /\/api\//
  if (!dataRegex.test(pathname)) { // 请求页面
    // 从文件系统中读取请求的文件内容
    fs.readFile(pathname.substr(1), function (err, data) {
      if (err) {
        console.log(err);
        response.writeHead(404, { 'Content-Type': 'text/html' });
      } else {
        response.writeHead(200, { 'Content-Type': 'text/html' });
        response.write(data.toString());
      }
      response.end();
    });
  } else { // 请求数据
    let type = (url.parse(request.url).query || '').replace('type=', '')
    data.getData(type).then(res => {
      response.writeHead(200, { 'Content-Type': 'application/json' });
      response.write(JSON.stringify(res));
      response.end();
    })
  }

}).listen(3000)

console.log('Server running at http://127.0.0.1:3000/')