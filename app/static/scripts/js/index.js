/**
 * Created by chenzejun on 2019/4/11.
 */

var chart1 = echarts.init(document.getElementById('bar'));
var option1 = {
    title : {
        text : '1号人脸'
    },
    tooltip : {
        trigger : 'axis',
        axisPointer : {
            type : 'cross',
            label : {
                backgroundColor: '#283b56'
            }
        }
    },
    legend : {
        data : ['表情力']
    },
    xAxis : {
        type : 'value',
        boundaryGap : [0.2, 0.2],
        max : 1,
        min : 0
    },
    yAxis : {
        type : 'category',
        boundaryGap : 'true',
        data : ['angry', 'disgust', 'fear', 'happy', 'sad', 'surprise', 'neutral']
    },
    series : [
        {
            name : '表情力',
            type : 'bar',
            itemstyle :{
                normal : {
                    color : '#b53028'
                }
            },
            data : []
        }
    ]
};

var chart2 = echarts.init(document.getElementById('bar2'));
var option2 = {
    title : {
        text : '2号人脸'
    },
    tooltip : {
        trigger : 'axis',
        axisPointer : {
            type : 'cross',
            label : {
                backgroundColor: '#283b56'
            }
        }
    },
    legend : {
        data : ['表情力']
    },
    xAxis : {
        type : 'value',
        boundaryGap : [0.2, 0.2],
        max : 1,
        min : 0
    },
    yAxis : {
        type : 'category',
        boundaryGap : 'true',
        data : ['angry', 'disgust', 'fear', 'happy', 'sad', 'surprise', 'neutral']
    },
    series : [
        {
            name : '表情力',
            type : 'bar',
            itemstyle :{
                normal : {
                    color : '#d5b020'
                }
            },
            data : []
        }
    ]
};

var chart3 = echarts.init(document.getElementById('bar3'));
var option3 = {
    title : {
        text : '3号人脸'
    },
    tooltip : {
        trigger : 'axis',
        axisPointer : {
            type : 'cross',
            label : {
                backgroundColor: '#283b56'
            }
        }
    },
    legend : {
        data : ['表情力']
    },
    xAxis : {
        type : 'value',
        boundaryGap : [0.2, 0.2],
        max : 1,
        min : 0
    },
    yAxis : {
        type : 'category',
        boundaryGap : 'true',
        data : ['angry', 'disgust', 'fear', 'happy', 'sad', 'surprise', 'neutral']
    },
    series : [
        {
            name : '表情力',
            type : 'bar',
            itemstyle :{
                normal : {
                    color : '#18cc42'
                }
            },
            data : []
        }
    ]
};

var chart4 = echarts.init(document.getElementById('bar4'));
var option4 = {
    title : {
        text : '4号人脸'
    },
    tooltip : {
        trigger : 'axis',
        axisPointer : {
            type : 'cross',
            label : {
                backgroundColor: '#283b56'
            }
        }
    },
    legend : {
        data : ['表情力']
    },
    xAxis : {
        type : 'value',
        boundaryGap : [0.2, 0.2],
        max : 1,
        min : 0
    },
    yAxis : {
        type : 'category',
        boundaryGap : 'true',
        data : ['angry', 'disgust', 'fear', 'happy', 'sad', 'surprise', 'neutral']
    },
    series : [
        {
            name : '表情力',
            type : 'bar',
            itemstyle :{
                normal : {
                    color : '#4243d9'
                }
            },
            data : []
        }
    ]
};


var chart5 = echarts.init(document.getElementById('line'));
var option5 = {
    title : {
        text : ''
    },
    tooltip : {
        trigger : 'axis'
    },
    legend : {
        data : ['angry', 'disgust', 'fear', 'happy', 'sad', 'surprise', 'neutral']
    },
    grid : {
        left: '3%',
        right: '4%',
        bottom: '3%',
        containLabel: true
    },
    xAxis : {
        type : 'category',
        boundaryGap : 'false',
        data : []
    },
    yAxis : {
        type : 'value'
    },
    series : [
        {
            name : 'angry',
            type : 'line',
            data : []
        },
        {
            name : 'disgust',
            type : 'line',
            data : []
        },
        {
            name : 'fear',
            type : 'line',
            data : []
        },
        {
            name : 'happy',
            type : 'line',
            data : []
        },
        {
            name : 'sad',
            type : 'line',
            data : []
        },
        {
            name : 'surprise',
            type : 'line',
            data : []
        },
        {
            name : 'neutral',
            type : 'line',
            data : []
        }
    ]
};


function getBarData() {
    $.ajax({
        url: '/return_bar',
        type: 'post',
        dataType: 'json',
        success: function (data) {
            if (data['data'] != 'camera closed.') {
                var len = data['data'].length;
                switch(len){
                    case 1:
                        option1.series[0].data = data['data'][0];
                        window.setTimeout(chart1.setOption(option1), 1000);
                        document.getElementById('bar').style.display = 'inline';
                        document.getElementById('bar2').style.display = 'none';
                        document.getElementById('bar3').style.display = 'none';
                        document.getElementById('bar4').style.display = 'none';
                        break;
                    case 2:
                        option1.series[0].data = data['data'][0];
                        window.setTimeout(chart1.setOption(option1), 1000);
                        option2.series[0].data = data['data'][1];
                        window.setTimeout(chart2.setOption(option2), 1000);
                        document.getElementById('bar').style.display = 'inline';
                        document.getElementById('bar2').style.display = 'inline';
                        document.getElementById('bar3').style.display = 'none';
                        document.getElementById('bar4').style.display = 'none';
                        break;
                    case 3:
                        option1.series[0].data = data['data'][0];
                        window.setTimeout(chart1.setOption(option1), 1000);
                        option2.series[0].data = data['data'][1];
                        window.setTimeout(chart2.setOption(option2), 1000);
                        option3.series[0].data = data['data'][2];
                        window.setTimeout(chart3.setOption(option3), 1000);
                        document.getElementById('bar').style.display = 'inline';
                        document.getElementById('bar2').style.display = 'inline';
                        document.getElementById('bar3').style.display = 'inline';
                        document.getElementById('bar4').style.display = 'none';
                        break;
                    case 4:
                        option1.series[0].data = data['data'][0];
                        window.setTimeout(chart1.setOption(option1), 1000);
                        option2.series[0].data = data['data'][1];
                        window.setTimeout(chart2.setOption(option2), 1000);
                        option3.series[0].data = data['data'][2];
                        window.setTimeout(chart3.setOption(option3), 1000);
                        option4.series[0].data = data['data'][3];
                        window.setTimeout(chart4.setOption(option4), 1000);
                        document.getElementById('bar').style.display = 'inline';
                        document.getElementById('bar2').style.display = 'inline';
                        document.getElementById('bar3').style.display = 'inline';
                        document.getElementById('bar4').style.display = 'inline';
                        break;
                    default :
                        document.getElementById('bar').style.display = 'none';
                        document.getElementById('bar2').style.display = 'none';
                        document.getElementById('bar3').style.display = 'none';
                        document.getElementById('bar4').style.display = 'none';
                }
            }
        },
        error: function (data) {
            alert("服务器连接失败");
        }
    });
}

window.setInterval(getBarData, 1500);

function getLineData(){
    $.ajax({
        url: '/return_line',
        type: 'post',
        dataType: 'json',
        success: function(data){
            if(data != null){
                for(var i=0;i<7;i++){
                    option5.series[i].data = data['data']['1'][i];
                }
                window.setTimeout(chart5.setOption(option5), 1000);
            }else{
                alert('信息获取失败')
            }
        },
        error: function(data){
            alert('服务器连接失败')
        }
    });
}