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
  var allChartVars = [];

  var sel = $('#chartVar');
  for(key in federalGovData[0]) {
    if($.inArray(key, exclude) == -1)
      sel.append($("<option>").attr('value',key).text(key));
  }

  sel.change(function() {
    chart.y(function(d) { return d[sel.val()]; });
    chart.update();
    $('#varname').html(sel.val());
  });



  // Enables the Grouped vs Stacked controls.
  chart.showControls(true);
  // Rotate labels
  chart.rotateLabels(45);
  // Custom function to have the X axis as the reference date (quarters for each year)
  chart.x(function(d, i) { return d.Ref_Date; });
  // Custom function to have the Y axis as whatever value we choose
  chart.y(function(d, i) { return d["Net financial worth (x 1 000 000)"]; });

  // Format the y-Axis data (ten thousand will be "10,000" instead of 10000.0)
  chart.yAxis.tickFormat(d3.format(','));


  svg = d3.select('#chart svg');

  //prog-con MAJ
  topkek = svg.append("rect")
            .attr("y", 0)
            .attr("x", 60)
            .attr("width", 150)
            .attr("height", 700)
            .attr("fill", "rgba(0,255,255, 0.2")
            .attr("class", "legendBar");

  svg.append("rect")
            .attr("y", 0)
            .attr("x", 210)
            .attr("width", 525)
            .attr("height", 700)
            .attr("fill", "rgba(255,0,0, 0.2")
            .attr("class", "legendBar");

  svg.append("rect")
            .attr("y", 0)
            .attr("x", 735)
            .attr("width", 75)
            .attr("height", 700)
            .attr("fill", "rgba(255,0,0, 0.1")
            .attr("class", "legendBar");

  svg.append("rect")
            .attr("y", 0)
            .attr("x", 810)
            .attr("width", 275)
            .attr("height", 700)
            .attr("fill", "rgba(0,0,255, 0.1")
            .attr("class", "legendBar");

  svg.append("rect")
            .attr("y", 0)
            .attr("x", 1085)
            .attr("width", 200)
            .attr("height", 700)
            .attr("fill", "rgba(0,0,255, 0.2")
            .attr("class", "legendBar");

  svg.datum(allData)
      .transition().duration(500)
      .call(chart);


  nv.utils.windowResize(chart.update);

  sel.val("Net financial worth (x 1 000 000)");

  return chart;
});