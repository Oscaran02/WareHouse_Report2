/* globals Chart:false, feather:false */

(function () {
    'use strict'

    feather.replace({ 'aria-hidden': 'true' })

    let ctx = document.getElementById("graph4");
    $.getJSON('/data4', function(data) {
        // make a pie chart
        // print the keys of the data2
        let keys = Object.keys(data);
        let values = Object.values(data);
        new Chart(ctx, {
            type: 'pie',
            data: {
                labels: keys,
                datasets: [{
                    data: values,
                    backgroundColor: [
                        'rgba(255, 99, 132, 0.2)',
                        'rgba(6,255,0,0.2)',
                    ],
                }]
            },
        });
    });
})()