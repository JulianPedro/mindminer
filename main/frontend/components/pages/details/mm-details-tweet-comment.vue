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
        <span v-if="tweet.analysis_result === 'Negativo'">(👎)</span>
        <span v-if="tweet.analysis_result === 'Positivo'">(👍)</span>
      </div>
      <div class="header__details details">
        <div></div>
        <div class="details__date">
          {{ tweet.date | ptDate }}
        </div>
      </div>
    </div>
    <div class="tweet__body">
      {{ tweet.content }}
    </div>
  </div>
</template>

<script>
import { UserIcon } from "vue-feather-icons";
export default {
  name: "MmDetailsTweetComment",
  components: {
    UserIcon,
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
  @apply flex-1 ml-4 items-center font-medium;
}

.header__avatar {
  @apply flex justify-center items-center h-8 w-8 rounded-full;

  background-color: #c4c4c4;
}

.tweet__body {
  @apply ml-12 text-secondary text-sm;
}
</style>
