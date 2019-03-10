<template>
  <vue-plotly :data="data" :layout="layout" :options="options"/>
</template>


<script>
import VuePlotly from '@statnett/vue-plotly'

export default {
  components: {
    VuePlotly
  },
  data: function () {
    return {
      data: [{
        x: [1, 2, 3, 4],
        y: [10, 11, 12, 13],
        mode: 'markers',
        marker: {
          size: [40, 60, 80, 100]
        }
      }],
      layout: {title: 'Marker Size', showlegend: false, height: 600, width: 1200},
      options: {}
    }
  }
}
</script>