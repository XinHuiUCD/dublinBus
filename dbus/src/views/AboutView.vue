<template>
	<ContentBase>
		<div class="common-layout">
			<el-container>
				<el-container>
					<el-aside width="30%">
						<h3 style="color: #1dc1ec;margin-top: 9%;">Rating for us!</h3>
						<el-rate v-model="value" :texts="['oops', 'disappointed', 'normal', 'good', 'great']" show-text
							style="color: #1dc1ec" />

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
					</el-aside>

					<el-container>
						<el-main>
							<h1 style="color: #1dc1ec">About Us</h1>
							<el-descriptions border>
								<el-descriptions-item label="Staff Name" align="center" label-class-name="my-label"
									class-name="my-content" width="150px">Cheng Zhang, Gus Boothman, Will O'Donohoe,
									Xinhui Jiang
								</el-descriptions-item>
								<el-descriptions-item label="Telephone" align="center">017167777
								</el-descriptions-item>
								<el-descriptions-item label="Place" align="center">Dublin
								</el-descriptions-item>
								<el-descriptions-item label="Remarks" align="center">
									<el-tag size="small">School</el-tag>
								</el-descriptions-item>
								<el-descriptions-item label="Address" align="center">University College Dublin,
									Belfield, Dublin 4</el-descriptions-item>
							</el-descriptions>
							<el-divider border-style="dashed" />
							<h3 style="color: #1dc1ec">Our Members</h3>
							<el-carousel :interval="3000" type="card" height="200px">
								<el-carousel-item v-for="item in carouseImgs" :key="item">
									<img :src="item.url" alt="" />
								</el-carousel-item>
							</el-carousel>
						</el-main>
						<el-footer>

						</el-footer>
					</el-container>
				</el-container>
			</el-container>
		</div>
	</ContentBase>
</template>

<script lang="ts">
/* eslint-disable */
import ContentBase from '../components/ContentBase.vue'
import {
	ref, reactive
} from 'vue'
import {
	ElMessageBox
} from 'element-plus'

const form = reactive({
	name: '',

})

const dialogVisible = ref(false)
const handleClose = (done: () => void) => {
	ElMessageBox.confirm('Are you sure to close this dialog?')
		.then(() => {
			done()
		})
		.catch(() => {
			// catch error
		})
}

export default {
	name: "AboutView",
	components: {
		ContentBase,
	},
	data() {
		return {
			dialogVisible,
			carouseImgs: [
				{ url: require("../assets/photo1.png") },
				{ url: require("../assets/photo2.png") },
				{ url: require("../assets/photo3.png") },
				{ url: require("../assets/photo4.jpg") },
			]
		}
	}
};
</script>

<style scoped>
.el-carousel__item:nth-child(2n) {
	background-color: #99a9bf;
	text-align: center;
}

.el-carousel__item:nth-child(2n + 1) {
	background-color: #d3dce6;
	text-align: center;
}

.my-label {
	background: var(--el-color-success-light-9);
}

.my-content {
	background: var(--el-color-danger-light-9);
}
</style>