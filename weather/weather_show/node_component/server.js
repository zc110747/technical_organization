/*
基于node实现的web服务器,具体功能
1.解析json配置文件，用于ip地址和端口定义
2.web服务器，支持静态文件读取和动态处理
3.基于TCP的socket,和C++的axios服务器通讯
*/
//node module
const http = require('http');

//user module
const config_manage = require("./config_manage.js")
const static_engine = require('./static_engine.js')
const dynamic_engine = require('./dynamic_engine.js')
const mqtt_subscribe = require('./mqtt_subscribe.js')

//global parameter

const filepath = "config.json";

let server = http.createServer();
function start_server_work()
{
    console.log("node server start!")
    
    //加载配置信息
    config_manage.load_config_file(filepath)

    //定义服务器回调
    server.on('request', function (request, response) {
        if(static_engine.engine_process(request, response)){
            //console.log("static engine process success!");
        }
        else{
            dynamic_engine.dynamic_engine_process(request, response);
        }
    })

    //建立web服务器, 支持动态和静态处理
    //访问的界面文件在webpage/目录下
    console.log(`server run on http://${config_manage.config_info.web_ip}:${config_manage.config_info.web_port}, visit on browser!`);
    server.listen(config_manage.config_info.web_port, config_manage.config_info.web_ip, function (err) {
        if(err) throw err;
        console.log(`server start ok!`);
    })

    mqtt_subscribe.init()
}

start_server_work();





