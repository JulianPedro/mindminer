import Vue from "vue";
import moment from "moment";

Vue.filter("ptDate", (val) => {
  if (!val) return "";

  return moment(val).format("DD/MM/YYYY hh:mm:ss");
});
