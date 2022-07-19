<template>
    <ContentBase>
        <div id="Menu">
            <div id="title">
                <div id="function">
                    <!-- Your Position -->
                    <div class="input-group mb-3">
                        <button class="btn btn-outline-secondary" type="button" id="button-addon1">🔍</button>
                        <input type="text" class="form-control" placeholder="RouteID" v-model="routeId" show-clear>
                    </div>
                    <div>
                        <datalist id="suggestions">
                            <option>First option</option>
                            <option>Second Option</option>
                        </datalist>
                        <input  autoComplete="on" list="suggestions"/> 
                    </div>


                    <!-- submit -->
                    <button class="btn btn-outline-secondary" type="submit" @click="submit"
                        style="margin-top: 10px;margin-left: 20px;width: 70px;height: 60px;background-color: chartreuse;">Submit️</button>
                </div>
            </div>
        </div>
    </ContentBase>
</template>

<script lang="ts">
import ContentBase from '../components/ContentBase.vue'
// import VueGoogleAutocomplete from "vue-google-autocomplete"
import { ref } from 'vue';
import $ from 'jquery';

export default {
    name: "RouteStopInfoView",
    components: {
        ContentBase,
    },
    setup() {
        let routeId = ref('');
        const submit = () => {
            $.ajax({
                url: "http://127.0.0.1:9000/getinfo",
                type: "GET",
                data: {
                    routeId: routeId.value,
                },
                success(resp) {
                    console.log(resp);
                }
            });
        };

        return {
            routeId,
            submit,
        }
    }
}
</script>

<style scoped>
</style>