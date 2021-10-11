const mainEl = document.getElementById("main");
console.log(mainEl);
let charts = echarts.init(mainEl);
console.log(charts)

//指定圖表的配置項和資料
const option = {
    title: {
        text: "PM2.5圖形繪製",
    },
    tooltip: {},
    legend: {
        data: ["PM2.5"],
    },
    xAxis: {
        data: ["襯衫", "羊毛衫", "雪紡衫", "褲子", "高跟鞋", "襪子"],
    },
    yAxis: {},
    series: [
        {
            name: "PM2.5",
            type: "bar",
            data: [5, 20, 36, 10, 10, 20],
        },
    ],
};

charts.setOption(option)