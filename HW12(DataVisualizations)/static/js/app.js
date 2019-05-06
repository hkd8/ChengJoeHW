function buildMetadata(sample) {

  // @TODO: Complete the following function that builds the metadata panel

  // Use `d3.json` to fetch the metadata for a sample
    // Use d3 to select the panel with id of `#sample-metadata`
    var selectMeta = d3.select("#sample-metadata");

    // get the jsonified data
    d3.json(`/metadata/${sample}`).then(function(data) {

      // Use `.html("") to clear any existing metadata
      selectMeta.html("")

      // Use `Object.entries` to add each key and value pair to the panel
      var metaData = Object.entries(data)
      metaData.forEach((data) => {
        console.log(data);
      
        // Display each key/value pair from the metadata JSON object somewhere on the page
        selectMeta
        .append('span')
        .text(`${data[0]}: ${data[1]}`)
        .append('br')
      });
      
      //print data
      // console.log(data);
      // console.log(data.sample);
      // console.log(data.ETHNICITY);
      // console.log(data.GENDER);
      // console.log(data.AGE);
      // console.log(data.LOCATION);
      // console.log(data.BBTYPE);
      // console.log(data.WFREQ);
      // console.log(Object.entries(data))

      //Optional buildGauge
      buildGauge(data.WFREQ);
    });

}

function buildCharts(sample) {

  // Select the ids using d3 to display the charts
  var selectPie = d3.select("#pie");
  var selectBubble = d3.select("#bubble");

  // @TODO: Use `d3.json` to fetch the sample data for the plots
  d3.json(`/samples/${sample}`).then((sample) => {
        
        // bubble chart
        var trace1 = {
          x: sample.otu_ids,
          y: sample.sample_values,
          text: sample.otu_labels,
          mode: 'markers',
          marker: {
            size: sample.sample_values,
            color: sample.otu_ids,
            colorscale: "Earth"
          }
        };
        
        var data = [trace1];
        
        var layout = {
          showlegend: false,
        };
        
        Plotly.newPlot('bubble', data, layout);
    
    // pie chart
    // sort sample_values in descending order
    var sample1 = sample.sample_values.sort(function compareFunction(firstNum, secondNum) {
     return secondNum - firstNum;
   });
    
    // use slice to display 10 value_samples
    var sliceSamples = sample1.slice(0, 10)

    var trace = {
      labels: sample.otu_ids,
      hovertext: sample.otu_labels,
      values: sliceSamples,
      type: 'pie'
  }

    var data = [trace];
    var layout = { margin: { t: 30, b: 100 } };
    Plotly.plot('pie', data, layout);

    // Recreate/refresh chart (needs to be done otherwise selecting a different sample will convelute the chart)
    Plotly.restyle('pie', "labels", [sample.otu_ids]);
    Plotly.restyle('pie', "hovertext", [sample.otu_labels]);
    Plotly.restyle('pie', "values", [sliceSamples]);
    //-----------------//

    // print data
      console.log(sample);
      console.log(sample.otu_ids);
      console.log(sample.otu_labels);
      console.log(sample.sample_values);
  });

}

function init() {
  // Grab a reference to the dropdown select element
  var selector = d3.select("#selDataset");

  // Use the list of sample names to populate the select options
  d3.json("/names").then((sampleNames) => {
    sampleNames.forEach((sample) => {
      selector
        .append("option")
        .text(sample)
        .property("value", sample);
        console.log(sample)
    });

    // Use the first sample from the list to build the initial plots
    const firstSample = sampleNames[0];
    buildCharts(firstSample);
    buildMetadata(firstSample);
  });
}

function optionChanged(newSample) {
  // Fetch new data each time a new sample is selected
  buildCharts(newSample);
  buildMetadata(newSample);
}

// Initialize the dashboard
init();
