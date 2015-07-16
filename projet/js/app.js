/* Inspired by Lee Byron's test data generator. */ 
function stream_layers(n, m, o) { 
  if (arguments.length < 3) o = 0; 
  function bump(a) { 
    var x = 1 / (.1 + Math.random()), 
        y = 2 * Math.random() - .5, 
        z = 10 / (.1 + Math.random()); 
    for (var i = 0; i < m; i++) { 
      var w = (i / m - y) * z; 
      a[i] += x * Math.exp(-w * w); 
    } 
  } 
  return d3.range(n).map(function() { 
      var a = [], i; 
      for (i = 0; i < m; i++) a[i] = o + o * Math.random(); 
      for (i = 0; i < 5; i++) bump(a); 
      return a.map(stream_index); 
    }); 
}

function stream_index(d, i) { 
  return {x: i, y: Math.max(0, d)}; 
}  

nv.addGraph(function() {
  var chart = nv.models.multiBarChart();

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

  chart.x(function(d) { return d.Ref_Date; });
  chart.y(function(d) { return d["Compensation of employees (x 1 000 000)"]; });

  //chart.xAxis
  //    .tickFormat(d3.format(',f'));

  chart.yAxis
      .tickFormat(d3.format(',.2f'));

  //chart.y2Axis
  //    .tickFormat(d3.format(',.2f'));


  d3.select('#chart svg')
      .datum(allData)
      .transition().duration(500)
      .call(chart);


  nv.utils.windowResize(chart.update);

  return chart;
});

/**************************************
 * Simple test data generator
 */

function testData() {
  return stream_layers(3,128,.1).map(function(data, i) {
    return { 
      key: 'Stream' + i,
      values: data
    };
  });
}