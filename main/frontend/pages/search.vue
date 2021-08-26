<template>
  <div>
    <div>Sua busca por "{{ search }}" retornou 0 resultados</div>
    <div>
      <vue-table
        :fields="['nome', 'interações', 'Aprovações', 'Rejeições']"
        :data="[]"
      />
    </div>
  </div>
</template>

<script>
import VueTable from "vuetable-2";
export default {
  name: "Search",
  components: {
    VueTable,
  },
  computed: {
    search() {
      return this.$route.query.search;
    },
  },
};
</script>

<style scoped></style>
