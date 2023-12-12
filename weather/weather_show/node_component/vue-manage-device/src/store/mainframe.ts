import { ref, reactive} from 'vue';
import request from '../utils/request';

export const weather = reactive({
	tempature:18,
	text:"晴",
	feel_temp:16,
	idity:85,
});

//"on", "off", "exception"
export const device = reactive({
	state:"off",
});

export const devicelist = reactive([
	{
		title: '',
	},
	{
		title: '',
	},
	{
		title: '',
	},
]);

export const requestData = () => {
    return request({
        url: './req_mainframe',
        method: 'get'
    });
};

export const ResonsoleJsonProcess = (data:any) => {
    weather.tempature = data.weather.temp;
    weather.text = weather.text;
    weather.feel_temp = data.weather.feel_temp;
    weather.idity = data.weather.idity;
    const state: string = data.device;
    if(device.state != state)
    {
        device.state = state;
        let sign:string = '';
        if(state == "on")
        {
            
        }

        devicelist.shift();
        devicelist.push({
            title: sign,
        });
    }
}