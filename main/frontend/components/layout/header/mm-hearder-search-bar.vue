<template>
  <div class="search-bar">
    <input class="search-bar__input" placeholder="Pesquisar assunto" />
    <search-icon size="20" />
  </div>
</template>

<script>
import { SearchIcon } from "vue-feather-icons";
export default {
  name: "MmHearderSearchBar",
  components: {
    SearchIcon,
  },
};
</script>

<style scoped>
.search-bar {
  @apply text-secondary  flex bg-white rounded-sm p-1 items-center;
}

.search-bar__input {
  @apply font-medium outline-none pl-2;
}
</style>
