import $ from 'jquery';

const ModuleWeather = {
    state: {
        temps: [],
        tempsLen: 0,
    },
    getters: {

    },
    mutations: {
        updateWeather(state, weather) {
            state.temps = weather.temps;
            state.tempsLen = weather.tempsLen;
        },
    },
    actions: {
        getWeather(context) {
            $.ajax({
                url: "https://api.openweathermap.org/data/2.5/onecall?lat=53.344&lon=-6.2672&units=metric&exclude=minutely,daily&appid=d6e328f404504a98d4be6d3942d42e9e",
                type: "GET",
                async: false,
                success(resp) {
                    context.commit("updateWeather", {
                        temps: resp.hourly,
                        tempsLen: resp.hourly.length,
                    });
                },
            });
        },
    },
    modules: {
    },
};


export default ModuleWeather;