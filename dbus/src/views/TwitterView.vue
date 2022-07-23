<template>
<ContentBase>
  <h2 style="text-align:center">
            <span style="color: black">View up to date tweets from</span>&nbsp;
            <span style="color: gray">Dublin Bus</span>
        </h2>
  <div style= "margin:20px auto; width: 50%; height: 700px; overflow: auto;">
    <a  
    id="twitter"
      class="twitter-timeline"
      :href="src"></a>
  </div>
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