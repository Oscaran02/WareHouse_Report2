/* globals Chart:false, feather:false */

(function () {
  'use strict'

  feather.replace({ 'aria-hidden': 'true' })

  let ctx = document.getElementById("tiemposProm");
  $.getJSON('/promedios_bodega', function(data2) {
    new Chart(ctx, {
      type: 'bar',
      data: {
        labels: ["Foto", "Registro Datos", "Bodega", "Transito"],
        datasets: [{
          axis: 'x',
          label: 'Tiempo promedio',
          data: data2,
          backgroundColor: 'rgba(255, 99, 132, 0.2)',
          borderColor: 'rgba(255,99,132,1)',
          borderWidth: 2
        }]
      },
      options: {
        elements: {
          bar: {
            borderWidth: 2,
          }
        },
        responsive: true,
        indexAxis: 'y',
        plugins: {
          legend: {
            position: 'right',
          },
        }
      },
    });
  });
})()