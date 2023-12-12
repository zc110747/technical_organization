<template>
	<div>
		<el-row :gutter="20">
			<el-col :span="8">
				<el-card shadow="hover" class="mgb20" style="height: 252px">
					<div class="user-info">
						<el-avatar :size="120" :src="imgurl" />
						<div class="user-info-cont">
							<div class="user-info-name">{{ name }}</div>
							<div>{{ role }}</div>
						</div>
					</div>
					<div class="user-info-list">
						上次登录时间：
						<span>2023-10-23</span>
					</div>
					<div class="user-info-list">
						上次登录地点：
						<span>上海</span>
					</div>
				</el-card>
				<el-card shadow="hover" style="height: 252px">
					<template #header>
						<div class="clearfix">
							<span>每日天气</span>
						</div>
					</template>
					<div style="margin-left: 20px;">
						<div class="grid-content grid-con-1">
							<el-avatar :size="75" :src="weatherimgurl" />
							<div class = "weather-cont-left">
								<p>{{ weather.text }}</p>
								<p>{{ weather.tempature }}<span>°</span></p>					
							</div>
						</div>
						<div class="weather-local">
							<p>体感温度:{{ weather.feel_temp }}°</p>
							<p>当前湿度:{{ weather.idity }}%</p>
						</div>
					</div>		
				</el-card>
			</el-col>
			<el-col :span="16">
				<el-row :gutter="20" class="mgb20">
					<el-col :span="8">
						<el-card shadow="hover" :body-style="{ padding: '0px' }">
							<div class="grid-content grid-con-1">
								<el-icon class="grid-con-icon"><User /></el-icon>
								<div class="grid-cont-right">
									<div class="grid-num">0</div>
									<div>用户访问量</div>
								</div>
							</div>
						</el-card>
					</el-col>
					<el-col :span="8">
						<el-card shadow="hover" :body-style="{ padding: '0px' }">
							<div class="grid-content grid-con-2">
								<el-icon class="grid-con-icon"><ChatDotRound /></el-icon>
								<div class="grid-cont-right">
									<div class="grid-num">2</div>
									<div>系统消息</div>
								</div>
							</div>
						</el-card>
					</el-col>
					<el-col :span="8">
						<el-card shadow="hover" :body-style="{ padding: '0px' }">
							<div class="grid-content grid-con-3">
								<el-icon class="grid-con-icon"><Goods /></el-icon>
								<div class="grid-cont-right">
									<div class="grid-num">1</div>
									<div>设备数量</div>
								</div>
							</div>
						</el-card>
					</el-col>
				</el-row>
				<el-card shadow="hover" style="height: 403px">
					<template #header>
						<div class="clearfix">
							<span>设备连接状态</span>
						</div>
					</template>
						<div style="margin-left: 10px;">
							<div v-if="device.state == 'off'">
								<div style="font-size: 100px">
									<el-icon><Loading /></el-icon>
								</div>
								<div>设备连接中...</div>
							</div>
							<div v-else>
								<div style="font-size: 100px">
									<el-icon><Link /></el-icon>
								</div>
								<div>设备已连接</div>
							</div>
						</div>
				</el-card>
			</el-col>
		</el-row>
		<el-row :gutter="20">
			<el-col :span="24">
			<el-card shadow="hover" class="mgb20" style="height: 252px">
				<template #header>
						<div class="clearfix">
							<span>记录消息</span>
						</div>
				</template>

				<el-table :show-header="false" :data="devicelist" style="width: 100%">
					<el-table-column>
						<template #default="scope">
							<div class="todo-item">
								{{ scope.row.title }}
							</div>
						</template>
					</el-table-column>
				</el-table>
			</el-card>
			</el-col>
		</el-row>
	</div>
</template>

<script setup lang="ts" name="dashboard">
import {onBeforeMount, onBeforeUnmount } from 'vue';
import imgurl from '../assets/img/img.jpg';
import weatherimgurl from '../assets/img/weather/101.png';
import { ref} from 'vue';
import { requestData , ResonsoleJsonProcess, devicelist, weather, device} from '../store/mainframe'

const name = localStorage.getItem('ms_username');
const role: string = name === 'admin' ? '超级管理员' : '普通用户';

const interval = ref(0);
const interval_run_task = ref(()=>{
	requestData().then((Pesponse)=>{
			 	console.log(Pesponse.data)
			
				ResonsoleJsonProcess(Pesponse.data)
			}).catch((reason) =>{
			 	console.log(reason);
		});
});

//运行时钩子
onBeforeMount(() => {
	interval_run_task.value();
	if(interval.value == 0)
	{
		interval.value = window.setInterval(interval_run_task.value, 1000);
	}
});

onBeforeUnmount(() => {
	window.clearInterval(interval.value);
	interval.value = 0;
});
</script>

<style scoped>
.el-row {
	margin-bottom: 20px;
}

.grid-content {
	display: flex;
	align-items: center;
	height: 100px;
}

.grid-cont-right {
	flex: 1;
	text-align: center;
	font-size: 14px;
	color: #999;
}

.grid-num {
	font-size: 30px;
	font-weight: bold;
}

.grid-con-icon {
	font-size: 50px;
	width: 100px;
	height: 100px;
	text-align: center;
	line-height: 100px;
	color: #fff;
}

.grid-con-1 .grid-con-icon {
	background: rgb(45, 140, 240);
}

.grid-con-1 .grid-num {
	color: rgb(45, 140, 240);
}

.grid-con-2 .grid-con-icon {
	background: rgb(100, 213, 114);
}

.grid-con-2 .grid-num {
	color: rgb(100, 213, 114);
}

.grid-con-3 .grid-con-icon {
	background: rgb(242, 94, 67);
}

.grid-con-3 .grid-num {
	color: rgb(242, 94, 67);
}

.user-info {
	display: flex;
	align-items: center;
	padding-bottom: 20px;
	border-bottom: 2px solid #ccc;
	margin-bottom: 20px;
}

.user-info-cont {
	padding-left: 50px;
	flex: 1;
	font-size: 14px;
	color: #999;
}

.user-info-cont div:first-child {
	font-size: 30px;
	color: #222;
}

.user-info-list {
	font-size: 14px;
	color: #999;
	line-height: 25px;
}

.user-info-list span {
	margin-left: 70px;
}

.weather-local {
	font-size: 16px;
	color: black;
	margin-left: 5px;
	margin-top: 5px;
}

.weather-cont-left {
	flex: 1;
	text-align: left;
	font-size: 30px;
	margin-left: 10px;
	color: #222121;
}

.mgb20 {
	margin-bottom: 20px;
}

.todo-item {
	font-size: 14px;
}

.todo-item-del {
	text-decoration: line-through;
	color: #999;
}

.schart {
	width: 100%;
	height: 300px;
}
</style>
