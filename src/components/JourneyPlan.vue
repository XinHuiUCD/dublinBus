<template>
    <div id="Menu" style="height: 700px;">
        <div id="title">
            <h1>
                <span style="color: black">Plan Your Journery</span>&nbsp;
                <span style="color: gray">With DublinBus</span>
            </h1>
            <div id="function">
                <!-- Your Position -->
                <div class="input-group mb-3 enter">
                    <input type="text" class="form-control" v-model="ur_position" placeholder="Your Position"
                        aria-label="Username" aria-describedby="basic-addon1" clearable />
                </div>
                <!-- Your Destination -->
                <el-input v-model="ur_destination" class="w-50 m-2" placeholder="Your Destination" :prefix-icon="Search"
                    style="width: 100%; height: 40px; border-radius: 18px; margin-top: 20px;" clearable />

                <!-- Select date and time -->
                <div class="block">
                    <el-date-picker v-model="value2" type="datetime" placeholder="Pick a Date"
                        format="YYYY/MM/DD hh:mm:ss" value-format="YYYY-MM-DD h:m:s a"
                        style="height: 40px; border-radius: 18px; margin-top: 20px;" />
                </div>
                <div style="height: 300px; margin-top: 20px;">
                    <el-steps direction="vertical" :active="1">
                        <el-step title="Start" description="39A" />
                        <el-step title="Futher Info" description="" />
                        <el-step title="End" />
                    </el-steps>
                </div>
            </div>
        </div>
    </div>

</template>

<script setup lang="ts">
/* eslint-disable */
import { ref } from 'vue'
import {
    Calendar,
    Search
} from '@element-plus/icons-vue'

const ur_position = ref('')
const ur_destination = ref('')
const value2 = ref('')

</script>

<style scoped>
.enter {
    width: 80%;
    height: 40px;
    border-radius: 8px;
    margin-top: 20px;
}
</style>
