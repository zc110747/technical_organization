
//node module
const mqtt = require('mqtt')

//user module
const { config_info } = require('./config_manage.js')

//global value:
let subscribe_info = {
    device: "off",
    info: {
        weather: {
            temp: '16',
            icon: '100',
            text: '阴',
            feel_temp: '15',
            idity:90
        },
        os:{
            CPU_temp: 0,
            CPU_usage: '5.0',
            RAM_used: '224',
            RAM_total: '245',
            Disk_used: '232',
            Disk_total: '375',
            ipaddress:"127.0.0.1",
            gateway:"0.0.0.0",
            netmask:"255.255.255.0",
            mqtt_server:"127.0.0.1",
            mqtt_port:0,
        }
    }
}

function init()
{
    try
    { 
        let mqtt_addr = `mqtt://${config_info.mqtt_server}:${config_info.mqtt_port}`;
        console.log(mqtt_addr)

        let client = mqtt.connect(mqtt_addr,  { 
            clientId: 'nodejs-mqtt-client' 
        });
    
        client.on('connect', function(){
            console.log('Connected to MQTT broker')
            client.subscribe(config_info.mqtt_subscribe_topic, {qos: 1});
        });
    
        client.on('message', function (topic, message) {
            const json_obj = JSON.parse(message.toString())
            for (let key in json_obj.weather){
                if(subscribe_info.info.weather.hasOwnProperty(key)){
                    subscribe_info.info.weather[key] = json_obj.weather[key]
                }
            }
            for (let key in json_obj.os){
                if(subscribe_info.info.os.hasOwnProperty(key)){
                    subscribe_info.info.os[key] = json_obj.os[key]
                }
            }
            subscribe_info.device = json_obj.device
            console.log(subscribe_info)
        })
    }
    catch(e)
    {
        console.log(e);
    }
}

//export var and function
module.exports.init = init
module.exports.subscribe_info = subscribe_info