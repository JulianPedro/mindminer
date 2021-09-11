<template>
  <div class="search">
    <h1 v-if="search" class="font-medium">
      Sua busca resultou por "{{ search }}" restornou {{ count }} resultados
    </h1>
    <table class="w-full mt-4">
      <thead>
        <tr class="table__header">
          <th colspan="3">
            <div>
              Nome
              <mm-sort
                class="ml-1"
                @up="goToPage(`/subject`, 'hashtag')"
                @down="goToPage(`/subject`, '-hashtag')"
              />
            </div>
          </th>
          <th colspan="1">
            <div>
              Interações
              <mm-sort
                class="ml-1"
                @up="goToPage(`/subject`, 'popularity')"
                @down="goToPage(`/subject`, '-popularity')"
              />
            </div>
          </th>
          <th colspan="1">
            <div>
              Aprovações
              <mm-sort
                class="ml-1"
                @up="goToPage(`/subject`, 'approval_percentage')"
                @down="goToPage(`/subject`, '-approval_percentage')"
              />
            </div>
          </th>
          <th colspan="1">
            <div>
              Rejeições
              <mm-sort
                class="ml-1"
                @up="goToPage(`/subject`, 'disapproval_percentage')"
                @down="goToPage(`/subject`, '-disapproval_percentage')"
              />
            </div>
          </th>
        </tr>
      </thead>
      <tbody class="table__body">
        <tr
          v-for="subject in subjects"
          :key="`subject_${subject.id}`"
          @click="openSubject(subject)"
        >
          <td colspan="3">{{ subject.hashtag }}</td>
          <td colspan="1">{{ getTimelineSetInfo(subject, "interaction") }}</td>
          <td class="text-green-500" colspan="1">
            {{ getTimelineSetInfo(subject, "approval_percentage") }}
          </td>
          <td class="text-red-500" colspan="1">
            {{ getTimelineSetInfo(subject, "disapproval_percentage") }}
          </td>
        </tr>
        <tr v-if="!subjects.length">
          <td class="text-center" colspan="6">Sem resultados</td>
        </tr>
      </tbody>
    </table>

    <mm-paginate
      :prev-page="previous"
      :next-page="next"
      @next="() => goToPage(next)"
      @previous="() => goToPage(previous)"
    />
  </div>
</template>

<script>
import MmSort from "@/components/global/mm-sort";
import MmPaginate from "@/components/global/mm-paginate";
export default {
  name: "Search",
  key(route) {
    return route.fullPath;
  },
  components: { MmPaginate, MmSort },
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
  },
  watchQuery: ["search"],
  methods: {
    getTimelineSetInfo(subject, key) {
      if (subject.timeline_set) {
        return subject.timeline_set[key];
      }

      return " ";
    },
    async goToPage(url, ordering = undefined) {
      const {
        data: { results: subjects, count, previous, next },
      } = await this.$axios.get(url, {
        params: {
          search: this.$route.query.search,
          ordering,
        },
      });

      this.subjects = subjects;
      this.count = count;
      this.previous = previous;
      this.next = next;
    },
    openSubject(subject) {
      this.$router.push({ path: `/details/${subject.id}` });
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

.table__header > th > div {
  @apply flex items-center;
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
</style>
