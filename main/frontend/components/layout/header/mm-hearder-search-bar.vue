<template>
  <div class="search-bar">
    <input class="search-bar__input" placeholder="Pesquisar assunto" />
  </div>
</template>

<script>
export default {
  name: 'MmHearderSearchBar',
}
</script>

<style scoped>
.search-bar {
  @apply bg-white rounded-sm p-2;
}

.search-bar__input {
  @apply text-secondary font-medium outline-none;
}
</style>
