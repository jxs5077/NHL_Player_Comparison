d3.csv("game_dict.csv", function(d) {
  
    var trace1 = {
          x: ['Goals', 'Total Assists'],
          y: [d[1]['amount'], d[8]['amount']],
          
          name: d[0]['amount'],
          type: 'bar',
        };
      
    var trace2 = {
          x: ['Goals','Total Assists'],
          y: [d[11]['amount'], d[18]['amount']],
        
          name: d[10]['amount'],
          type: 'bar',
        };
    
        var data = [trace1, trace2];
        
  
    var layout = { 
      title: "Split Goal and Assist Totals",
      barmode: 'group' };
  
    Plotly.newPlot('bar_plot', data, layout)});