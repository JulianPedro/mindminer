<template>
  <div>
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
            <div>Quantidade analisada</div>
          </th>
          <th colspan="1">
            <div>Quantidade positivo</div>
          </th>
          <th colspan="1">
            <div>Quantidade Negativa</div>
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
          <td class="text-green-500" colspan="1">
            {{ release.correct_classify_percentage }}
          </td>
          <td class="text-red-500" colspan="1">
            {{ release.epoch }}
          </td>
          <td class="text-red-500" colspan="1">
            {{ release.amount_data }}
          </td>
          <td class="text-red-500" colspan="1">
            {{ release.amount_positive }}
          </td>
          <td class="text-red-500" colspan="1">
            {{ release.amount_negative }}
          </td>
          <td class="text-red-500" colspan="1">
            {{ release.training_date }}
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
    const { data: releases } = await $axios.post(`/about/training`);

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

<style scoped></style>
