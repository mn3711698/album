

init_post = {
    api_repost: "http://127.0.0.1:8000/monitor/repost/"
}

//document.write("<meta http-equiv=Content-Type content=text/html;charset=utf-8>");
//document.write("<script src='http://code.jquery.com/jquery-1.6.2.min.js'></script>");

function getCookie(c_name) {

    if (document.cookie.length > 0) {
        c_start = document.cookie.indexOf(c_name + "=")
        if (c_start != -1) {
            c_start = c_start + c_name.length + 1
            c_end = document.cookie.indexOf(";", c_start)
            if (c_end == -1) c_end = document.cookie.length
            return decodeURIComponent(document.cookie.substring(c_start, c_end))
        }
    }

    return ""

}

//json_get
function parse_cookie_json() {

    var cookie_data = getCookie('key')
    arrs = eval('(' + cookie_data.toString() + ')')
    var time = arrs.time
    var hotelname = arrs.hotelname
    var account = arrs.account
    return time + "|" + hotelname + "|" + account
}

//get local url
function parse_url() {
    var url = document.URL
    return url
}

//send data
function send_data(datas) {
    $.post(init_post.api_repost, datas);
}


//动态获取button a标签按钮啊 #自定义属性内容    #并发送数据
var mintor_data = ""
$('button[sendtype="1"]').live('click', function (){
    var mintor = $(this).attr('mintor')
    mintor_data = mintor
    cookie_data ="1"+"|"+"北京酒店"+"|"+"301063019"
    url = parse_url()
    var timestamp = Date.parse(new Date());
    send_data( cookie_data +"|"+mintor_data + "|"  + url +"|" + timestamp)
});

$('a[sendtype="1"]').live('click', function () {
    var mintor = $(this).attr('mintor')
    mintor_data = "1"+"|"+"北京酒店"+"|"+"301063019"
    cookie_data = parse_cookie_json()
    url = parse_url()
    var timestamp = Date.parse(new Date());
    send_data(cookie_data + "|"+ mintor_data + "|" + url +"|" + timestamp)
});