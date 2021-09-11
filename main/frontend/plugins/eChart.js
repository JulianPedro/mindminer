import Vue from "vue";
import VueEcharts from "vue-echarts";
import { use } from "echarts/core";
import { CanvasRenderer } from "echarts/renderers";
import { PieChart } from "echarts/charts";
import {
  TitleComponent,
  TooltipComponent,
  LegendComponent,
} from "echarts/components";

use([CanvasRenderer]);

use([TitleComponent, TooltipComponent, LegendComponent]);

use([PieChart]);

Vue.component("VChart", VueEcharts);
