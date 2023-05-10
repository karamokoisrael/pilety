// // Get the monthly expenses by category as a dictionary
// var expenses = JSON.parse(document.getElementById('expenses-data').textContent);

// // Render the pie chart
// var ctx1 = document.getElementById('pieChart').getContext('2d');
// var pieChart = new Chart(ctx1, {
//     type: 'pie',
//     data: {
//         labels: Object.keys(expenses),
//         datasets: [{
//             data: Object.values(expenses),
//             backgroundColor: [
//                 '#FF6384',
//                 '#36A2EB',
//                 '#FFCE56',
//                 '#E7E9ED',
//                 '#4BC0C0',
//                 '#9966FF'
//             ],
//             hoverBackgroundColor: [
//                 '#FF6384',
//                 '#36A2EB',
//                 '#FFCE56',
//                 '#E7E9ED',
//                 '#4BC0C0',
//                 '#9966FF'
//             ]
//         }]
//     },
//     options: {
//         title: {
//             display: true,
//             text: 'Monthly Expenses by Category'
//         }
//     }
// });

// // Render the line graph
// var ctx2 = document.getElementById('lineGraph').getContext('2d');
// var lineGraph = new Chart(ctx2, {
//     type: 'line',
//     data: {
//         labels: Object.keys(expenses['Total']),
//         datasets: Object.keys(expenses).map(function(key, index) {
//             return {
//                 label: key,
//                 data: Object.values(expenses[key]),
//                 fill: false,
//                 borderColor: [
//                     '#FF6384',
//                     '#36A2EB',
//                     '#FFCE56',
//                     '#E7E9ED',
//                     '#4BC0C0',
//                     '#9966FF'
//                 ][index % 6]
//             };
//         })
//     },
//     options: {
//         title: {
//             display: true,
//             text: 'Monthly Expenses by Category'
//         },
//         scales: {
//             yAxes: [{
//                 ticks: {
//                     beginAtZero: true
//                 }
//             }]
//         }
//     }
// });


// Pie chart
var ctx = document.getElementById('category-chart').getContext('2d');
var categoryChart = new Chart(ctx, {
    type: 'pie',
    data: {
        labels: categories,
        datasets: [{
            label: 'Expenses by Category',
            data: category_totals,
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)'
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
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
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true
                }
            }]
        }
    }
});

// Bar chart
var ctx = document.getElementById('month-chart').getContext('2d');
var monthChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: months,
        datasets: [{
            label: 'Expenses by Month',
            data: month_totals,
            backgroundColor: 'rgba(54, 162, 235, 0.2)',
            borderColor: 'rgba(54, 162, 235, 1)',
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true
                }
            }]
        }
    }
});
