const ServerConfig = 'http://127.0.0.1:3000'

const WEBSITE_List = ['netease', 'sina', 'both']

// <body> onload 时调用该函数绘制图表
const setSparkData = () => {
    WEBSITE_List.map(v => { setWebsiteData(v) })
}

// 绘制图表
const setWebsiteData = (website) => {
    // 基于准备好的dom，初始化echarts实例
    let myChart = echarts.init(document.getElementById(website));

    // 指定图表的配置项和数据
    let option = {
        title: {
            text: ''
        },
        tooltip: {
            trigger: 'axis'
        },
        legend: {
            data: []
        },
        grid: {
            left: '3%',
            right: '4%',
            bottom: '3%',
            containLabel: true
        },
        toolbox: {
            feature: {
                saveAsImage: {}
            }
        },
        xAxis: {
            type: 'category',
            boundaryGap: false,
            data: []
        },
        yAxis: {
            type: 'value'
        },
        series: []
    }

    const updateData = () => {
        let httpRequest = new XMLHttpRequest();
        httpRequest.open('GET', `${ServerConfig}/api/websiteData?type=${WEBSITE_List.indexOf(website)}`, true);
        httpRequest.send();
        httpRequest.onreadystatechange = function () {
            if (httpRequest.readyState == 4 && httpRequest.status == 200) {
                let res = JSON.parse(httpRequest.responseText);
                option.title.text = res.titleText
                option.xAxis.data = res.xAxisData
                option.legend.data = res.legendData
                option.series = res.series
                myChart.setOption(option);
            }
        };
    }

    updateData()
    window.setInterval(updateData, 3000)
}