<template>
  <div v-if="subject" class="subject">
    <mm-details-subject-title :title="subject.hashtag" />
    <div class="subject__chart">
      <v-chart :autoresize="true" :option="chart" />
      Números de tweets:
      {{ totalInteraction }}
      <br />
      Números de tweets positivos: {{ totalApproval }} <br />
      Números de tweets negativos: {{ totalDisapproval }}
    </div>
    <div class="subject__text">
      <mm-subject-text :subject="subject" />
    </div>
    <div class="mt-4">
      <div class="flex justify-between font-medium text-lg mb-4">
        <span># Tweets</span>
        <div class="cursor-pointer">
          <span @click="showDateFilter = !showDateFilter">
            <filter-icon v-if="!showDateFilter" class="text-secondary" />
          </span>
          <vue-date-picker
            v-if="showDateFilter"
            v-model="dateFilter"
            placeholder="Escolha um range de data"
            range
            format="DD/MM/YYYY"
            @change="queryTweets"
            @clear="showDateFilter = false"
          ></vue-date-picker>
        </div>
      </div>
      <mm-details-tweet-comment
        v-for="tweet in comments"
        :key="`tweet_${tweet.id}`"
        :tweet="tweet"
        class="mt-2"
      />
      <mm-paginate
        :prev-page="prev"
        :next-page="next"
        @next="() => getTweets(next)"
        @previous="() => getTweets(prev)"
      />
    </div>
  </div>
</template>

<script>
import MmDetailsSubjectTitle from "@/components/pages/details/mm-details-subject-title";
import MmDetailsTweetComment from "@/components/pages/details/mm-details-tweet-comment";
import MmSubjectText from "@/components/pages/details/mm-subject-text";
import MmPaginate from "@/components/global/mm-paginate";
import { FilterIcon } from "vue-feather-icons";
export default {
  name: "Id",
  components: {
    MmPaginate,
    MmSubjectText,
    MmDetailsTweetComment,
    MmDetailsSubjectTitle,
    FilterIcon,
  },
  async asyncData({ $axios, params }) {
    const { data: subject } = await $axios.get(`/subject/${params.id}`);

    return {
      subject,
    };
  },
  data() {
    return {
      subject: null,
      comments: [],
      prev: null,
      next: null,
      showDateFilter: false,
      dateFilter: null,
    };
  },
  computed: {
    approvalPercentage() {
      return this.subject.timeline_set?.approval_percentage || 0;
    },
    disapprovalPercentage() {
      return this.subject.timeline_set?.disapproval_percentage || 0;
    },
    totalInteraction() {
      return this.subject.timeline_set?.interaction || 0;
    },
    totalApproval() {
      return Math.floor(
        (this.approvalPercentage * this.totalInteraction) / 100
      );
    },
    totalDisapproval() {
      return Math.floor(
        (this.disapprovalPercentage * this.totalInteraction) / 100
      );
    },
    chart() {
      return {
        title: {
          text: "Aprovação/reprovação",
          left: "center",
        },
        tooltip: {
          trigger: "item",
        },
        legend: {
          orient: "vertical",
          left: "left",
          data: ["Aprovação", "Reprovação"],
        },
        series: [
          {
            name: "Total",
            type: "pie",
            radius: "70%",
            label: {
              position: "inner",
              fontSize: 14,
              formatter: "{c}",
            },
            data: [
              {
                value: this.subject.timeline_set?.approval_percentage || 0,
                name: "Aprovação",
                itemStyle: { color: "#4ADE80" },
              },
              {
                value: this.subject.timeline_set?.disapproval_percentage || 0,
                name: "Reprovação",
                itemStyle: { color: "#F87171" },
              },
            ],
            emphasis: {
              itemStyle: {
                shadowBlur: 10,
                shadowOffsetX: 0,
                shadowColor: "rgba(0, 0, 0, 0.5)",
              },
            },
          },
        ],
      };
    },
  },
  mounted() {
    this.getTweets();
  },
  methods: {
    queryTweets(dates) {
      if (!dates[0] && !dates[1]) {
        this.getTweets("/tweets", null, null);
        return;
      }
      const from = this.formatDateToQuery(dates[0]);
      const to = this.formatDateToQuery(dates[1]);
      this.getTweets("/tweets", from, to);
    },
    formatDateToQuery(date) {
      return `${date.getFullYear()}-${date.getMonth()}-${date.getDate()}`;
    },
    async getTweets(url = "/tweets", from = undefined, to = undefined) {
      const {
        data: { results: tweets, previous, next },
      } = await this.$axios.get(url, {
        params: {
          search: this.subject.hashtag,
          from,
          to,
        },
      });

      this.prev = previous;
      this.next = next;
      this.comments = tweets.map((tweet) => ({
        id: tweet.id,
        date: tweet.tweet_date,
        content: tweet.tweet_text,
        analysis_result: tweet.analysis_result,
        url: tweet.tweet_url,
        author: {
          name: tweet.user_name,
          image: tweet.user_photo,
        },
      }));
    },
  },
};
</script>

<style scoped>
.subject {
  @apply p-2;
}

.subject__chart {
  @apply w-full flex flex-col justify-center items-center h-96 bg-tertiary mt-2 p-4 text-secondary text-sm;
}

@screen md {
  .subject {
    @apply px-16 py-8;
  }
}

.subject__text {
  @apply mt-4;
}
</style>
