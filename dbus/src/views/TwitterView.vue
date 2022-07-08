<!-- <template>
	<ContentBase>
		<div id="twitter">
			<frame-options policy="SAMEORIGIN" />
			<iframe :src="txtUrl" frameborder="0" width="100%" :style="{height:calHeight}" scrolling="auto"></iframe>
		</div>

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

</style> -->
<template>
<ContentBase>
	<a
	id="twitter"
    class="twitter-timeline"
    :href="src"></a>
</ContentBase>

</template>

<script>
export default {
  props: {
    src: {
      type: String,
      default: "https://twitter.com/dublinbusnews"
    },
    dark: {
      type: Boolean,
      default: true
    },
    dataLinkColor: {
      type: String,
      default: "#2B7BB9"
    }
  },
  created() {
    let twitterFeed = document.createElement("script");
    twitterFeed.setAttribute("src", "https://platform.twitter.com/widgets.js");
    document.head.appendChild(twitterFeed);
  }
};
</script>
