var ctx = document.getElementById("myChart");
$.getJSON('http://127.0.0.1:5001/data', function(data2) {
    // Setting the data for the chart.
    // Converting data from string to number.
    data2 = data2.slice(1);
    data2 = data2.slice(0, -1);
    data2 = data2.split(',');
    data2 = data2.map(Number);
    data2.pop();


    const myChart = new Chart(ctx, {
        type: 'horizontalBar',
        data: {
            labels: ["Tiempo para foto", "Delta foto-registro datos ", "Delta registro datos-ubicación", "Delta ubicación bodega-tránsito"],
            datasets: [{
                axis: 'x',
                label: 'Minutes',
                data: data2,
                backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                    'rgba(255, 206, 86, 0.2)',
                    'rgba(75, 192, 192, 0.2)',
                    'rgba(153, 102, 255, 0.2)',
                    'rgba(255, 159, 64, 0.2)'
                ],
                borderColor: [
                    'rgba(255,99,132,1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)',
                    'rgba(153, 102, 255, 1)',
                    'rgba(255, 159, 64, 1)'
                ],
                borderWidth: 1
            }]
        },
        options: {
            indexAxis: 'y',
        }
    });
});
