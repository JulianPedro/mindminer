<template>
  <div class="layout">
    <mm-header />
    <div class="layout__page page">
      <div class="page__content">
        <Nuxt />
      </div>
    </div>
  </div>
</template>

<script>
import MmHeader from "@/components/layout/header/mm-header";
export default {
  components: { MmHeader },
};
</script>

<style>
html {
  font-family: "Source Sans Pro", -apple-system, BlinkMacSystemFont, "Segoe UI",
    Roboto, "Helvetica Neue", Arial, sans-serif;
  font-size: 16px;
  word-spacing: 1px;
  -ms-text-size-adjust: 100%;
  -webkit-text-size-adjust: 100%;
  -moz-osx-font-smoothing: grayscale;
  -webkit-font-smoothing: antialiased;
  box-sizing: border-box;
}

:hover::-webkit-scrollbar-thumb {
  @apply bg-primary;
}

/* width */
::-webkit-scrollbar {
  width: 5px;
  height: 5px;
  border-radius: 5px;
}

/* Track */
::-webkit-scrollbar-track {
  border-radius: 5px;
}

/* Handle */
::-webkit-scrollbar-thumb {
  background: #eee;
  border-radius: 5px;
}

/* Handle on hover */
::-webkit-scrollbar-thumb:hover {
  @apply bg-secondary;
}
</style>
<style scoped>
.layout {
  @apply flex flex-col bg-tertiary h-screen;
}

.layout__page {
  @apply flex flex-col min-h-0 flex-1 p-2;

  @screen md {
    @apply px-6 py-4;
  }
}

.page__content {
  @apply flex flex-col h-full w-full overflow-auto bg-white rounded-sm shadow;
}
</style>
