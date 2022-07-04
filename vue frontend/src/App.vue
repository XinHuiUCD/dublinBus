<!-- <template>
	<div class="container">
		<NavBar>
			<theme-button />
		</NavBar>
		<div class="card">
			<router-view />
		</div>
	</div>
</template>


<script lang="ts">
	import 'bootstrap/dist/css/bootstrap.css'
	import 'bootstrap/dist/js/bootstrap'
	import 'element-plus/dist/index.css'
	import NavBar from './components/NavBar.vue'
	import ThemeButton from "./components/ThemeButton.vue";

	export default {
		name: "App",
		components: {
			NavBar,
			ThemeButton
		}
	}
</script>

<style>
</style> -->

<template>
	<div class="container">
		<div class="card">
			<NavBar />
			<theme-button />
			<router-view />
		</div>
	</div>
</template>

<script>
	import 'bootstrap/dist/css/bootstrap.css'
	import 'bootstrap/dist/js/bootstrap'
	import 'element-plus/dist/index.css'
	import NavBar from './components/NavBar.vue'
	import ThemeButton from "./components/ThemeButton.vue";

	export default {
		name: "App",
		components: {
			NavBar,
			ThemeButton,
		},
	};
</script>

<style>
	/* Define styles for the default root window element */
	:root {
		--background-color-primary: #ebebeb;
		--background-color-secondary: #fafafa;
		--accent-color: #cacaca;
		--text-primary-color: #222;
		--element-size: 4rem;
	}

	/* Define styles for the root window with dark - mode preference */
	:root.dark-theme {
		--background-color-primary: #1e1e1e;
		--background-color-secondary: #2d2d30;
		--accent-color: #3f3f3f;
		--text-primary-color: #ddd;
	}

	* {
		color: var(--text-primary-color);
	}

	.card {
		border: 1px solid var(--accent-color);
		background-color: var(--background-color-secondary);
	}
	.map {
		filter: grayscale(100%);
	}
</style>
