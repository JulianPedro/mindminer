<template>
  <div class="subject" v-on="$listeners" @click="openSubject">
    <div class="subject__image">
      <img alt="capa" :src="subject.image_url" />
    </div>
    <div class="subject__title">
      {{ subject.title }}
    </div>
  </div>
</template>

<script>
export default {
  name: "MmSubject",
  props: {
    subject: {
      type: Object,
      required: true,
    },
  },
  methods: {
    openSubject() {
      window.open(this.subject.source_url, "_blank");
    },
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

.subject__title {
  @apply text-secondary text-base font-light ml-2 w-full;
}
</style>
