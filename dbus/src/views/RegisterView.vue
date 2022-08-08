<template>
    <ContentBase>
        <div class="row justify-content-md-center" id="register">
            <form @submit.prevent="register">
                <div class="mb-3">
                    <label for="username" class="form-label">Username</label>
                    <input v-model="username" type="etext" class="form-control" id="username">
                </div>
                <div class="mb-3">
                    <label for="password" class="form-label">Password</label>
                    <input v-model="password" type="password" class="form-control" id="password">
                </div>
                <div class="mb-3">
                    <label for="password" class="form-label">Confirm Password</label>
                    <input v-model="password_confirm" type="password" class="form-control" id="password_confirm">
                </div>
                <div class="error-message">{{ error_message }}</div>
                <button id="sigupBtn" type="submit" class="btn btn-primary">Sign Up</button>
            </form>
        </div>
    </ContentBase>
</template>

<script lang="ts">
import ContentBase from '../components/ContentBase.vue'
import { ref } from 'vue';
import { useStore } from 'vuex';
import router from '@/router/index';
import $ from 'jquery';


export default {
    name: "RegisterView",
    components: {
        ContentBase,
    },
    setup() {
        const store = useStore();
        let username = ref('');
        let password = ref('');
        let password_confirm = ref('');
        let error_message = ref('');

        const register = () => {
            error_message.value = "";
            $.ajax({
                url: "https://app165.acapp.acwing.com.cn/myspace/user/",
                type: "POST",
                data: {
                    username: username.value,
                    password: password.value,
                    password_confirm: password_confirm.value,
                },
                success(resp) {
                    if (resp.result === "success") {
                        store.dispatch("login", {
                            username: username.value,
                            password: password.value,
                            success() {
                                router.push({ name: 'home' });
                            },
                            error() {
                                error_message.value = "System Error, please retry later";
                            }
                        });
                    } else {
                        if (resp.result === "用户名已存在")
                            error_message.value = "This username already exists";
                        else if (resp.result === "两个密码不一致")
                            error_message.value = "The two passwords do not match";
                        else if (resp.result === "用户名和密码不能为空")
                            error_message.value = "The username and password can not be blanked!";
                    }
                }
            })
        };

        return {
            username,
            password,
            password_confirm,
            error_message,
            register,
        }

    }
}
</script>

<style scoped>
.error-message {
    color: red;
    font-size: 12px;
    margin-bottom: 10px;
}

button {
    width: 100%;
    margin-bottom: 10px;
}
</style>