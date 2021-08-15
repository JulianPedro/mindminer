<template>
  <div class="subject__content">
    {{ text }}
  </div>
</template>

<script>
export default {
  name: "MmSubjectText",
  data() {
    return {
      text: `Lorem ipsum facilisis sociosqu vestibulum posuere sed metus mi inceptos mauris, aptent lorem rutrum ante volutpat fusce condimentum porttitor tellus, integer vitae consequat primis suspendisse tellus sagittis curabitur vel. curabitur morbi lacinia augue dui dolor, fusce pharetra hac. vitae adipiscing quis egestas blandit class nostra sociosqu inceptos, venenatis habitasse consequat laoreet lorem viverra nec cursus scelerisque, turpis sollicitudin aenean cursus dapibus aenean erat. sit urna ultricies ut leo nibh sem justo hendrerit mi libero interdum convallis, luctus erat nisl cras eu augue quisque pretium donec tellus. lacus integer ipsum torquent metus vulputate orci curae ut, hendrerit nostra auctor aliquam scelerisque volutpat vestibulum eleifend odio, quisque molestie donec turpis vulputate proin morbi.
`,
    };
  },
};
</script>

<style scoped>
.subject__content {
  @apply text-secondary text-sm;
}

@screen md {
  .subject__content {
    @apply text-base;
  }
}
</style>
