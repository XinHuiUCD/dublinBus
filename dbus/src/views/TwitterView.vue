<template>
<ContentBase>
  <h2 style="text-align:center">
            <span style="color: black">View the latest tweets from</span>&nbsp;
            <span style="color: gray">Dublin Bus</span>
        </h2>
  <div style= "margin:20px auto; width: 50%; height: 700px; overflow: auto; box-shadow: 4px 4px 5px;">
    <a  
    id="twitter"
      class="twitter-timeline"
      :href="src"></a>
  </div>
</ContentBase>

</template>

<script>
import ContentBase from '../components/ContentBase.vue'

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
  components: {
        ContentBase,
    },
  created() {
    let twitterFeed = document.createElement("script");
    twitterFeed.setAttribute("src", "https://platform.twitter.com/widgets.js");
    document.head.appendChild(twitterFeed);
  }
};
</script>

<style scoped>

@import url('https://fonts.googleapis.com/css2?family=Roboto&display=swap');

h2{
  font-family: 'Roboto', sans-serif;

}
</style>