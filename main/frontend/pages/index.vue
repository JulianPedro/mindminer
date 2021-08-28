<template>
  <div class="home">
    <mm-home-main :subjects="top3" />
    <mm-home-sidebar :subjects="others" />
  </div>
</template>

<script>
import MmHomeMain from "~/components/pages/home/mm-home-main";
import MmHomeSidebar from "~/components/pages/home/mm-home-sidebar";
export default {
  name: "Index",
  components: { MmHomeSidebar, MmHomeMain },
  async asyncData({ $axios }) {
    const { data } = await $axios.get("/news");
    const top3 = data.results.slice(0, 3);
    const others = data.results.slice(3);

    return {
      top3,
      others,
    };
  },
  data() {
    return {
      top3: [],
      others: [],
    };
  },
};
</script>

<style>
.home {
  @apply flex h-full;
}
</style>
