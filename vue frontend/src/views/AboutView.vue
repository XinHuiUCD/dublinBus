<template>
	<ContentBase>
		<div class="common-layout">
			<el-container>

				<el-header>
					<h1 style="color: #1dc1ec">About Us</h1>
				</el-header>

				<el-container>
					<el-aside width="300px">
						<h3 style="color: #1dc1ec">Rating for us!</h3>
						<br />
						<span class="content" style="color: #1dc1ec">User Experience</span>
						<br />
						<el-rate v-model="value" :texts="['oops', 'disappointed', 'normal', 'good', 'great']"
							show-text style="color: #1dc1ec"/>
						<br />
						<span class="content" style="color: #1dc1ec">Product Quality</span>
						<br />
						<el-rate v-model="value1" :texts="['oops', 'disappointed', 'normal', 'good', 'great']"
							show-text style="color: #1dc1ec" />
						<br />
						<span class="content" style="color: #1dc1ec">What Else?</span>
						<br />
						<el-rate v-model="value2" :texts="['oops', 'disappointed', 'normal', 'good', 'great']"
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
					</el-aside>

					<el-container>
						<el-main>
							<h3 style="color: #1dc1ec">Our Members</h3>
							<el-carousel :interval="3000" type="card" height="200px">
								<el-carousel-item v-for="item in 4" :key="item">
									<h3 text="2xl" justify="center">{{ item }}</h3>
								</el-carousel-item>
							</el-carousel>
						</el-main>
						<el-footer>Footer</el-footer>
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
		ref
	} from 'vue'
	import {
		ElMessageBox
	} from 'element-plus'

	const dialogVisible = ref(false)
	const value = ref()
	const value1 = ref()
	const value2 = ref()
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
				value,
				value1,
				value2,
				dialogVisible
			}
		}
	};
</script>

<style scoped>
	.el-carousel__item h3 {
		color: #475669;
		opacity: 0.75;
		line-height: 200px;
		margin: 0;
		text-align: center;
	}

	.el-carousel__item:nth-child(2n) {
		background-color: #99a9bf;
	}

	.el-carousel__item:nth-child(2n + 1) {
		background-color: #d3dce6;
	}
</style>