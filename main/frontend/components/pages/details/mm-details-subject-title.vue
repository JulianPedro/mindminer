<template>
  <div class="subject__title"># {{ title }}</div>
</template>

<script>
export default {
  name: "DetailsSubjectTitle",
  props: {
    title: {
      required: true,
      type: String,
    },
  },
};
</script>

<style scoped>
.subject__title {
  @apply text-lg text-primary font-medium;
}

@screen md {
  .subject__title {
    @apply text-xl;
  }
}
</style>
