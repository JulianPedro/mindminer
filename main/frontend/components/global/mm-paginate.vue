<template>
  <div class="paginate__buttons">
    <button
      :disabled="!prevPage"
      class="paginate__button mr-2"
      @click="$emit('previous')"
    >
      <span>Voltar</span>
    </button>
    <button
      :disabled="!nextPage"
      class="paginate__button"
      @click="$emit('next')"
    >
      <span>Avançar</span>
    </button>
  </div>
</template>

<script>
export default {
  name: "MmPaginate",
  props: {
    prevPage: {
      type: [String, null],
      required: false,
      default: null,
    },
    nextPage: {
      type: [String, null],
      required: false,
      default: null,
    },
  },
};
</script>

<style scoped>
.paginate__buttons {
  @apply mt-6 flex justify-end;
}

.paginate__button {
  @apply flex items-center justify-center p-2 bg-tertiary font-medium rounded-sm;
}

.paginate__button:disabled {
  @apply cursor-not-allowed;
}

.paginate__button:not(:disabled):hover {
  @apply bg-primary text-white;
}
</style>
