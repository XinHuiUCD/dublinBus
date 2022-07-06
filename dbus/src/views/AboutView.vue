<template>
	<ContentBase>
		<div class="common-layout">
			<el-container>

				<el-header>
					<h1 style="color: #1dc1ec">About Us</h1>
				</el-header>

					<el-container>
						<el-main>
						<h3 style="color: #1dc1ec">Rating for us!</h3>
						<el-rate v-model="value" :texts="['oops', 'disappointed', 'normal', 'good', 'great']"
							show-text style="color: #1dc1ec"/>

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
							<h3 style="color: #1dc1ec">Our Members</h3>
							<el-carousel :interval="3000" type="card" height="200px">
								<el-carousel-item v-for="item in carouseImgs" :key="item">
									<img :src="item.url" alt=""/>
								</el-carousel-item>
							</el-carousel>
						</el-main>
					</el-container>
				</el-container>
		</div>
	</ContentBase>
</template>

<script lang="ts">
	/* eslint-disable */
	import ContentBase from '../components/ContentBase.vue'
	import {
		ref
	} from 'vue'
	import {
		ElMessageBox
	} from 'element-plus'

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
					{ url: require("../assets/photo1.png")},
					{ url: require("../assets/photo1.png")},
					{ url: require("../assets/photo1.png")},
					{ url: require("../assets/photo1.png")},
				]
			}
		}
	};
</script>

<style scoped>
	.el-carousel{
		width: 40%;
		
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