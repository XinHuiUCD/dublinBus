<template>
    <div class="home">
        <div class="container">
            <div class="card">
                <div class="card-body">
                    <slot></slot>
                </div>
            </div>
        </div>
        <div class="common-layout">
            <el-container>

                <el-header>
                    <h1 style="color: #1dc1ec">About Us</h1>
                </el-header>

                <el-container>
                    <el-main>
                        <h3 style="color: #1dc1ec">Rating for us!</h3>
                        <el-rate v-model="value" :texts="['oops', 'disappointed', 'normal', 'good', 'great']" show-text
                            style="color: #1dc1ec" />

                        <!-- submit button -->
                        <el-divider border-style="dashed" />
                        <el-button text @click="dialogVisible = true" style="background-color: pink;">click here to
                            submit your rating</el-button>

                        <el-dialog v-model="dialogVisible" title="Tips" width="30%" :before-close="handleClose">
                            <span>We are pleased to receive your rating 😊</span>
                            <template #footer>
                                <span class="dialog-footer">
                                    <el-button @click="dialogVisible = false">Cancel</el-button>
                                    <el-button type="primary" @click="dialogVisible = false">Confirm</el-button>
                                </span>
                            </template>
                        </el-dialog>
                        <el-divider border-style="dashed" />
                    </el-main>
                </el-container>
            </el-container>
        </div>
        <footer style="text-align: center;margin-top: 10px;color: #1dc1ec">
            © 2022: XpressBusEgineering- Team 10
        </footer>
    </div>
</template>

<script lang="ts">
import {
    ref
} from 'vue'
import {
    ElMessageBox
} from 'element-plus'

const dialogVisible = ref(false)

export default {
    name: "ContentBase",
    components: {
    },
    data() {
        return {
            dialogVisible,
        }
    }
}

</script>

<style scoped>
.card-body {
    background: transparent;
}

.el-carousel__item:nth-child(2n) {
    background-color: #99a9bf;
    text-align: center;
}

.el-carousel__item:nth-child(2n + 1) {
    background-color: #d3dce6;
    text-align: center;
}
</style>