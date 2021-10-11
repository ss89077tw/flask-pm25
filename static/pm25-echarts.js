const mainEl = document.getElementById("main");
console.log(mainEl);
let charts = echarts.init(mainEl);
console.log(charts)

//指定圖表的配置項和資料
const option = {
    title: {
        text: "echart圖形繪製DEMO",
    },
    tooltip: {},
    legend: {
        data: ["銷量"],
    },
    xAxis: {
        data: ["襯衫", "羊毛衫", "雪紡衫", "褲子", "高跟鞋", "襪子"],
    },
    yAxis: {},
    series: [
        {
            name: "銷量",
            type: "bar",
            data: [5, 20, 36, 10, 10, 20],
        },
    ],
};

charts.setOption(option)