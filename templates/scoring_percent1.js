d3.csv("game_dict.csv", function(d) {
    console.log(d[0]['stat_category']);

    A1 = parseFloat(d[2]['amount'])
    A2 = parseFloat(d[5]['amount'])
    A3 = parseFloat(d[3]['amount'])
    A4 = parseFloat(d[6]['amount'])
    A5 = parseFloat(d[7]['amount'])

    B1 = parseFloat(d[12]['amount'])
    B2 = parseFloat(d[15]['amount'])
    B3 = parseFloat(d[13]['amount'])
    B4 = parseFloat(d[16]['amount'])
    B5 = parseFloat(d[17]['amount'])

    T1 = parseFloat(d[20]['amount'])
    T2 = parseFloat(d[21]['amount'])

    // var trace1 = {
    //     x: [d[0]['amount'], d[0]['amount'], d[0]['amount']],
    //     y: [d[7]['amount'], (A1+A2), (A3+A4)],
    //     type: 'bar',
    // }

    var team1_total= {
        x:[d[22]['amount']],
        y:[T1],
        name:'Total Team Goals',
        type: 'bar',
    };

    var player1= {
        x: [d[0]['amount']],
        y: [(A1+A2+A3+A4+A5)],
        name:'Total Player Involved Goals',
        type: 'bar',
    };

    var percent1= {
        x: [d[24]['amount']],
        y: [((A1+A2+A3+A4+A5)/T1)*100],
        name: 'Percent of Team Goals Involved In',
        type: 'bar',
    };

    
    var data = [player1, team1_total, percent1];
        
  
    var layout = { 
        title: "Percent Of Team Goals Player 1 Was Involved In",
        barmode: 'stack' };
  
    Plotly.newPlot('percent', data, layout)});