<template>
  <div class="home__main main">
    <div class="main__subject">
      <mm-carousel
        indicator-type="disc"
        style="height: 100%"
        :data="subjectsImages"
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
  props: {
    subjects: {
      type: Array,
      required: true,
    },
  },
  computed: {
    subjectsImages() {
      return this.subjects.map((subject) => this.makeSubject(subject));
    },
  },
  methods: {
    makeSubject(subject) {
      return `
        <div class="relative">
            <div class="font-medium text-white p-2 absolute text-xl bottom-0 mb-8">
                ${subject.title}
            </div>
            <img alt="capa" class="w-full h-96" src="${subject.image_url}" />
        </div>
      `;
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
