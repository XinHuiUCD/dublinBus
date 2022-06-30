<template>
    <div id="Weather" style="height: 700px;">
        <div class="demo-collapse">
            <el-collapse v-model="activeName" accordion>
                <el-collapse-item title="&nbsp; Current Weather" name="1">
                    <div>
                        <img src="https://z4a.net/images/2022/06/23/night.png" style="width: 200px;">

                        <h1>Hello World</h1>
                        <!-- <template v-for="index in result " :key="index">
                        <div>{{index.coord.lon}}</div>
                        </template> -->
                        {{result.main.temp}}
                    </div>
                </el-collapse-item>
                <el-collapse-item title="&nbsp; Today's Weather" name="2">
                    <div>
                        <img src="https://z4a.net/images/2022/06/23/rain.png" style="width: 200px;">
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

<script lang="ts">
/* eslint-disable */



import { result } from 'lodash';
import { defineComponent } from 'vue'


import {
    ref
} from 'vue'

const activeName = ref('1');


export default ({
  name: "WeatherData",
	setup(){
    const result = ref(null)
    const weather = {};
    


    fetch('https://api.openweathermap.org/data/2.5/weather?q=Ireland&units=metric&appid=17f166d4fd4137881f3c09b22dd04a7a')
      .then(response => response.json())
      .then(data => result.value = data)
      .then((result) => {
			console.log("helllooooo", result.weather[0].description)
            console.log("icon init",result.weather[0].icon);
        })


    return { result }

      
  }


});






</script>


<style>
</style>






