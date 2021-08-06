<template>
  <div class="subject">
    <div class="subject__image">
      <img :src="subject.image" />
      <span class="subject__title">{{ subject.name }}</span>
    </div>
    <div class="subject__summary">
      {{ subject.summary }}
    </div>
  </div>
</template>

<script>
export default {
  name: "MmSubject",
  data() {
    return {
      subject: {
        name: "Teste nome do assunto assunto 2 ahahsjas",
        summary:
          "Teste nome do assunto assunto 2 ahahsjas sjahsjhajs bsjabsjab shajhsj",
        image:
          "https://www.redebrasilatual.com.br/wp-content/uploads/2021/08/lula-lider-pesquisa.jpg",
      },
    };
  },
};
</script>

<style scoped>
.subject {
  @apply flex flex-col relative cursor-pointer;
}

.subject__image {
  @apply relative;
}

.subject__image > img {
  @apply rounded-tl rounded-tr shadow w-full h-24 object-cover;
}

.subject__summary {
  @apply text-secondary font-light text-base max-h-16;
}

.subject__title {
  @apply absolute bottom-0 left-0 text-white text-base font-light ml-2 truncate w-full;
}
</style>
