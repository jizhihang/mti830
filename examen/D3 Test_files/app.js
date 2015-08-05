nv.addGraph(function() {
  var width = nv.utils.windowSize().width,
      height = nv.utils.windowSize().height;

  $('#chart').height(height);

  chart = nv.models.multiBarChart();

  var allData = [  {   key: "Federal",
                    values: federalGovData 
                },
                {
                    key: "Provincial",
                    values: provincialGovData
                },
                {
                    key: "Consolidated",
                    values: consolidatedGovData
                },
                {
                    key: "Local",
                    values: localGovData
                },
                {
                    key: "Pensions",
                    values: pensionsGovData
                }

  ];

  var exclude = ['key', 'series', 'Ref_Date'];
  allChartVars = [];

  for(key in federalGovData[0]) {
    if(!(key in exclude)) {
      allChartVars.push(key);
    }
  }



  // Enables the Grouped vs Stacked controls.
  chart.showControls(true);
  // Rotate labels
  chart.rotateLabels(45);
  // Custom function to have the X axis as the reference date (quarters for each year)
  chart.x(function(d) { return d.Ref_Date; });
  // Custom function to have the Y axis as whatever value we choose
  chart.y(function(d) { return d["Net financial worth (x 1 000 000)"]; });

  // Format the y-Axis data (ten thousand will be "10,000" instead of 10000.0)
  chart.yAxis.tickFormat(d3.format(','));


  d3.select('#chart svg')
      .datum(allData)
      .transition().duration(500)
      .call(chart);


  nv.utils.windowResize(chart.update);

  return chart;
});