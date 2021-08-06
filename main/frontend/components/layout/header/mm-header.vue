<template>
  <header class="header">
    <nuxt-link to="/">
      <span class="text-white text-lg font-medium cursor-pointer">
        MindMiner
      </span>
    </nuxt-link>
    <mm-hearder-search-bar />
  </header>
</template>

<script>
import MmHearderSearchBar from "@/components/layout/header/mm-hearder-search-bar";
export default {
  name: "MmHeader",
  components: { MmHearderSearchBar },
};
</script>

<style scoped>
.header {
  @apply py-2 px-6 flex justify-between items-center bg-primary w-full;
}
</style>
