<template>
    <ContentBase>
        <div class="row justify-content-md-center" id="login">
                <form @submit.prevent="login">
                    <div class="mb-3">
                        <label for="username" class="form-label">Username</label>
                        <input v-model="username" type="etext" class="form-control" id="username">
                    </div>
                    <div class="mb-3">
                        <label for="password" class="form-label">Password</label>
                        <input v-model="password" type="password" class="form-control" id="password">
                    </div>
                    <div id="errorMsg" class="error-message">{{ error_message }}</div>
                    <button name="login_Button" id="loginBtn" type="submit" class="btn btn-primary">Log in</button>
                </form>
        </div>
    </ContentBase>
</template>

<script lang="ts">
import ContentBase from '../components/ContentBase.vue'
import { ref } from 'vue';
import { useStore } from 'vuex';
import routers from '@/router/index';

export default {
    name: "LoginView",
    components: {
        ContentBase,
    },
    setup() {
        const store = useStore();

        let username = ref('');
        let password = ref('');
        let error_message = ref('');

        const login = () => {
            error_message.value = '';
            store.dispatch("login", {
                username: username.value,
                password: password.value,
                success() {
                    routers.push({ name: "home" });
                },
                error() {
                    error_message.value = "Wrong username or password provided!";
                },
            });
        };

        return {
            username,
            password,
            error_message,
            login,
        }
    }
}
</script>

<style scoped>
button {
    width: 100%;
}

.error-message {
    color: red;
    font-size: 12px;
    margin-bottom: 10px;
}
</style>