/**
 * Created by 李珍鸿 on 2019/4/17.
 */
function onInputFileChange() {
    var file = document.getElementById('file').files[0];
    var url = URL.createObjectURL(file);
    console.log(url);
    document.getElementById("audio_id").src = url;
}
ctx = canvas.getContext("2d");
function capture(){
    ctx.drawImage(audio_id, 0, 0, 400, 300);
    var imageData = canvas.toDataURL();
        $.ajax({
        url: '/catch_image',
        type: 'post',
        data: imageData,
        success: function (data) {
            if (data != null) {
                ctx.drawImage(data, 0, 0, 400, 300);
            } else {
                alert('信息获取失败');
            }
        },
        error: function (data) {
            alert("服务器连接失败");
        }
    });
}