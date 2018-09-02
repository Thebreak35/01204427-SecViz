( function ( $ ) {
    "use strict";


    var dom = document.getElementById("week3_1");
    var myChart = echarts.init(dom);
    var app = {};
    var option = null;
    app.title = 'IP type';

    option = {
        tooltip: {
            trigger: 'item',
            formatter: "{a} <br/>{b}: {c} ({d}%)"
        },
        legend: {
            orient: 'vertical',
            x: 'left',
            data:['IPv4','Dual Stack','IPv6']
        },
        series: [
            {
                name:'Number of IP type',
                type:'pie',
                radius: ['50%', '70%'],
                avoidLabelOverlap: false,
                label: {
                    normal: {
                        show: false,
                        position: 'center'
                    },
                    emphasis: {
                        show: true,
                        textStyle: {
                            fontSize: '30',
                            fontWeight: 'bold'
                        }
                    }
                },
                labelLine: {
                    normal: {
                        show: false
                    }
                },
                data:[
                    {value:4000, name:'IPv4', itemStyle: {color: '#0000CE'}},
                    {value:3127, name:'Dual Stack', itemStyle: {color: '#7373FF'}},
                    {value:10, name:'IPv6', itemStyle: {color: '#C6C6FF'}}
                ]
            }
        ]
    };
    ;
    if (option && typeof option === "object") {
        myChart.setOption(option, true);
    }

    var dom = document.getElementById("week3_2");
    var myChart = echarts.init(dom);
    var app = {};
    option = null;
    app.title = 'Login servers distribution';

    option = {
        title: {
            text: 'Login servers distribution',
            subtext: 'Bar chart'
        },
        tooltip: {
            trigger: 'axis',
            axisPointer: {
                type: 'shadow'
            }
        },
        grid: {
            left: '3%',
            right: '4%',
            bottom: '3%',
            containLabel: true
        },
        xAxis: {
            type: 'value',
            boundaryGap: [0, 0.01]
        },
        yAxis: {
            type: 'category',
            data: ['::ffff:158.108.218.212','::ffff:158.108.218.205','::ffff:158.108.218.201','::ffff:158.108.218.206','::ffff:158.108.218.204','::ffff:158.108.218.203', '::ffff:158.108.218.208', '::ffff:158.108.218.209', '::ffff:158.108.218.210', '::ffff:158.108.218.211', '::ffff:158.108.218.207', '::ffff:158.108.218.202']
        },
        series: [
            {
                type: 'bar',
                data: [673, 570, 644, 570, 665, 553, 567, 548, 592, 523, 589, 643],
                itemStyle: {color: "#FF2626"}
            },
        ]
    };
    ;
    if (option && typeof option === "object") {
        myChart.setOption(option, true);
    }

} )( jQuery );