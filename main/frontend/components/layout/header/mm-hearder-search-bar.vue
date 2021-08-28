<template>
  <div class="search-bar">
    <input
      v-model="search"
      class="search-bar__input"
      placeholder="Pesquisar assunto"
      @keyup.enter="redirectToSearchPage"
    />
    <div
      v-if="search"
      class="cursor-pointer absolute right-0 top-0 mr-8 mt-2"
      @click="clear"
    >
      <x-icon size="18" />
    </div>
    <div class="cursor-pointer" @click="redirectToSearchPage">
      <search-icon size="20" />
    </div>
  </div>
</template>

<script>
import { SearchIcon, XIcon } from "vue-feather-icons";

export default {
  name: "MmHearderSearchBar",
  components: {
    SearchIcon,
    XIcon,
  },
  data() {
    return {
      search: "",
    };
  },
  mounted() {
    this.search = this.$route.query.search;
  },
  methods: {
    redirectToSearchPage() {
      this.$router.push({ path: "/search", query: { search: this.search } });
    },
    clear() {
      this.search = "";
      this.$router.push({ path: "/search", search: "" });
    },
  },
};
</script>

<style scoped>
.search-bar {
  @apply text-secondary relative flex bg-white rounded-sm p-1 items-center;
}

.search-bar__input {
  @apply font-medium outline-none pl-2;
}
</style>
