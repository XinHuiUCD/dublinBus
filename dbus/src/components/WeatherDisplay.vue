<!-- <template>
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
 -->


<!-- <template>


<div class="weather-widget-container">
  <open-weather-widget :api-key="17f166d4fd4137881f3c09b22dd04a7a"/>
</div>



</template>


<script>

import OpenWeatherWidget from 'vueOpenWeatherWidget'
import 'vue-open-weather-widget/dist/vue-open-weather-widget.css'

export default{
  components: {
    OpenWeatherWidget
  }
}



</script>


<style lang="scss">




:root {
  --bg-color-1: rgb(233, 233, 239);
}

.weather-widget-container {
  width: 320px;
  height: 380px;
  border-radius: 12px;
  box-shadow: 
    0px 0px 2px 4px rgba(255, 255, 255, 0.1),
    -12px -12px 32px rgba(255, 255, 255, 0.5),
    12px 12px 32px rgba(0, 0, 0, 0.1);
}

#app .open-weather-widget {
  border-radius: 12px;
  background-color: var(--bg-color-1);
  &__input-element {
    & label {
      background-color: var(--bg-color-1);
    }
  }
  &__sortable-list {
    &__item {
      padding: 12px;
      margin: 16px 0;
      background-color: var(--bg-color-1);
      border-radius: 4px;
      border: none;
      box-shadow: 
        -2px -2px 8px rgba(255,255,255,0.6), 
        2px 2px 8px rgba(0,0,0,0.1);
    }
  }
}

#app #open-weather-widget {
  &__loading-screen {
    background-color: var(--bg-color-1);
  }
}
</style> -->



<template>
      <div class="temp">
        <span>{{ weather.temp }}&deg;C</span>
        <span v-html="weather.icon"></span>
      </div>
</template>

<script>
export default {
  data() {
    return {
      weather: {
        temp: 14,
        description: "null",
        icon: "10n",
      },
    };
  },
  methods: {
    getWeather: async function () {
      const weatherURL = "/weather";
      const response = await fetch(weatherURL);
      const data = await response.json();
      
      this.weather.temp = Math.round(data.temp);
      this.weather.icon = "<img src=\"http://openweathermap.org/img/wn/" + data.icon + "@2x.png\"></img>";
    },
  },
  beforeMount() {
    this.getWeather();
  },
};
</script>

<style scoped>
.temp {
  font-weight: 100;
  font-size: 1.5em;
  letter-spacing: -1px;
  white-space: nowrap;
  color: white;
}
.card-mid {
line-height: 0.1;
}
@media only screen and (max-width: 600px) {
  .temp {
    width: 50%;
    font-size: 1.2em;
  }
}
</style>
