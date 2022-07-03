<template>
	<ContentBase>
		<frame-options policy="SAMEORIGIN" />
		<iframe :src="this.txtUrl" frameborder="0" width="100%" :style="{height:calHeight}" scrolling="auto"></iframe>
	</ContentBase>
</template>

<script lang="ts">
	import ContentBase from '../components/ContentBase.vue'

	export default {
		name: "TwitterView",
		components: {
			ContentBase,
		},
		data() {
			return {
				txtUrl: "https://twitter.com/dublinbusnews?ref_src=twsrc%5Etfw",
			}
		},

		computed: {
			//Calculate the property and set the iframe height to 100px less than the window height
			calHeight() {
				return (window.innerHeight - 100) + 'px';
			}
		},
	}
</script>

<style scoped>
</style>
