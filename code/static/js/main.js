// This script will handle the client-side logic for the website

// Function to generate a chart using Chart.js
function generateChart(chartId, chartType, chartData, chartLabels) {
    var ctx = document.getElementById(chartId).getContext('2d');
    var chart = new Chart(ctx, {
        type: chartType,
        data: {
            labels: chartLabels,
            datasets: [{
                label: 'My First Dataset',
                data: chartData,
                backgroundColor: 'rgba(75, 192, 192, 0.2)',
                borderColor: 'rgba(75, 192, 192, 1)',
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
}

// Function to fetch data from the API and update the chart
function updateChart(chartId, apiUrl) {
    fetch(apiUrl)
        .then(response => response.json())
        .then(data => {
            generateChart(chartId, 'line', data.values, data.labels);
        })
        .catch(error => console.error('Error:', error));
}

// Update the cashflow chart every 5 seconds
setInterval(updateChart, 5000, 'cashflowChart', '/api/cashflow');

// Update the workflow chart every 5 seconds
setInterval(updateChart, 5000, 'workflowChart', '/api/workflow');
