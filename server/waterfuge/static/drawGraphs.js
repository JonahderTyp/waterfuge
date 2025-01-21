const clients = ['1', '2', '3', '4'];  // Using "1", "2", etc. as client IDs

// Function to create or update a Plotly chart for each client with dual Y axes
function updatePlotlyChart(clientId, timestamps, rpmData, flowData) {
    const chartData = [
        {
            x: timestamps,
            y: rpmData,
            mode: 'lines',
            name: 'RPM',
            line: { color: 'rgb(0, 128, 255)' },
            yaxis: 'y1'  // Left Y axis for RPM
        },
        {
            x: timestamps,
            y: flowData,
            mode: 'lines',
            name: 'Flow',
            line: { color: 'rgb(255, 99, 71)' },
            yaxis: 'y2'  // Right Y axis for Flow
        }
    ];

    const layout = {
        margin: { t: 0 },
        xaxis: {
            title: 'Time',
            type: 'date',
        },
        yaxis: {
            title: 'RPM',
            showgrid: true,
            zeroline: true,
            side: 'left'
        },
        yaxis2: {
            title: 'Flow',
            showgrid: false,
            zeroline: false,
            overlaying: 'y',
            side: 'right'
        },
        legend: {
            x: 1,
            xanchor: 'right',
            y: 1
        }
    };

    Plotly.react(`${clientId}-chart`, chartData, layout);
}


// Function to fetch data from the API and update the charts
function fetchData() {
    clients.forEach(clientId => {
        fetch(`/data/${clientId}`)
            .then(response => response.json())
            .then(data => {
                if (data.length > 0) {
                    const timestamps = data.map(entry => new Date(entry.timestamp * 1000));
                    const rpmData = data.map(entry => entry.rpm);
                    const flowData = data.map(entry => entry.flow);
                    const latestData = data[data.length - 1];

                    // Update the current value display
                    document.getElementById(`${clientId}-current-rpm`).textContent = `${Number(latestData.rpm).toFixed(0)} u/min`;
                    document.getElementById(`${clientId}-current-flow`).textContent = `${Number(latestData.flow).toFixed(0)} l/min`;

                    // Update the Plotly chart with new data
                    updatePlotlyChart(clientId, timestamps, rpmData, flowData);
                }
            })
            .catch(error => console.error('Error fetching data:', error));
    });
}

setInterval(fetchData, 500);

// Initial fetch to load data when the page first loads
fetchData();