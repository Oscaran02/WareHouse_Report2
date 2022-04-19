/* globals Chart:false, feather:false */

(function () {
    'use strict'

    feather.replace({ 'aria-hidden': 'true' })

    let ctx = document.getElementById("graph3");
    $.getJSON('/data3', function(data) {
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
                    backgroundColor: 'rgba(33,121,27,0.2)',
                    borderColor: 'rgba(6,255,0,0.56)',
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
                indexAxis: 'x',
                plugins: {
                    legend: {
                        position: 'right',
                    },
                }
            },
        });
    });
})()