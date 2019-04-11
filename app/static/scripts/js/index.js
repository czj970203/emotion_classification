/**
 * Created by chenzejun on 2019/4/11.
 */
$.ajax({
    url: '/return_bar',
    type: 'post',
    dataType: 'json',
    success: function(data){
        if(data != null){
            alert(data['data'][0]);
        }else{
            alert('信息获取失败');
        }
    },
    error: function(data){
        alert("服务器连接失败");
    }
});