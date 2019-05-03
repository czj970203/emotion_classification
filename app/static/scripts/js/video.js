/**
 * Created by 李珍鸿 on 2019/4/17.
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

var chart6 = echarts.init(document.getElementById('line2'));
var option6 = {
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

var chart7 = echarts.init(document.getElementById('line3'));
var option7 = {
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

var chart8 = echarts.init(document.getElementById('line4'));
var option8 = {
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
            if (data['data'].length != 0) {
                var len = data['data'].length;
                if(len == 4){
                    option4.series[0].data = data['data'][3];
                    window.setTimeout(chart4.setOption(option4), 1000);
                    document.getElementById('bar4').style.display = 'inline';
                    len = len -1;
                }else{
                    document.getElementById('bar4').style.display = 'none';

                }
                if(len == 3){
                    option3.series[0].data = data['data'][2];
                    window.setTimeout(chart3.setOption(option3), 1000);
                    document.getElementById('bar3').style.display = 'inline';
                    len = len -1;
                }else{
                    document.getElementById('bar3').style.display = 'none';
                }
                if(len == 2){
                    option2.series[0].data = data['data'][1];
                    window.setTimeout(chart2.setOption(option2), 1000);
                    document.getElementById('bar2').style.display = 'inline';
                    len = len -1;
                }else{
                    document.getElementById('bar2').style.display = 'none';
                }
                if(len == 1){
                    option1.series[0].data = data['data'][0];
                    window.setTimeout(chart1.setOption(option1), 1000);
                    document.getElementById('bar').style.display = 'inline';
                    len = len -1;
                }else{
                    document.getElementById('bar').style.display = 'none';
                }
            } else {
                alert('信息获取失败');
            }
        },
        error: function (data) {
            alert("服务器连接失败");
        }
    });
    $.ajax({
        url: '/return_video_line',
        type: 'post',
        data: {'imageData':imageData},
        dataType: 'json',
        success: function (data) {
            if(data['locations'].length != 0){
                var index = 0;
                var index0 = data['locations'].indexOf(0);
                if(index0 != -1){
                    for(var i=0;i<7;i++){
                        option5.series[i].data.push(data['data'][index][i]);
                        window.setTimeout(chart5.setOption(option5), 1000);
                    }
                }
                var index1 = data['locations'].indexOf(1);
                if(index1 != -1){
                    index += 1;
                    for(var i=0;i<7;i++){
                        option6.series[i].data.push(data['data'][index][i]);
                        window.setTimeout(chart6.setOption(option6), 1000);

                    }
                }
                var index2 = data['locations'].indexOf(2);
                if(index2 != -1){
                    index += 1;
                    for(var i=0;i<7;i++){
                        option7.series[i].data.push(data['data'][index][i]);
                        window.setTimeout(chart7.setOption(option7), 1000);
                    }
                }
                var index3 = data['locations'].indexOf(3);
                if(index3 != -1){
                    index += 1;
                    for(var i=0;i<7;i++){
                        option8.series[i].data.push(data['data'][index][i]);
                        window.setTimeout(chart8.setOption(option8), 1000);

                    }
                }
            }else {
                alert('信息获取失败');
            }
        }
    })
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
