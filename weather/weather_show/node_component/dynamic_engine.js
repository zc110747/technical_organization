/*
动态引擎处理
对于界面提交的命令, 进行解析并处理

*/
const url = require('url');
const { subscribe_info } = require('./mqtt_subscribe.js');
const { config_info } = require('./config_manage.js');

const use_mock = 0;
const mainframeInfo = {
    device:"",
    weather:{}
}

let mock_tick = 0;
function mock_run(req_data)
{
    if(use_mock == 1)
    {
        if(req_data == 'req_mainframe')
        {
            mainframeInfo.weather = subscribe_info.info.weather;
            if(mock_tick == 1)
            {
                mainframeInfo.device = 'off';
            }
            else if(mock_tick == 2)
            {
                mainframeInfo.device = "25";
                mainframeInfo.weather.text = '晴';
            }
            else if(mock_tick == 3)
            {
                mainframeInfo.weather.idity = '95';
            }
            else
            {
                mock_tick = 0;
                mainframeInfo.device = 'on';
                mainframeInfo.weather.text = '多云';
                mainframeInfo.weather.idity = 80;
            }
        }
    }
    mock_tick++;
}

function dynamic_engine_process(request, response)
{
    let Query = url.parse(request.url);
    let is_process_ok = false;

    if(Query.pathname)
    {
        let action = Query.pathname.slice(1);
        //console.log(action + " " + Query.query);
        response.setHeader('Content-Type', 'application/json;charset=utf-8');

        mock_run(action);
        switch(action)
        {
            case 'axiosDeviceSet':
                is_process_ok = device_set_process(Query.query);
                response.end("ack " + (is_process_ok?"ok":"false"));
                break;
            case 'axiosDeviceGet':
                console.log(subscribe_info.info);
                response.end(JSON.stringify(subscribe_info.info));
                break;
            case 'req_mainframe':
                mainframeInfo.device = subscribe_info.device;
                mainframeInfo.weather = subscribe_info.info.weather;
                response.end(JSON.stringify(mainframeInfo));
                break;
            case 'req_device':
                subscribe_info.info.os.ipaddress = config_info.web_ip;
                subscribe_info.info.os.gateway = config_info.web_gataway;
                subscribe_info.info.os.netmask = config_info.web_netmask;
                subscribe_info.info.os.mqtt_server = config_info.mqtt_server;
                subscribe_info.info.os.mqtt_port = config_info.mqtt_port;                
                response.end(JSON.stringify(subscribe_info.info.os));
                break;
            default:
                break;
        }
    }
}

module.exports.dynamic_engine_process = dynamic_engine_process;