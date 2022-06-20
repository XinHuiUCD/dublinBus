<template>
	<nav id="navigation_button">
		<img src="@/assets/imgs/dblogo.png" style="width: 200px;position: left;">
		<el-button type="primary" plain style="margin-left: 30px;">Home</el-button>
		<el-button type="success" plain style="margin-left: 30px;">Journey Plan</el-button>
		<el-button type="warning" plain style="margin-left: 30px;">Fare Calculator</el-button>
		<el-button type="danger" plain style="float: right;margin-left: 30px">Logout</el-button>
		<el-button type="info" plain style="float: right;">About Us</el-button>

		<!-- Switch Button -->
		<el-switch v-model="dark_mode" class="mb-2"
			style="--el-switch-on-color: #000000; --el-switch-off-color: #eaeaea; display: block;float: right;margin-top: 10px"
			active-text="Dark" inactive-text="Light" />

	</nav>
</template>

<script lang="ts" setup>
	import {
		ref
	} from 'vue'

	const dark_mode = ref(true)
</script>

<style>

</style>
