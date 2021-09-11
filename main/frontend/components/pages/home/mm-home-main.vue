<template>
  <div class="home__main main">
    <div class="main__subject">
      <carousel :per-page="1">
        <slide v-for="subject in subjects" :key="`${subject.id}`">
          <div class="cursor-pointer relative">
            <div
              class="font-medium text-white p-2 absolute text-xl bottom-0 mb-8"
              @click="openSubject(subject)"
            >
              {{ subject.title }}
            </div>
            <img alt="capa" class="w-full h-96" :src="subject.image_url" />
          </div>
        </slide>
      </carousel>
    </div>
    <div class="main__help help">
      <span class="help__name"> <strong> # Como utilizar </strong> </span><br />
      <div class="help__text">
        Mindminer é uma plataforma de visualização de dados com viés político
        classificado por uma inteligência artificial. Para utilizar basta
        procurar por um determinado assunto na barra de pesquisa, caso o assunto
        não exista em nossa base de dados, não se preocupe, nosso robô 🤖 irá
        agendar novas buscas pelo mesmo de forma automática.
      </div>
    </div>
  </div>
</template>

<script>
import { Carousel, Slide } from "vue-carousel";
export default {
  name: "MmHomeMain",
  components: {
    Carousel,
    Slide,
  },
  props: {
    subjects: {
      type: Array,
      required: true,
    },
  },
  methods: {
    openSubject(subject) {
      window.open(subject.source_url, "_blank");
    },
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
