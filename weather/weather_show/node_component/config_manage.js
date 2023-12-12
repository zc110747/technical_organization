/*
配置文件解析，提前信息包含
1.本地服务器地址
*/
//global require
const fs = require('fs')
const os = require('os')

let config_info = {
    //web info
    web_ip: "127.0.0.1",
    web_port: 15059,
    web_path: "",
    web_gataway: '0.0.0.0',
    web_netmask: '255.0.0.0',

    //mqtt sever info
    mqtt_server: "127.0.0.1",
    mqtt_port: 1883,
    mqtt_subscribe_topic: "/public/weather/1",
    mqtt_publisher_topic: "/public/weather/2"
};

const get_and_check_ip = (ipaddr)=>{
    const interfaces = os.networkInterfaces();

    for(let devName in interfaces)
    {
        const iface = interfaces[devName];
        const len = iface.length;

        for(let index=0; index<len; index++)
        {
            if(iface[index].address == ipaddr)
            {
                let web_gataway = ipaddr.split(".").slice(0, -1)
                web_gataway.push('1');
                config_info.web_gataway = web_gataway.join('.');
                config_info.web_netmask = iface[index].netmask;
                return true;
            }
        }
    }
    return false;
}

function load_config_file(filePath)
{
    try
    {
        let resdata = fs.readFileSync(filePath).toString();
        let jsonValue = JSON.parse(resdata);
        
        get_and_check_ip(jsonValue.socket.socket_ip);

        config_info.web_ip = jsonValue.socket.socket_ip;
        config_info.web_port = jsonValue.node.port;
        config_info.web_path = jsonValue.node.page;

        let is_remote = jsonValue.use_remote;
        if(is_remote)
        {
            config_info.mqtt_server = jsonValue.remote_mqtt.socket_ip;
            config_info.mqtt_port = jsonValue.remote_mqtt.port;
        }
        else
        {
            config_info.mqtt_server = jsonValue.local_mqtt.socket_ip;
            config_info.mqtt_port = jsonValue.local_mqtt.port;
        }
        config_info.mqtt_subscribe_topic = jsonValue.res_topic;
        config_info.mqtt_publisher_topic = jsonValue.req_topic
        console.log("use config file:", config_info)
    }
    catch(err)
    {
        console.log(err);
    }
}

module.exports.load_config_file = load_config_file;
module.exports.config_info = config_info;

load_config_file("config.json")