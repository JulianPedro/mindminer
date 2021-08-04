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
  @apply flex-1 p-2;
}

.main__subject {
  @apply py-4 rounded-md;
}

@screen md {
  .home__main {
    @apply py-8 px-8;
  }
}

.main__subject {
  @apply w-full h-64 bg-tertiary;
}

.main__help {
  @apply mt-4;
}
</style>
