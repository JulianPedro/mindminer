<template>
  <aside class="home_sidebar sidebar">
    <div class="sidebar__title">Mais populares</div>
  </aside>
</template>

<script>
export default {
  name: "MmHomeSidebar",
};
</script>

<style scoped>
.home_sidebar {
  @apply hidden;
}

@screen md {
  .home_sidebar {
    @apply w-64 flex border-l py-8 p-4;
  }

  .sidebar__title {
    @apply font-bold text-lg;
  }
}
</style>
