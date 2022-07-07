<template>
  <a
    class="twitter-timeline"
    :href="src"
    :data-theme="dark ? 'dark' : 'light'"
    :data-link-color="dataLinkColor"
  ></a>
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