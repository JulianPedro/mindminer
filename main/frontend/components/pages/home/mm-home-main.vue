<template>
  <div class="home__main main">
    <div class="main__subject">
      <mm-carousel
        indicator-type="disc"
        style="height: 100%"
        :data="trendsSubjects"
      />
    </div>
    <div class="main__help help">
      <span class="help__name"> <strong> # Como utilizar </strong> </span><br />
      <div class="help__text">Bolsolula 2022</div>
    </div>
  </div>
</template>

<script>
export default {
  name: "MmHomeMain",
  data() {
    return {
      trendsSubjects: [
        `<img class="w-full" src="https://www.redebrasilatual.com.br/wp-content/uploads/2021/08/lula-lider-pesquisa.jpg" />`,
        `<img class="w-full" src="https://www.novoeste.com/uploads/image/img_brasil247_estados-rejeitam-cloroquina-doada-trump.jpg" />`,
        `<img class="w-full" src="https://revistacult.uol.com.br/home/wp-content/uploads/2021/05/ciro-gomes-foto-jarbas-oliveira.png" />`,
      ],
    };
  },
};
</script>

<style scoped>
.home__main {
  @apply flex-1 p-2;
}

.main__subject {
  @apply py-4 rounded-md overflow-hidden;
}

@screen md {
  .home__main {
    @apply py-8 px-8;
  }
}

.main__subject {
  @apply w-full h-96 bg-tertiary;
}

.main__help {
  @apply mt-10;
}

.help__name {
  @apply text-blue-700;
}

.help__text {
  @apply mt-4;
}
</style>
