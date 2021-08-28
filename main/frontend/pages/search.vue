<template>
  <div class="search">
    <h1 v-if="search">
      Sua busca resultou por {{ search }} restornou {{ count }} resultados
    </h1>
    <table class="w-full">
      <thead>
        <tr class="table__header">
          <th colspan="3">Nome</th>
          <th colspan="1">Interações</th>
          <th colspan="1">Aprovações</th>
          <th colspan="1">Rejeições</th>
        </tr>
      </thead>
      <tbody class="table__body">
        <tr v-for="subject in subjects" :key="`subject_${subject.id}`">
          <td colspan="3">{{ subject.hashtag }}</td>
          <td colspan="1">{{ getTimelineSetInfo(subject, "interactions") }}</td>
          <td class="text-green-500" colspan="1">
            {{ getTimelineSetInfo(subject, "approval_percentage") }}
          </td>
          <td class="text-red-500" colspan="1">
            {{ getTimelineSetInfo(subject, "disapproval_percentage") }}
          </td>
        </tr>
      </tbody>
    </table>

    <div class="paginate__buttons">
      <button
        :disabled="isPrevBtnDisabled"
        class="paginate__button mr-2"
        @click="goToPage(previous)"
      >
        <span>Voltar</span>
      </button>
      <button
        :disabled="isNextBtnDisabled"
        class="paginate__button"
        @click="goToPage(next)"
      >
        <span>Avançar</span>
      </button>
    </div>
  </div>
</template>

<script>
export default {
  name: "Search",
  key(route) {
    return route.fullPath;
  },
  async asyncData({ query, $axios }) {
    const {
      data: { results: subjects, count, previous, next },
    } = await $axios.get(`/subject`, {
      params: {
        search: query.search,
      },
    });

    return {
      subjects,
      count,
      previous,
      next,
    };
  },
  data() {
    return {
      subjects: [],
      count: 0,
      next: "",
      previous: "",
    };
  },
  computed: {
    search() {
      return this.$route.query.search;
    },
    isPrevBtnDisabled() {
      return !this.previous;
    },
    isNextBtnDisabled() {
      return !this.next;
    },
  },
  watchQuery: ["search"],
  methods: {
    getTimelineSetInfo(subject, key) {
      if (subject.timeline_set) {
        return subject.timeline_set[key];
      }

      return " ";
    },
    async goToPage(url) {
      const {
        data: { results: subjects, count, previous, next },
      } = await this.$axios.get(url, {
        params: {
          search: this.$route.query.search,
        },
      });

      this.subjects = subjects;
      this.count = count;
      this.previous = previous;
      this.next = next;
    },
  },
};
</script>

<style scoped>
.search {
  @apply m-10;
}

.table__header {
  @apply bg-tertiary;
}

.table__header > th {
  @apply text-left py-2;
}

.table__body > tr {
  @apply cursor-pointer;
}

.table__body > tr td {
  @apply py-2;
}

.table__body tr:hover {
  @apply bg-tertiary;
}

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
