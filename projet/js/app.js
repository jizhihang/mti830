/**
 *
 */
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
  svg.append("rect")
            .attr("y", 0)
            .attr("x", 60)
            .attr("width", 150)
            .attr("height", 700)
            .attr("fill", "rgba(0,255,255, 0.4")
            .attr("class", "legendBar");

  svg.append("rect")
            .attr("y", 0)
            .attr("x", 210)
            .attr("width", 525)
            .attr("height", 700)
            .attr("fill", "rgba(255,0,0, 0.4")
            .attr("class", "legendBar");

  svg.append("rect")
            .attr("y", 0)
            .attr("x", 735)
            .attr("width", 75)
            .attr("height", 700)
            .attr("fill", "rgba(255,0,0, 0.2")
            .attr("class", "legendBar");

  svg.append("rect")
            .attr("y", 0)
            .attr("x", 810)
            .attr("width", 275)
            .attr("height", 700)
            .attr("fill", "rgba(0,0,255, 0.2")
            .attr("class", "legendBar");

  svg.append("rect")
            .attr("y", 0)
            .attr("x", 1085)
            .attr("width", 200)
            .attr("height", 700)
            .attr("fill", "rgba(0,0,255, 0.4")
            .attr("class", "legendBar");

  svg.datum(allData)
      .transition().duration(500)
      .call(chart);


  nv.utils.windowResize(chart.update);

  sel.val("Net financial worth (x 1 000 000)");

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