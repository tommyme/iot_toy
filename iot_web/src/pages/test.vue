<template>
  <q-page class="row items-center justify-evenly">
    <div id="main" style="width:500;length:800">

    </div>
  </q-page>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import * as echarts from 'echarts';

var dom = document.getElementById('main');
var option = {
  title: {
    text: 'ECharts 入门示例'
  },
  tooltip: {},
  xAxis: {
    data: ['衬衫', '羊毛衫', '雪纺衫', '裤子', '高跟鞋', '袜子']
  },
  yAxis: {},
  series: [
    {
      name: '销量',
      type: 'bar',
      data: [5, 20, 36, 10, 10, 20]
    }
  ]
}
if (dom) {
  var myChart = echarts.init(dom);
  myChart.setOption(option);
}


export default defineComponent({
  name: 'PageIndex',
  setup() {
    return { 
      lorem: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.'
    };
  }
});
</script>