<template>
  <q-page class="row items-center justify-evenly">
    <q-card class="my-card">
      <q-card-section>
        <div id="myChart" :style="{width: '1300px', height: '900px'}">
          <div id="lchart" :style="{width: '1300px', height: '450px'}"></div>
          <div id="tchart" :style="{width: '1300px', height: '450px'}"></div>
        </div>
      </q-card-section>
    </q-card>
  </q-page>
</template>

<script lang="ts">
// import { Todo, Meta } from 'components/models';
import { defineComponent } from 'vue';
import * as echarts from 'echarts';
import * as _ from 'lodash'
// import axios from 'src/boot/axios';

export default defineComponent({
  name: 'PageIndex',
  // components: { ExampleComponent },
  setup() {
    return { 
      lorem: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.'
    };
  },
  mounted() {
    console.log('mounted');
    var loption = {
      title: {
        text: '光敏传感器数据可视化'
      },
      tooltip: {},
      xAxis: {
        data: [] as string[]
        // data: ['A', 'B', 'C', 'D', 'E']
      },
      yAxis: {},
      series: [
        {
          // data: [200, 88, 98, 73, 79],
          data: [] as number[],
          type: 'line',
          smooth: true
        }
      ]
    }
    var toption = {
      title: {
        text: '热敏传感器数据可视化'
      },
      tooltip: {},
      xAxis: {
        data: [] as string[]
        // data: ['A', 'B', 'C', 'D', 'E']
      },
      yAxis: {},
      series: [
        {
          // data: [200, 88, 98, 73, 79],
          data: [] as number[],
          type: 'line',
          smooth: true
        }
      ]
    }
    var ldom = document.getElementById('lchart')
    var tdom = document.getElementById('tchart')
    if (ldom && tdom){
      var lchart = echarts.init(ldom);
      var tchart = echarts.init(tdom);
      lchart.setOption(loption);
      tchart.setOption(toption);
    }


    var getData = () => {
      fetch('http://localhost/graph_data')
        .then(res => res.json())
        .then(data => {
            // eslint-disable-next-line @typescript-eslint/no-unsafe-member-access
            loption.xAxis.data = _.keys(data['tv']);
            // eslint-disable-next-line @typescript-eslint/no-unsafe-member-access
            toption.xAxis.data = _.keys(data['tv']);

            // eslint-disable-next-line @typescript-eslint/no-unsafe-assignment,@typescript-eslint/no-unsafe-member-access
            loption.series[0].data = _.values(data['lv']);
            // eslint-disable-next-line @typescript-eslint/no-unsafe-assignment,@typescript-eslint/no-unsafe-member-access
            toption.series[0].data = _.values(data['tv']);
          lchart.setOption(loption);
          tchart.setOption(toption);
        })
        .catch(err => {
          console.log(err);
        });
    }        
    getData();
    setInterval(getData, 1000);

  }
});
</script>
