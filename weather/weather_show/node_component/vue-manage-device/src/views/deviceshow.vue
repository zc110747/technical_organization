<template>
	<div class="container">
		<div class="plugins-tips">
			系统的工作状态, 包含CPU信息, 内存和硬盘占用情况和内部工作的状态信息。
		</div>
		<el-row :gutter="20">
			<el-col :span="10" style="max-width: 100%;">
			<div class="schart-box">
				<div class="content-title">cpu工作状态</div>
				<schart class="schart" canvasId="line" :options="cpu_usage"></schart>
			</div>
			</el-col>
			<el-col :span="12">
				<el-card shadow="hover" class="mgb20" style="margin-top: 40px; height: 330px">
					<template #header>
						<div class="clearfix">
							<span>其它信息</span>
						</div>
					</template>
					<div>
						<el-table :data="LocalSocketTable" border class="table" header-cell-class-name="table-header">
							<el-table-column prop="id" label="设备配置"></el-table-column>
							<el-table-column prop="info" label="设备信息"></el-table-column>
						</el-table>
					</div>		
				</el-card>	
			</el-col>
		</el-row>
		<div class="schart-box">
			<div class="content-title">内存占用(MB)</div>
			<schart class="schart" canvasId="canvas_ram"  :options="ram_usage"></schart>
		</div>
		<div class="schart-box">
			<div class="content-title">硬盘占用(GB)</div>
			<schart class="schart" canvasId="canvas_disk" :options="disk_usage"></schart>
		</div>
	</div>
</template>

<script setup lang="ts" name="basecharts">
import Schart from 'vue-schart';
import { ref} from 'vue';
import {onBeforeMount, onBeforeUnmount } from 'vue';
import { requestData } from '../api/index'
import {LocalSocketTable, GetSocketTable, cpu_usage, ram_usage, disk_usage, ResonsoleJsonProcess} from '../store/deviceshow'

const interval = ref(0);

GetSocketTable();

const interval_run_task = ()=>{
	requestData('./req_device', 'get').then((Pesponse)=>{
			 	console.log(Pesponse.data)
			
				ResonsoleJsonProcess(Pesponse.data);
			 }).catch((reason) =>{
			 	console.log(reason);
	});
};

//运行时钩子
onBeforeMount(() => {

	interval_run_task();
	if(interval.value == 0)
	{
		interval.value = window.setInterval(interval_run_task, 1000);
	}
});

onBeforeUnmount(() => {
	window.clearInterval(interval.value);
	interval.value = 0;
});
</script>

<style scoped>
.schart-box {
	display: inline-block;
	margin: 20px;
}
.schart {
	width: 600px;
	height: 280px;
}
.content-title {
	clear: both;
	font-weight: 400;
	line-height: 50px;
	margin: 10px 0;
	font-size: 22px;
	color: #1f2f3d;
}
.mgb20 {
	margin-bottom: 20px;
}
</style>
