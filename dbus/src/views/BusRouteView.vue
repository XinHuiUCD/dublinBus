<template>
	<ContentBase>
		<RouteDisplay />
	</ContentBase>
</template>

<script lang="ts">
	import ContentBase from '../components/ContentBase.vue'
	import RouteDisplay from '../components/RouteDisplay.vue'

	export default {
		name: "BusRouteView",
		components: {
			ContentBase,
			RouteDisplay,
		}
	}
</script>

<style scoped>
</style>
