<template>
  <div class="subject__title"># Este é um assunto de teste</div>
</template>

<script>
export default {
  name: "DetailsSubjectTitle",
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
