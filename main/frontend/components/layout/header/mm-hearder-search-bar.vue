<template>
  <div class="search-bar">
    <input
      v-model="search"
      class="search-bar__input"
      placeholder="Pesquisar assunto"
      @keyup.enter="redirectToSearchPage"
    />
    <div class="cursor-pointer" @click="redirectToSearchPage">
      <search-icon size="20" />
    </div>
  </div>
</template>

<script>
import { SearchIcon } from "vue-feather-icons";
export default {
  name: "MmHearderSearchBar",
  components: {
    SearchIcon,
  },
  data() {
    return {
      search: "",
    };
  },
  methods: {
    redirectToSearchPage() {
      this.$router.push(
        { path: "/search", query: { search: this.search } },
        () => {
          this.search = "";
        }
      );
    },
  },
};
</script>

<style scoped>
.search-bar {
  @apply text-secondary  flex bg-white rounded-sm p-1 items-center;
}

.search-bar__input {
  @apply font-medium outline-none pl-2;
}
</style>
