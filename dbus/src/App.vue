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
	--filter-invert: invert(1);
	--filter-grayscale: grayscale(1);
}

p {
	color: var(--text-primary-color);
}

.card {
	border: 1px solid var(--accent-color);
	background-color: var(--background-color-secondary);
}

.el-collapse * {
	background-color: var(--background-color-secondary);
	color: var(--text-primary-color);
}

#texts {
	color: var(--text-primary-color);
}


.el-autocomplete * {
	background-color: var(--background-color-secondary);
	color: var(--text-primary-color);
}

.form-control {
	background-color: var(--background-color-secondary);
	color: var(--text-primary-color);
}

.el-date-picker,
.el-input__wrapper{
	background-color: var(--background-color-secondary);
	color: var(--text-primary-color);
}

.el-date-picker,
.el-picker-panel__footer {
	background-color: var(--background-color-secondary);
	color: var(--text-primary-color);
}

.el-date-picker,
.el-button+.el-button {
	background-color: var(--background-color-secondary);
	color: var(--text-primary-color);
}

.el-time-panel {
	background-color: var(--background-color-secondary);
	color: var(--text-primary-color);
}

.el-button {
	background-color: var(--background-color-secondary);
	color: var(--text-primary-color);
}

.el-input {
	background-color: var(--background-color-secondary);
	color: var(--text-primary-color);
}

.twitter-timeline {
	filter: var(--filter-invert);
}

#map {
	filter: var(--filter-invert);
}

.pac-target-input {
	background-color: var(--background-color-secondary);
	color: var(--text-primary-color);
}

.btn {
	color: var(--text-primary-color);
}

#browser {
	background-color: var(--background-color-secondary);
	color: var(--text-primary-color);
}

#browsers {
	background-color: var(--background-color-secondary);
	color: var(--text-primary-color);
}

#addFavourite {
	background-color: var(--background-color-secondary);
	color: var(--text-primary-color);
}

#myForm {
	filter: var(--filter-invert);
}

.el-button {
	filter: var(--filter-invert);
}

#login {
	background-color: var(--background-color-secondary);
	color: var(--text-primary-color);
}

#register {
	background-color: var(--background-color-secondary);
	color: var(--text-primary-color);
}

#MlResult {
	background-color: var(--background-color-secondary);
	color: var(--text-primary-color);
}
</style>
