import { ref} from 'vue';

interface TableItem {
    id: string;
    info: string;
}
export const LocalSocketTable = ref<TableItem[]>([]);
export const GetSocketTable = () => {
    LocalSocketTable.value = [
        {
            id: "ipaddress",
            info: "192.168.16.52",
        },
        {
            id: "gateway",
            info: "192.168.16.1",
        },
        {
            id: "netmask",
            info: "255.255.255.0",
        },
		{
			id: "mqtt server",
			info:"192.168.16.52"
		},
		{
			id: "mqtt port",
			info:"1883"
		}
    ];
};

export const cpu_usage = ref({
	type: 'line',
	title: {
		text: 'CPU状态'
	},
	bgColor: '#fbfbfb',
	labels: ['1', '2', '3', '4', '5'],
	datasets: [
		{
			label: '使用率',
			data: [0, 0, 0, 0, 0]
		},
		{
			label: '温度',
			data: [0, 0, 0, 0, 0]
		}
	]
});

export const ram_usage = ref({
	type: 'pie',
	title: {
		text: '内存使用情况'
	},
	legend: {
		position: 'left'
	},
	bgColor: '#fbfbfb',
	labels: ['未使用', '已使用'],
	datasets: [
		{
			data: [334, 278]
		}
	]
});

export const disk_usage = ref({
	type: 'pie',
	title: {
		text: '硬盘使用情况'
	},
	legend: {
		position: 'left'
	},
	bgColor: '#fbfbfb',
	labels: ['未使用', '已使用'],
	datasets: [
		{
			data: [123, 65]
		}
	]
});

const local_cpu_process = ref({
	info:[
		{
			label: '使用率',
			data: [0, 5, 15, 12, 100]
		},
		{
			label: '温度',
			data: [0, 45, 25, 15, 60]
		}
	]
});
const local_socket_info = ref([
        {
            id: "ipaddress",
            info: "192.168.16.52",
        },
        {
            id: "gateway",
            info: "192.168.16.1",
        },
        {
            id: "netmask",
            info: "255.255.255.0",
        },
		{
			id: "mqtt server",
			info:"192.168.16.52"
		},
		{
			id: "mqtt port",
			info:"1883"
		}
]);

export const ResonsoleJsonProcess = (ResponseData:any)=>{

	//process disk used
	const disk_used = parseFloat(ResponseData.Disk_used);
	const disk_total = parseFloat(ResponseData.Disk_total);
	const disk_obj = [
		{
			data: [disk_total-disk_used, disk_used]
		}
	];	
	disk_usage.value.datasets = disk_obj;
					
	//process ram used
	const ram_used = parseFloat(ResponseData.RAM_used);
	const ram_total = parseFloat(ResponseData.RAM_total);
	const ram_obj = [
		{
			data: [ram_total-ram_used, ram_used]
		}
	]
	ram_usage.value.datasets = ram_obj;

	//process cpu
	const cpu_temp = ResponseData.CPU_temp;
	const now_cpu_usage = parseFloat(ResponseData.CPU_usage);
	local_cpu_process.value.info[0].data.shift();
	local_cpu_process.value.info[0].data.push(cpu_temp);
	local_cpu_process.value.info[1].data.shift();
	local_cpu_process.value.info[1].data.push(now_cpu_usage);
	cpu_usage.value.datasets = local_cpu_process.value.info;

	// id: "ipaddress",
	// id: "gateway",
	// id: "netmask",
	// id: "mqtt server",
	// id: "mqtt port",
	local_socket_info.value[0].info = ResponseData.ipaddress;
	local_socket_info.value[1].info = ResponseData.gateway;
	local_socket_info.value[2].info = ResponseData.netmask;
	local_socket_info.value[3].info = ResponseData.mqtt_server;
	local_socket_info.value[4].info = ResponseData.mqtt_port;	
	LocalSocketTable.value = local_socket_info.value;
}
