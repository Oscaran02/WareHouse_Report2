/* globals Chart:false, feather:false */

(function () {
    'use strict'

    feather.replace({ 'aria-hidden': 'true' })

    let ctx = document.getElementById("graph6");
    $.getJSON('/data6', function(data) {
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
                        'rgb(255,0,54)',
                        'rgb(0,26,255)',
                        'rgb(255,183,0)',
                    ],
                }]
            },
        });
    });
})()