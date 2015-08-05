
/* Inspired by Lee Byron's test data generator. */
/**
 *
 * @param n
 * @param m
 * @param o
 * @returns {Array}
 */
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

/**
 *
 * @param d
 * @param i
 * @returns {{x: *, y: number}}
 */
function stream_index(d, i) { 
  return {x: i, y: Math.max(0, d)}; 
}

/**
 *
 */
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

//Donut chart example
nv.addGraph(function() {
    var chart = nv.models.pieChart()
            .x(function(d) { return d.label })
            .y(function(d) { return d.value })
            .showLabels(true)     //Display pie label
            .labelThreshold(.05)  //Configure the minimum slice size for labels to show up
            .labelType("value") //Configure what type of data to show in the label. Can be "key", "value" or "percent"
            .donut(true)          //Turn on Donut mode. Makes pie chart look tasty!
            .donutRatio(0.4)     //Configure how big you want the donut hole size to be.
        ;

    d3.select("#govchart svg")
        //.datum(govtSummaryList)
        .datum(govtInPower())
        .transition().duration(350)
        .call(chart);

    return chart;
});

function govtInPower(){
    var govtList = [
        {	"begin": "1988/11/21",
            "end": "1993/10/25",
            "party": "Progressive conservative",
            "type": "majority"
        },
        {	"begin": "1993/10/25",
            "end": "1997/06/02",
            "party": "Liberal",
            "type": "majority"
        },
        {	"begin": "1997/06/02",
            "end": "2000/11/27",
            "party": "Liberal",
            "type": "majority"
        },
        {	"begin": "2000/11/27",
            "end": "2004/06/28",
            "party": "Liberal",
            "type": "majority"
        },
        {	"begin": "2004/06/28",
            "end": "2006/01/23",
            "party": "Liberal",
            "type": "minority"
        },
        {	"begin": "2006/01/23",
            "end": "2008/10/14",
            "party": "Conservative",
            "type": "minority"
        },
        {	"begin": "2008/10/14",
            "end": "2011/05/02",
            "party": "Conservative",
            "type": "minority"
        },
        {	"begin": "2011/05/02",
            "end": "N/A",
            "party": "Conservative",
            "type": "majority"
        }
    ];

    // Global summary list for the days in power for each government
    govtSummaryList = [{"label":"Liberal","value":56}, {"label":"Conservative","value":78}];

    govtList.forEach(function(element){
        calculateDaysInPower(element,govtSummaryList);
    });

    return govtSummaryList;
}

/**
 * Calculate the number of days in power
 *
 **/
function calculateDaysInPower(element, govtsummary){
    var numberOfDays = 0;
    var partyName = element.party;

    if(element.end != "N/A"){
        numberOfDays = Math.floor( (Date.parse(element.end)- Date.parse(element.begin)) / (1000*60*60*24));
    } else {
        numberOfDays = Math.floor( (Date.now() - Date.parse(element.begin)) / (1000*60*60*24));
    }

    // Verify if party exists in data array
    // if yes, append the # of days
    var foundMatch = false;

    for(var i = 0;i < govtsummary.length; i++) {
        console.log("The actual ");
        if (govtsummary[i].label === partyName) {
            govtsummary[i].value += numberOfDays;
            foundMatch = true;
            break;
        }
    }

    // If no existing party has been found, add the item
    if(!foundMatch){
        govtsummary.push({"label": partyName, "value": numberOfDays});
    }
};

/**
 * For a given party, return the percentage of the time they where in majority when in power
 */
function calculateMajorityPercentage(element, govtsummary){

}

/**
 * For a given party, return the percentage of the time they where in majority when in power
 */
function calculateMinorityPercentage(element, govtsummary){

}