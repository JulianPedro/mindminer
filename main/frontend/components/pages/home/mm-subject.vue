<template>
  <div class="subject" @click="openSubject">
    <div class="subject__image">
      <img alt="capa" :src="subject.image_url" />
      <span class="subject__title">{{ subject.title }}</span>
    </div>
    <div class="subject__description">
      {{ subject.description }}
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
      this.$router.push(`/details/${this.subject.id}`);
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

.subject__description {
  @apply text-secondary font-light text-base max-h-16 truncate;
}

.subject__title {
  @apply absolute truncate bottom-0 left-0 text-white text-base font-light ml-2 truncate w-full;
}
</style>
