const mainEl = document.getElementById("main");
console.log(mainEl);
let charts = echarts.init(mainEl);
console.log(charts)


$(document).ready(() => {
    $.ajax(
        {
            url: "/pm25-data",
            type: "POST",
            datetype: "json",
            success: (datas) => {
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
                        data: datas['sites'],
                    },
                    yAxis: {},
                    series: [
                        {
                            name: "PM2.5",
                            type: "bar",
                            data: datas['values'],
                        },
                    ],
                };
                
                charts.setOption(option)

            }
        }
    )    
});   

    


