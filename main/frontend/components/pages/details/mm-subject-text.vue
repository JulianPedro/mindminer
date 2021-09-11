<template>
  <div class="subject__content">
    Todos os dados sobre <b>{{ subject.hashtag }}</b> foram obtidos através do
    Twitter e analisados por uma IA que classificou os tweets subjacentes com
    base na versão de treinamento 0.01. É importante levar os dados aqui
    contidos como base de referência e não verdade absoluta, a IA está em fase
    de aprendizagem e pode errar em alguns momentos.
  </div>
</template>

<script>
export default {
  name: "MmSubjectText",
  props: {
    subject: {
      type: Object,
      required: true,
    },
  },
};
</script>

<style scoped>
.subject__content {
  @apply text-secondary text-sm;
}

@screen md {
  .subject__content {
    @apply text-base;
  }
}
</style>
