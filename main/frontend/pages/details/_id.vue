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
    </div>
  </div>
</template>

<script>
import MmDetailsSubjectTitle from "@/components/pages/details/mm-details-subject-title";
import MmDetailsTweetComment from "@/components/pages/details/mm-details-tweet-comment";
import MmSubjectText from "@/components/pages/details/mm-subject-text";
export default {
  name: "Id",
  components: { MmSubjectText, MmDetailsTweetComment, MmDetailsSubjectTitle },
  async asyncData({ $axios, params }) {
    const { data: subject } = await $axios.get(`/subject/${params.id}`);

    return {
      subject,
    };
  },
  data() {
    return {
      subject: null,
      comments: [
        {
          id: 0,
          author: {
            name: "teste",
            src: "",
          },
          content:
            "Lorem ipsum facilisis sociosqu vestibulum posuere sed metus mi inceptos mauris, aptent lorem rutrum ante volutpat fusce condimentum porttitor tellus, integer vitae consequat primis suspendisse tellus sagittis curabitur vel. curabitur morbi lacinia augue dui dolor, fusce pharetra hac. vitae adipiscing quis egestas blandit class nostra sociosqu inceptos, venenatis habitasse consequat laoreet lorem viverra nec cursus scelerisque, turpis sollicitudin aenean cursus dapibus aenean erat. sit urna ultricies ut leo nibh sem justo hendrerit mi libero interdum convallis, luctus erat nisl cras eu augue quisque pretium donec tellus. lacus integer ipsum torquent metus vulputate orci curae ut, hendrerit nostra auctor aliquam scelerisque volutpat vestibulum eleifend odio, quisque molestie donec turpis vulputate proin morbi.",
          is_positive: false,
          date: "2021-10-10",
        },
        {
          id: 1,
          author: {
            name: "teste",
            src: "",
          },
          content:
            "Lorem ipsum facilisis sociosqu vestibulum posuere sed metus mi inceptos mauris, aptent lorem rutrum ante volutpat fusce condimentum porttitor tellus, integer vitae consequat primis suspendisse tellus sagittis curabitur vel. curabitur morbi lacinia augue dui dolor, fusce pharetra hac. vitae adipiscing quis egestas blandit class nostra sociosqu inceptos, venenatis habitasse consequat laoreet lorem viverra nec cursus scelerisque, turpis sollicitudin aenean cursus dapibus aenean erat. sit urna ultricies ut leo nibh sem justo hendrerit mi libero interdum convallis, luctus erat nisl cras eu augue quisque pretium donec tellus. lacus integer ipsum torquent metus vulputate orci curae ut, hendrerit nostra auctor aliquam scelerisque volutpat vestibulum eleifend odio, quisque molestie donec turpis vulputate proin morbi.",
          is_positive: false,
          date: "2021-10-10",
        },
      ],
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
        },
        series: [
          {
            name: "访问来源",
            type: "pie",
            radius: "50%",
            data: [
              {
                value: 1048,
                name: "Aprovação",
                itemStyle: { color: "#4ADE80" },
              },
              {
                value: 735,
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
};
</script>

<style scoped>
.subject {
  @apply p-2;
}

.subject__chart {
  @apply w-full h-64 bg-tertiary mt-2;
}

@screen md {
  .subject {
    @apply px-16 py-8;
  }
}
</style>
