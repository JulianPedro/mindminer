<template>
  <aside class="home_sidebar sidebar">
    <div class="sidebar__title">Mais populares <mm-sort /></div>
    <div class="sidebar__subjects">
      <mm-subject
        v-for="subject in subjects"
        :key="subject.id"
        :subject="subject"
      />
    </div>
  </aside>
</template>

<script>
import MmSubject from "@/components/pages/home/mm-subject";
import MmSort from "@/components/global/mm-sort";
export default {
  name: "MmHomeSidebar",
  components: { MmSort, MmSubject },
  props: {
    subjects: {
      required: true,
      type: Array,
    },
  },
};
</script>

<style scoped>
.home_sidebar {
  @apply flex flex-col overflow-auto hidden;
}

.sidebar__subjects > div {
  @apply mt-4;
}

.sidebar__subjects {
  @apply mt-2;
}

.sidebar__title {
  @apply flex justify-between font-medium text-lg;
}

@screen md {
  .home_sidebar {
    @apply w-80 flex border-l py-8 px-10;
  }
}
</style>
