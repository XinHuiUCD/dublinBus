<template>
	<nav class="navbar navbar-expand-lg">
		<div class="container">
			<router-link class="navbar-brand" :to="{ name: 'home' }">
				<img src="https://z4a.net/images/2022/06/23/dublinBus.jpg" />
			</router-link>
			<button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarText"
				aria-controls="navbarText" aria-expanded="false" aria-label="Toggle navigation">
				<span class="navbar-toggler-icon"></span>
			</button>
			<div class="collapse navbar-collapse" id="navbarText">
				<ul class="navbar-nav me-auto mb-2 mb-lg-0">
					<li class="nav-item">
						<div class="card">
							<div class="card-body">
								<router-link class="nav-link active" aria-current="page" :to="{ name: 'home' }">Home
								</router-link>
							</div>
						</div>
					</li>
				</ul>
				<ul class="navbar-nav">
					<li class="nav-item">
						<el-switch v-model="dark_mode" class="mb-2"
							style="--el-switch-on-color: #000000; --el-switch-off-color: #eaeaea; display: block;float: right;margin-top: 10px"
							active-text="🌛" inactive-text="🌞" />
					</li>
					<li class="nav-item">
						<div class="card">
							<div class="card-body">
								<router-link class="nav-link active" aria-current="page" :to="{ name: 'about' }">About
								</router-link>
							</div>
						</div>
					</li>
					<li class="nav-item">
						<div class="card">
							<div class="card-body">
								<router-link class="nav-link active" :to="{ name: 'login' }">Log out</router-link>
							</div>
						</div>
					</li>
				</ul>
			</div>
		</div>
	</nav>
</template>

<script lang="ts">
	/* eslint-disable */
	import {
		ref
	} from 'vue'

	const dark_mode = ref(false)

	export default {
		name: "NavBar",
		data(){
			return{
				dark_mode
			}
		}
	};
</script>


<style scoped>
	img {
		width: 200px;
	}

	.card {
		margin-left: 20px;
	}

	.card-body {
		padding: 2px 8px;
	}
</style>