<template>
  <div class="sort">
    <chevron-up-icon
      class="sort__direction"
      :size="size"
      @click="$emit('up')"
    />
    <chevron-down-icon
      class="sort__direction"
      :size="size"
      @click="$emit('down')"
    />
  </div>
</template>

<script>
import { ChevronDownIcon, ChevronUpIcon } from "vue-feather-icons";
export default {
  name: "MmSort",
  components: { ChevronUpIcon, ChevronDownIcon },
  props: {
    size: {
      required: false,
      type: String,
      default: "12",
    },
  },
};
</script>

<style scoped>
.sort {
  @apply flex flex-col;
}

.sort__direction:hover {
  @apply text-primary cursor-pointer;
}
</style>
