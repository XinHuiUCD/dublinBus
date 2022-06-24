<template>
    <div id="Weather" style="height: 700px;">
        <div class="demo-collapse">
            <el-collapse v-model="activeName" accordion>
                <el-collapse-item title="&nbsp; Current Weather" name="1">
                    <div>
                        <img src="https://z4a.net/images/2022/06/23/night.png" style="width: 200px;">
                    </div>
                </el-collapse-item>
                <el-collapse-item title="&nbsp; Today's Weather" name="2">
                    <div>
                        <img src="https://z4a.net/images/2022/06/23/rain.png" style="width: 200px;">
                        <img src="https://z4a.net/images/2022/06/23/windy.png" style="width: 200px;">
                        <img src="https://z4a.net/images/2022/06/23/night.png" style="width: 200px;">
                    </div>
                </el-collapse-item>
                <el-collapse-item title="&nbsp; Future Weather" name="3">
                    <div>
                        <img src="https://z4a.net/images/2022/06/23/sunny.png" style="width: 200px;">
                    </div>
                </el-collapse-item>
            </el-collapse>
        </div>
    </div>
</template>

<script lang="ts" setup>
import {
    ref
} from 'vue'

const activeName = ref('1');

</script>


<style>
</style>
