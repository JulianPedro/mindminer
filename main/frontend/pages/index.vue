<template>
  <div class="home">
    <mm-home-main />
    <mm-home-sidebar />
  </div>
</template>

<script>
import MmHomeMain from "~/components/pages/home/mm-home-main";
import MmHomeSidebar from "~/components/pages/home/mm-home-sidebar";
export default {
  name: "Index",
  components: { MmHomeSidebar, MmHomeMain },
};
</script>

<style>
.home {
  @apply flex;
}
</style>
