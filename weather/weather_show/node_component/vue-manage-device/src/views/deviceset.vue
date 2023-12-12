<template>
    <div class="container">
        <div class="form-box">
            <el-form ref="formRef" :rules="rules" :model="form" label-width="80px">
                <el-form-item label="ip地址" prop="name">
                    <el-input v-model="form.ipaddress"></el-input>
                </el-form-item>
                <el-form-item label="网关" prop="name">
                    <el-input v-model="form.gateway"></el-input>
                </el-form-item>
                <el-form-item label="子网掩码" prop="name">
                    <el-input v-model="form.netmask"></el-input>
                </el-form-item>
                <el-form-item label="MQTT" prop="resource">
                    <el-radio-group v-model="form.resource">
                        <el-radio label="本地服务器"></el-radio>
                        <el-radio label="远端服务器"></el-radio>
                    </el-radio-group>
                </el-form-item>
                <el-form-item label="工作灯" prop="led">
                    <el-switch v-model="form.led"></el-switch>
                </el-form-item>   
                <el-form-item label="蜂鸣器" prop="beep">
                    <el-switch v-model="form.beep"></el-switch>
                </el-form-item>               
                <el-form-item>
                    <el-button type="primary" @click="onSubmit(formRef)">配置提交</el-button>
                    <el-button @click="onReset(formRef)">重置参数</el-button>
                </el-form-item>
            </el-form>
        </div>
    </div>
</template>

<script setup lang="ts" name="baseform">
import { reactive, ref } from 'vue';
import { ElMessage } from 'element-plus';
import type { FormInstance, FormRules } from 'element-plus';

const rules: FormRules = {
   //name: [{ required: true, message: '请输入表单名称', trigger: 'blur' }],
};
const formRef = ref<FormInstance>();
const form = reactive({
    ipaddress: '127.0.0.1',
    gateway: '0.0.0.0',
    netmask: '255.255.255.0',
    resource: '本地服务器',
    led:false,
    beep:true,
});

// 提交
const onSubmit = (formEl: FormInstance | undefined) => {
    // 表单校验
    if (!formEl) return;
    formEl.validate((valid) => {
        if (valid) {
            console.log(form);
            ElMessage.success('提交成功！');
        } else {
            return false;
        }
    });
};

// 重置
const onReset = (formEl: FormInstance | undefined) => {
    if (!formEl) return;
    console.log(form);
    formEl.resetFields();
};
</script>
