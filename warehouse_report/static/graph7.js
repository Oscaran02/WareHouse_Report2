/* globals Chart:false, feather:false */

(function () {
    'use strict'

    feather.replace({ 'aria-hidden': 'true' })

    let ctx = document.getElementById("graph7");
    $.getJSON('/data7', function(data) {
        // make a pie chart
        // print the keys of the data2
        let keys = Object.keys(data);
        let values = Object.values(data);
        new Chart(ctx, {
            type: 'bar',
            data: {
                labels: keys,
                datasets: [{
                    axis: 'x',
                    label: 'Número de paquetes',
                    data: values,
                    backgroundColor: 'rgb(0,60,101)',
                    borderColor: 'rgba(54, 162, 235, 1)',
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