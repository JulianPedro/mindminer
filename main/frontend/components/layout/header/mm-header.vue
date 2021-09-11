<template>
  <header class="header">
    <nuxt-link to="/">
      <span class="text-white text-lg font-medium cursor-pointer">
        MindMiner
      </span>
    </nuxt-link>
    <div class="flex items-center justify-center">
      <div
        class="text-white mr-4 font-medium cursor-pointer"
        @click="goToSubjectsPage"
      >
        Explorar
      </div>
      <mm-hearder-search-bar />
    </div>
  </header>
</template>

<script>
import MmHearderSearchBar from "@/components/layout/header/mm-hearder-search-bar";
export default {
  name: "MmHeader",
  components: { MmHearderSearchBar },
  methods: {
    goToSubjectsPage() {
      this.$router.push({ path: "/search" });
    },
  },
};
</script>

<style scoped>
.header {
  @apply py-2 px-6 flex justify-between items-center bg-primary w-full;
}
</style>
