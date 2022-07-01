<template>
  <div id="Weather" style="height: 700px;">
    <div class="demo-collapse">
      <el-collapse>
        <el-collapse-item title="&nbsp; Current Weather" name="1">
          <div>
            <img src="https://z4a.net/images/2022/06/23/night.png" style="width: 200px;">
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
            <button @click="getWeather" type="button" class="btn btn-primary">Primary
              {{ tempsLen }}</button>
          </div>
        </el-collapse-item>
      </el-collapse>
    </div>
  </div>
</template>

<script lang="ts">
import { ref } from 'vue';
import { useStore } from 'vuex';

export default {
  name: "WeatherDisplay",
  setup() {
    let temps = ref([]);
    let tempsLen = ref('');
    const store = useStore();

    const getWeather = () => {
      store.dispatch("getWeather");
      temps.value = store.state.weather.temps;
      tempsLen.value = store.state.weather.tempsLen;
    };

    return {
      temps,
      tempsLen,
      getWeather,
    };
  }
};

</script>


<style scoped>
</style>

