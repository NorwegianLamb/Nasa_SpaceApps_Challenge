$(document).ready(function() {
    function updateMap(year) {
        $.getJSON(`/data/${year}`, function(data) {
            const countries = data.map(d => d.iso3);
            const giiValues = data.map(d => d[`gii_${year}`]);

            const mapData = [{
                type: 'choropleth',
                colorscale: 'Viridis',
                reversescale: true,
                z: giiValues,
                locations: countries,
                locationmode: 'ISO-3',
                text: data.map(d => `${d.country}: ${d[`gii_${year}`]}`),
                colorbar: {
                    title: 'GII'
                }
            }];

            const layout = {
                title: `Gender Inequality Index in ${year}`,
                geo: {
                    showframe: false,
                    projection: {
                        type: 'mercator'
                    }
                }
            };

            Plotly.newPlot('map', mapData, layout);
        });
    }

    $('#yearSlider').on('input', function() {
        const year = $(this).val();
        $('#yearValue').text(year);
        updateMap(year);
    });

    // Initialize map with the latest year
    updateMap(2018);
});
