<template>
  <div v-if="subject" class="subject">
    <mm-details-subject-title :title="subject.hashtag" />
    <div class="subject__chart">
      <v-chart :option="chart" />
    </div>
    <div class="subject__text">
      <mm-subject-text />
    </div>
    <div class="mt-4">
      <div class="font-medium text-lg mb-4"># Tweets</div>
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
export default {
  name: "Id",
  components: {
    MmPaginate,
    MmSubjectText,
    MmDetailsTweetComment,
    MmDetailsSubjectTitle,
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
    };
  },
  computed: {
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
    async getTweets(url = "/tweets") {
      const {
        data: { results: tweets, previous, next },
      } = await this.$axios.get(url, {
        params: {
          search: this.subject.hashtag,
        },
      });

      this.prev = previous;
      this.next = next;
      this.comments = tweets.map((tweet) => ({
        id: tweet.id,
        data: tweet.tweet_date,
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
  @apply w-full flex justify-center items-center h-64 bg-tertiary mt-2 p-4;
}

@screen md {
  .subject {
    @apply px-16 py-8;
  }
}
</style>
