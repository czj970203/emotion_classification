/**
 * Created by chenzejun on 2019/4/11.
 */
function getBarData() {
    $.ajax({
        url: '/return_bar',
        type: 'post',
        dataType: 'json',
        success: function (data) {
            if (data != null) {
                alert('柱状图获取成功');
            } else {
                alert('信息获取失败');
            }
        },
        error: function (data) {
            alert("服务器连接失败");
        }
    });
}

window.setInterval(getBarData, 5000)

function getLineData(){
    $.ajax({
        url: '/return_line',
        type: 'post',
        dataType: 'json',
        success: function(data){
            if(data != null){
                alert(data['data'][0])
            }else{
                alert('信息获取失败')
            }
        },
        error: function(data){
            alert('服务器连接失败')
        }
    });
}