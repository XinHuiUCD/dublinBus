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
		
		// computed: {
		// 	map() {
		// 		return this.$store.state.map;
		// 	},
		// },
		// watch: {
		// 	map() {
		// 		this.initAuto();
		// 	}
		// },

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
				this.changeMap();
				this.$emit('toggleTheme', this.userTheme.toLowerCase());
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
			// initAuto: function() {
			// 	const controlDiv = document.getElementById("checkbox");
			// 	this.map.controls[window.google.maps.ControlPosition.TOP_RIGHT].push(controlDiv);
			// },
			// changeMap: function() {
			// 	if (this.userTheme === 'dark-theme') {
			// 		this.map.setOptions({
			// 			styles: [{
			// 					elementType: "geometry",
			// 					stylers: [{
			// 						color: "#242f3e"
			// 					}]
			// 				},
			// 				{
			// 					elementType: "labels.text.stroke",
			// 					stylers: [{
			// 						color: "#242f3e"
			// 					}]
			// 				},
			// 				{
			// 					elementType: "labels.text.fill",
			// 					stylers: [{
			// 						color: "#746855"
			// 					}]
			// 				},
			// 				{
			// 					featureType: "administrative.locality",
			// 					elementType: "labels.text.fill",
			// 					stylers: [{
			// 						color: "#d59563"
			// 					}],
			// 				},
			// 				{
			// 					featureType: "poi",
			// 					elementType: "labels.text.fill",
			// 					stylers: [{
			// 						color: "#d59563"
			// 					}],
			// 				},
			// 				{
			// 					featureType: "poi.park",
			// 					elementType: "geometry",
			// 					stylers: [{
			// 						color: "#263c3f"
			// 					}],
			// 				},
			// 				{
			// 					featureType: "poi.park",
			// 					elementType: "labels.text.fill",
			// 					stylers: [{
			// 						color: "#6b9a76"
			// 					}],
			// 				},
			// 				{
			// 					featureType: "road",
			// 					elementType: "geometry",
			// 					stylers: [{
			// 						color: "#38414e"
			// 					}],
			// 				},
			// 				{
			// 					featureType: "road",
			// 					elementType: "geometry.stroke",
			// 					stylers: [{
			// 						color: "#212a37"
			// 					}],
			// 				},
			// 				{
			// 					featureType: "road",
			// 					elementType: "labels.text.fill",
			// 					stylers: [{
			// 						color: "#9ca5b3"
			// 					}],
			// 				},
			// 				{
			// 					featureType: "road.highway",
			// 					elementType: "geometry",
			// 					stylers: [{
			// 						color: "#746855"
			// 					}],
			// 				},
			// 				{
			// 					featureType: "road.highway",
			// 					elementType: "geometry.stroke",
			// 					stylers: [{
			// 						color: "#1f2835"
			// 					}],
			// 				},
			// 				{
			// 					featureType: "road.highway",
			// 					elementType: "labels.text.fill",
			// 					stylers: [{
			// 						color: "#f3d19c"
			// 					}],
			// 				},
			// 				{
			// 					featureType: "transit",
			// 					elementType: "geometry",
			// 					stylers: [{
			// 						color: "#2f3948"
			// 					}],
			// 				},
			// 				{
			// 					featureType: "transit.station",
			// 					elementType: "labels.text.fill",
			// 					stylers: [{
			// 						color: "#d59563"
			// 					}],
			// 				},
			// 				{
			// 					featureType: "water",
			// 					elementType: "geometry",
			// 					stylers: [{
			// 						color: "#17263c"
			// 					}],
			// 				},
			// 				{
			// 					featureType: "water",
			// 					elementType: "labels.text.fill",
			// 					stylers: [{
			// 						color: "#515c6d"
			// 					}],
			// 				},
			// 				{
			// 					featureType: "water",
			// 					elementType: "labels.text.stroke",
			// 					stylers: [{
			// 						color: "#17263c"
			// 					}],
			// 				},
			// 			]
			// 		})
			// 	} else {
			// 		this.map.setOptions({
			// 			styles: []
			// 		})
			// 	}
			// }
		},
	};
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
		margin-top: -20px;
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
