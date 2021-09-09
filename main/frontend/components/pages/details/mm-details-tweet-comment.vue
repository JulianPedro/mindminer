<template>
  <div class="tweet">
    <div class="tweet__header header">
      <div class="header__avatar">
        <div v-if="!tweet.author.image">
          <user-icon size="18" />
        </div>
        <img v-else class="rounded-full w-8 h-8" :src="tweet.author.image" />
      </div>
      <div class="header__name">
        <span>
          <a :href="tweet.url" target="_blank">{{ tweet.author.name }}</a>
        </span>
        <div class="flex flex-1 justify-end items-center">
          <div
            v-if="tweet.analysis_result === 'Positivo'"
            class="rate-flag bg-green-400"
          >
            <check-icon size="16" />
          </div>
          <div
            v-if="tweet.analysis_result === 'Negativo'"
            class="rate-flag bg-red-400"
          >
            <x-icon size="16" />
          </div>
          <div class="details__date">
            {{ tweet.date | ptDate }}
          </div>
        </div>
      </div>
    </div>
    <div class="tweet__body">
      {{ tweet.content }}
    </div>
  </div>
</template>

<script>
import { UserIcon, CheckIcon, XIcon } from "vue-feather-icons";
export default {
  name: "MmDetailsTweetComment",
  components: {
    UserIcon,
    CheckIcon,
    XIcon,
  },
  props: {
    tweet: {
      required: true,
      type: Object,
    },
  },
};
</script>

<style scoped>
.tweet__header {
  @apply flex;
}

.header__name {
  @apply flex flex-1 ml-4 items-center font-medium;
}

.header__avatar {
  @apply flex justify-center items-center h-8 w-8 rounded-full;

  background-color: #c4c4c4;
}

.tweet__body {
  @apply ml-12 text-secondary text-sm;
}

.rate-flag {
  @apply mr-2 w-8 h-8 rounded-full flex items-center justify-center text-white;
}

.details__date {
  @apply text-secondary text-sm;
}
</style>
