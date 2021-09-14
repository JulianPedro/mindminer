<template>
  <div class="m-10">
    <h1 class="text-lg font-bold">Versionamento</h1>
    <table class="w-full mt-4">
      <thead>
        <tr class="table__header">
          <th colspan="1">
            <div>Versão de treinamento</div>
          </th>
          <th colspan="1">
            <div>Precisão do modelo</div>
          </th>
          <th colspan="1">
            <div>Taxa de acerto</div>
          </th>
          <th colspan="1">
            <div>Época</div>
          </th>
          <th colspan="1">
            <div>Qtd. analisada</div>
          </th>
          <th colspan="1">
            <div>Qtd. positivo</div>
          </th>
          <th colspan="1">
            <div>Qtd. negativa</div>
          </th>
          <th colspan="1">
            <div>Data de treinamento</div>
          </th>
        </tr>
      </thead>
      <tbody class="table__body">
        <tr v-for="release in releases" :key="`subject_${release.id}`">
          <td colspan="1">{{ release.training_version }}</td>
          <td colspan="1">{{ release.accuracy }}</td>
          <td colspan="1">
            {{ release.correct_classify_percentage }}
          </td>
          <td colspan="1">
            {{ release.epochs }}
          </td>
          <td colspan="1">
            {{ release.amount_data }}
          </td>
          <td colspan="1">
            {{ release.amount_positive }}
          </td>
          <td colspan="1">
            {{ release.amount_negative }}
          </td>
          <td colspan="1">
            {{ release.training_date | ptDate }}
          </td>
        </tr>
        <tr v-if="!releases.length">
          <td class="text-center" colspan="6">Sem resultados</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  name: "Releases",
  async asyncData({ $axios }) {
    const {
      data: { results: releases },
    } = await $axios.get(`/about/training`);

    return {
      releases,
    };
  },
  data() {
    return {
      releases: [],
    };
  },
};
</script>

<style scoped>
.table__header {
  @apply bg-tertiary;
}

.table__header > th {
  @apply text-left py-2 font-medium;
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
