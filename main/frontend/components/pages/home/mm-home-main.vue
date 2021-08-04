<template>
  <div class="home__main main">
    <div class="main__subject"></div>
    <div class="main__help">
      <span># Como utilizar</span><br />
      <div>Bolsolula 2022</div>
    </div>
  </div>
</template>

<script>
export default {
  name: "MmHomeMain",
};
</script>

<style scoped>
.home__main {
  @apply flex-1 p-1;
}

@screen md {
  .home__main {
    @apply p-2;
  }
}

.main__subject {
  @apply w-full h-64 bg-gray-500;
}
</style>
