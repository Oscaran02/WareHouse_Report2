
(function () {
    'use strict'

    feather.replace({ 'aria-hidden': 'true' })

    let ctx = document.getElementById("graph10");
    $.getJSON('/data10', function(data) {
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
                    label: 'Tiempo promedio (días)',
                    data: values,
                    backgroundColor: 'rgba(235,184,54,0.2)',
                    borderColor: 'rgb(235,184,54,1)',
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