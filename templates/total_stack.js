



d3.csv("game_dict.csv", function(d) {
    console.log(d[0]['stat_category']);

    A1 = parseFloat(d[2]['amount'])
    A2 = parseFloat(d[5]['amount'])
    A3 = parseFloat(d[3]['amount'])
    A4 = parseFloat(d[6]['amount'])

    B1 = parseFloat(d[12]['amount'])
    B2 = parseFloat(d[15]['amount'])
    B3 = parseFloat(d[13]['amount'])
    B4 = parseFloat(d[16]['amount'])
  
    var goals = {
          x: [d[0]['amount'], d[10]['amount']],
          y: [d[7]['amount'], d[17]['amount']],
          
          name: 'Goals',
          type: 'bar',
        };
      
    var PriAsst= {
          x: [d[0]['amount'], d[10]['amount']],
          y: [(A1+A2), (B1+B2)],
        
          name: 'Primary Assists',
          type: 'bar',
        };

    var SecAsst= {
        x: [d[0]['amount'], d[10]['amount']],
        y: [(A3+A4), (B3+B4)],
        
        name: 'Secondary Assists',
        type: 'bar',
        };
    
        var data = [goals, PriAsst, SecAsst];
        
  
    var layout = {
        title: "Combined Goal and Assist Totals",
        barmode: 'stack' };
  
    Plotly.newPlot('total_bar', data, layout)});