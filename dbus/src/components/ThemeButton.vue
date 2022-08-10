<template>
	<div>
		<input @change="toggleTheme" id="checkbox" type="checkbox" class="switch-checkbox" />
		<label for="checkbox" class="switch-label">
			<span>🌙</span>
			<span>☀️</span>
			<div class="switch-toggle" :class="{ 'switch-toggle-checked': userTheme === 'dark-theme' }"></div>
		</label>
		{{ mode }}
	</div>
</template>

<script>
	export default {

		mounted() {
			const initUserTheme = this.getTheme() || this.getMediaPreference();
			this.setTheme(initUserTheme);
		},

		data() {
			return {
				userTheme: "light-theme",
			};
		},

		methods: {
			toggleTheme() {
				const activeTheme = localStorage.getItem("user-theme");
				if (activeTheme === "light-theme") {
					this.setTheme("dark-theme");
				} else {
					this.setTheme("light-theme");
				}
			},

			getTheme() {
				return localStorage.getItem("user-theme");
			},

			setTheme(theme) {
				localStorage.setItem("user-theme", theme);
				this.userTheme = theme;
				document.documentElement.className = theme;
			},

			getMediaPreference() {
				const hasDarkPreference = window.matchMedia(
					"(prefers-color-scheme: dark)"
				).matches;
				if (hasDarkPreference) {
					return "dark-theme";
				} else {
					return "light-theme";
				}
			},
		},
	};
	// code ref: https://dev.to/tqbit/create-your-own-dark-mode-toggle-component-with-vue-js-1284
</script>

<style scoped>
	.switch-checkbox {
		display: none;
	}

	.switch-label {
		align-items: center;
		background: var(--text-primary-color);
		border: calc(var(--element-size) * 0.025) solid var(--accent-color);
		border-radius: var(--element-size);
		cursor: pointer;
		display: flex;
		font-size: calc(var(--element-size) * 0.3);
		height: calc(var(--element-size) * 0.5);
		position: relative;
		padding: calc(var(--element-size) * 0.1);
		transition: background 0.5s ease;
		justify-content: space-between;
		width: var(--element-size);
		z-index: 1;
		float: right;
		margin-bottom: 20px;
		margin-right: 10px;
		/* margin-top: -20px; */
	}

	.switch-toggle {
		position: absolute;
		background-color: var(--background-color-primary);
		border-radius: 50%;
		top: calc(var(--element-size) * 0.07);
		left: calc(var(--element-size) * 0.07);
		height: calc(var(--element-size) * 0.35);
		width: calc(var(--element-size) * 0.35);
		transform: translateX(0);
		transition: transform 0.3s ease, background-color 0.5s ease;
	}

	.switch-toggle-checked {
		transform: translateX(calc(var(--element-size) * 0.6)) !important;
	}
</style>
