import { App } from 'vue';
import { utcToTime, utcToDate, convertTimeZone, getWeather } from './utils';
export declare const OpenWeather: {
    install: (app: App) => void;
};
export { default as VueOpenWeather } from './VueOpenWeather.vue';
export { default as VueCurrentWeather } from './VueCurrentWeather.vue';
export { utcToTime, utcToDate, convertTimeZone, getWeather };
