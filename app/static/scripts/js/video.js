/**
 * Created by 李珍鸿 on 2019/4/17.
 */

var chart1 = echarts.init(document.getElementById('bar'));
var option1 = {
    title : {
        text : ''
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
            data : []
        }
    ]
};
var chart2 = echarts.init(document.getElementById('line'));
var option2 = {
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
function onInputFileChange() {
    var file = document.getElementById('file').files[0];
    var url = window.URL.createObjectURL(file);
    console.log(url);
    document.getElementById("audio_id").src = url;
}
var int;
function capture(){
    ctx = canvas.getContext("2d");
    ctx.drawImage(audio_id, 0, 0, 400, 300);
    var imageData = canvas.toDataURL('image',1.0);
    $.ajax({
        url: '/catch_image',
        type: 'post',
        data: {'imageData':imageData},
        success: function (data) {
            if (data != null) {
                document.getElementById('img').setAttribute('src',data)
            } else {
                alert('信息获取失败');
            }
        },
        error: function (data) {
            alert("服务器连接失败");
        }
    });
    $.ajax({
        url: '/return_video_bar',
        type: 'post',
        data: {'imageData':imageData},
        dataType: 'json',
        success: function (data) {
            if (data != null) {
                option1.series[0].data = data['data'];
                window.setTimeout(chart1.setOption(option1), 1000);
                for(var i=0;i<7;i++){
                    option2.series[i].data.push(data['data'][i]);
                }
                window.setTimeout(chart2.setOption(option2), 5000);
            } else {
                alert('信息获取失败');
            }
        },
        error: function (data) {
            alert("服务器连接失败");
        }
    });
}
function stop() {
    clearInterval(int)
    option1.series[0].data = [];
    window.setTimeout(chart1.setOption(option1), 1000);
    for(var i=0;i<7;i++){
        option2.series[i].data = [];
    }
    window.setTimeout(chart2.setOption(option2), 5000);
}
function start() {
    int = window.setInterval(capture, 500);
}
