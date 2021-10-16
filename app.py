from flask import Flask, render_template, request
from bs4 import BeautifulSoup
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route('/compare', methods=['POST'])
def comparison():
    
    player_name1=request.form['Player_Name1']
    team1=request.form['Team1']
    season1=request.form['Season1']
    player_name2=request.form['Player_Name2']
    team2=request.form['Team2']
    season2=request.form['Season2']


    # ==================1ST PLAYER GAME LOGS =====================

    game_log_path = "https://www.hockey-reference.com/teams/{}/{}_games.html".format(team1, season1)

    # # create a driver
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=True)

    # # use browser to pull html
    browser.visit(game_log_path)
    html = browser.html  

    soup = BeautifulSoup(html, 'html.parser')

    tbodies = soup.find_all('tbody')
    tbody = tbodies[0]
    tds = tbody.find_all('td')
    game_pages = tbody.find_all("td", attrs={"data-stat": "date_game"})

    urlextensions = []
    for e in game_pages:
        atag = e.find('a')
        urlextensions.append(atag["href"])

    gameurls = []
    base_url = "https://www.hockey-reference.com"
    for extension in urlextensions:
        gameurls.append(base_url+extension)

    # ==================1ST PLAYER STAT COMPARISON =====================

    searched_player1 = player_name1
    searched_team1 = team1

    SP1WGoals = 0
    SP1WAssists = 0
    SP1WAssists2 = 0

    SP1OTLGoals = 0
    SP1OTLAssists = 0
    SP1OTLAssists2 = 0
    team1_total=0
    # SO1Goals = 0

    for each_url in gameurls:
        game_scoring = pd.read_html(each_url, match='Scoring Summary')
        

        scoring = game_scoring[0]
        scoring_renamed = scoring.rename(columns={"1st Period.1": "index", "1st Period": "Time", "1st Period.2":"Goal_Type", "1st Period.3": "scorer", "1st Period.4":"Apples", "2nd Period.1": "index", "2nd Period": "Time", "2nd Period.2":"Goal_Type", "2nd Period.3": "scorer", "2nd Period.4":"Apples", "3rd Period.1": "index", "3rd Period": "Time", "3rd Period.2":"Goal_Type", "3rd Period.3": "scorer", "3rd Period.4":"Apples" })
        try:
            scoring_renamed['Apples'].fillna('No Assists', inplace=True)
        except:pass

        for index, row in scoring_renamed.iterrows():
            try:
                assists = scoring_renamed.Apples.str.split(pat=", ", expand=True)
                assists.fillna('No Assists', inplace=True)
            except:pass
            try:
                assists["Assists1"]= assists[0]    
                assists = assists.drop([0], axis=1)
            except:
                assists["Assists1"] = "No Assists"
            try:
                assists["Assists2"]= assists[1]
                assists = assists.drop([1], axis=1)
            except:
                assists["Assists2"] = "No Assists"

        try:
            scoring_renamed[['first_last', 'number']] = scoring_renamed.scorer.str.rsplit(pat=' ', n=1, expand=True)
            scoring_df = scoring_renamed.rename(columns={"index": "Team", "first_last": "Goal_Scorer"})
            scoring_df=scoring_df[['Team', 'Time', 'Goal_Type', 'Goal_Scorer']]
            scoring_df = pd.concat([scoring_df, assists], axis=1)
        except:pass

            
        if "Shootout" in scoring.values: 
            periods = scoring_df.loc[(scoring_df["Time"] == "1st Period") | (scoring_df["Time"] == "2nd Period") | (
            scoring_df["Time"] == "3rd Period") | (scoring_df["Time"] == "1st OT Period") | (scoring_df["Time"] == "Shootout"), :].index
            goal_df=scoring_df.drop(periods)
            
            search_team = 0
            other_team = 0
            
            
            for index, row in goal_df.iterrows():
                if row[0] == searched_team1:
                    search_team = search_team + 1
                else: other_team = other_team + 1

            if search_team > other_team:
                team1_total = team1_total + search_team
                    

            if search_team > other_team:
                for index, row in goal_df.iterrows():
                    if row[3] == searched_player1:
                        SP1WGoals = SP1WGoals + 1
                    if row[4] == searched_player1:
                        SP1WAssists = SP1WAssists + 1
                    try:
                        if row[5] == searched_player1:
                            SP1WAssists2 = SP1WAssists2 + 1
                    except:pass
            else:
                for index, row in goal_df.iterrows():
                    if row[3] == searched_player1:
                        SP1OTLGoals = SP1OTLGoals + 1
                    if row[4] == searched_player1:
                        SP1OTLAssists = SP1OTLAssists + 1
                    try:
                        if row[5] == searched_player1:
                            SP1OTLAssists2 = SP1OTLAssists2 + 1
                    except:pass
                        
                        
        elif "1st OT Period" in scoring.values:
            periods = scoring_df.loc[(scoring_df["Time"] == "1st Period") | (scoring_df["Time"] == "2nd Period") | (
            scoring_df["Time"] == "3rd Period") | (scoring_df["Time"] == "1st OT Period") | (scoring_df["Time"] == "Shootout"), :].index
            goal_df=scoring_df.drop(periods)
            
            search_team = 0
            other_team = 0
            
            
            for index, row in goal_df.iterrows():
                if row[0] == searched_team1:
                    search_team = search_team + 1
                else: other_team = other_team + 1

            if search_team > other_team:
                team1_total = team1_total + search_team
                    
            if search_team > other_team:
                for index, row in goal_df.iterrows():
                    if row[3] == searched_player1:
                        SP1WGoals = SP1WGoals + 1
                    if row[4] == searched_player1:
                        SP1WAssists = SP1WAssists + 1
                    try:
                        if row[5] == searched_player1:
                            SP1WAssists2 = SP1WAssists2 + 1
                    except:pass
            else:
                for index, row in goal_df.iterrows():
                    if row[3] == searched_player1:
                        SP1OTLGoals = SP1OTLGoals + 1
                    if row[4] == searched_player1:
                        SP1OTLAssists = SP1OTLAssists + 1
                    try:
                        if row[5] == searched_player1:
                            SP1OTLAssists2 = SP1OTLAssists2 + 1
                    except:pass
        else:
            periods = scoring_df.loc[(scoring_df["Time"] == "1st Period") | (scoring_df["Time"] == "2nd Period") | (
            scoring_df["Time"] == "3rd Period") | (scoring_df["Time"] == "1st OT Period") | (scoring_df["Time"] == "Shootout"), :].index
            goal_df=scoring_df.drop(periods)
            
            search_team = 0
            other_team = 0
            
            
            for index, row in goal_df.iterrows():
                if row[0] == searched_team1:
                    search_team = search_team + 1
                else: other_team = other_team + 1
                    
            s_team=0
            
            if search_team > other_team:
                print(each_url)
                for index, row in goal_df.iterrows():
                    if row[0] == searched_team1:
                        s_team = s_team + 1
                        if row[0] == searched_team1 and s_team <= other_team + 1:
                            team1_total = team1_total +1
                        if row[3] == searched_player1 and s_team <= other_team + 1:
                            SP1WGoals = SP1WGoals + 1
                        if row[4] == searched_player1 and s_team <= other_team + 1:
                            SP1WAssists = SP1WAssists + 1
                        try:
                            if row[5] == searched_player1 and s_team <= other_team + 1:
                                SP1WAssists2 = SP1WAssists2 + 1
                        except: pass

    SP1Goals2Comb = SP1WGoals + SP1OTLGoals
    SP1WAComb = SP1WAssists + SP1WAssists2
    SP1OTLAComb2 = SP1OTLAssists + SP1OTLAssists2




    #======================2ND PLAYER GAME LOGS==========================


    game_log_path = "https://www.hockey-reference.com/teams/{}/{}_games.html".format(team2, season2)

    # create a driver
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=True)

    # use browser to pull html
    browser.visit(game_log_path)
    html = browser.html  

    soup = BeautifulSoup(html, 'html.parser')

    tbodies = soup.find_all('tbody')
    tbody = tbodies[0]
    tds = tbody.find_all('td')
    game_pages = tbody.find_all("td", attrs={"data-stat": "date_game"})

    urlextensions = []
    for e in game_pages:
        atag = e.find('a')
        urlextensions.append(atag["href"])

    gameurls = []
    base_url = "https://www.hockey-reference.com"
    for extension in urlextensions:
        gameurls.append(base_url+extension)

    #==================2ND PLAYER STAT COMPARISON =====================

    searched_player2 = player_name2
    searched_team2 = team2

    SP2WGoals = 0
    SP2WAssists = 0
    SP2WAssists2 = 0

    SP2OTLGoals = 0
    SP2OTLAssists = 0
    SP2OTLAssists2 = 0
    team2_total = 0
    # SO2Goals = 0
    # SP2Goals2Comb = 0
    # SP2WAComb = 0
    # SP2OTLAComb2 = 0

    for each_url in gameurls:
        game_scoring = pd.read_html(each_url, match='Scoring Summary')
        

        scoring = game_scoring[0]
        scoring_renamed = scoring.rename(columns={"1st Period.1": "index", "1st Period": "Time", "1st Period.2":"Goal_Type", "1st Period.3": "scorer", "1st Period.4":"Apples", "2nd Period.1": "index", "2nd Period": "Time", "2nd Period.2":"Goal_Type", "2nd Period.3": "scorer", "2nd Period.4":"Apples", "3rd Period.1": "index", "3rd Period": "Time", "3rd Period.2":"Goal_Type", "3rd Period.3": "scorer", "3rd Period.4":"Apples" })
        try:
            scoring_renamed['Apples'].fillna('No Assists', inplace=True)
        except:pass

        for index, row in scoring_renamed.iterrows():
            try:
                assists = scoring_renamed.Apples.str.split(pat=", ", expand=True)
                assists.fillna('No Assists', inplace=True)
            except:pass
            try:
                assists["Assists1"]= assists[0]    
                assists = assists.drop([0], axis=1)
            except:
                assists["Assists1"] = "No Assists"
            try:
                assists["Assists2"]= assists[1]
                assists = assists.drop([1], axis=1)
            except:
                assists["Assists2"] = "No Assists"

        try:
            scoring_renamed[['first_last', 'number']] = scoring_renamed.scorer.str.rsplit(pat=' ', n=1, expand=True)
            scoring_df = scoring_renamed.rename(columns={"index": "Team", "first_last": "Goal_Scorer"})
            scoring_df=scoring_df[['Team', 'Time', 'Goal_Type', 'Goal_Scorer']]
            scoring_df = pd.concat([scoring_df, assists], axis=1)
        except:pass

            
        if "Shootout" in scoring.values: 
            periods = scoring_df.loc[(scoring_df["Time"] == "1st Period") | (scoring_df["Time"] == "2nd Period") | (
            scoring_df["Time"] == "3rd Period") | (scoring_df["Time"] == "1st OT Period") | (scoring_df["Time"] == "Shootout"), :].index
            goal_df=scoring_df.drop(periods)
            
            search_team = 0
            other_team = 0
            
            
            for index, row in goal_df.iterrows():
                if row[0] == searched_team2:
                    search_team = search_team + 1
                else: other_team = other_team + 1

            if search_team > other_team:
                team2_total = team2_total + search_team

            if search_team > other_team:
                for index, row in goal_df.iterrows():
                    if row[3] == searched_player2:
                        SP2WGoals = SP2WGoals + 1
                    if row[4] == searched_player2:
                        SP2WAssists = SP2WAssists + 1
                    try:
                        if row[5] == searched_player2:
                            SP2WAssists2 = SP2WAssists2 + 1
                    except:pass
            else:
                for index, row in goal_df.iterrows():
                    if row[3] == searched_player2:
                        SP2OTLGoals = SP2OTLGoals + 1
                    if row[4] == searched_player2:
                        SP2OTLAssists = SP2OTLAssists + 1
                    try:
                        if row[5] == searched_player2:
                            SP2OTLAssists2 = SP2OTLAssists2 + 1
                    except:pass
                        
                        
        elif "1st OT Period" in scoring.values:
            periods = scoring_df.loc[(scoring_df["Time"] == "1st Period") | (scoring_df["Time"] == "2nd Period") | (
            scoring_df["Time"] == "3rd Period") | (scoring_df["Time"] == "1st OT Period") | (scoring_df["Time"] == "Shootout"), :].index
            goal_df=scoring_df.drop(periods)
            
            search_team = 0
            other_team = 0
            
            
            for index, row in goal_df.iterrows():
                if row[0] == searched_team2:
                    search_team = search_team + 1
                else: other_team = other_team + 1
            
            if search_team > other_team:
                team2_total = team2_total + search_team

            if search_team > other_team:
                for index, row in goal_df.iterrows():
                    if row[3] == searched_player2:
                        SP2WGoals = SP2WGoals + 1
                    if row[4] == searched_player2:
                        SP2WAssists = SP2WAssists + 1
                    try:
                        if row[5] == searched_player2:
                            SP2WAssists2 = SP2WAssists2 + 1
                    except:pass
            else:
                for index, row in goal_df.iterrows():
                    if row[3] == searched_player2:
                        SP2OTLGoals = SP2OTLGoals + 1
                    if row[4] == searched_player2:
                        SP2OTLAssists = SP2OTLAssists + 1
                    try:
                        if row[5] == searched_player2:
                            SP2OTLAssists2 = SP2OTLAssists2 + 1
                    except:pass
        else:
            periods = scoring_df.loc[(scoring_df["Time"] == "1st Period") | (scoring_df["Time"] == "2nd Period") | (
            scoring_df["Time"] == "3rd Period") | (scoring_df["Time"] == "1st OT Period") | (scoring_df["Time"] == "Shootout"), :].index
            goal_df=scoring_df.drop(periods)
            
            search_team = 0
            other_team = 0
            
            
            for index, row in goal_df.iterrows():
                if row[0] == searched_team2:
                    search_team = search_team + 1
                else: other_team = other_team + 1
                    
            s_team=0
            if search_team > other_team:
                print(each_url)
                for index, row in goal_df.iterrows():
                    if row[0] == searched_team2:
                        s_team = s_team + 1
                        if row[0] == searched_team2 and s_team <= other_team + 1:
                            team2_total = team2_total +1
                        if row[3] == searched_player2 and s_team <= other_team + 1:
                            SP2WGoals = SP2WGoals + 1
                        if row[4] == searched_player2 and s_team <= other_team + 1:
                            SP2WAssists = SP2WAssists + 1
                        try:
                            if row[5] == searched_player2 and s_team <= other_team + 1:
                                SP2WAssists2 = SP2WAssists2 + 1
                        except: pass

        SP2Goals2Comb = SP2WGoals + SP2OTLGoals
        SP2WAComb = SP2WAssists + SP2WAssists2
        SP2OTLAComb2 = SP2OTLAssists + SP2OTLAssists2



    game_dict={ "stat_category": "amount",
                "Player1":player_name1 + " " + team1 + " Season ending in " + season1,
                "SP1WGoals":SP1WGoals,
                "SP1WAssists":SP1WAssists,
                "SP1WAssists2": SP1WAssists2,  
                "SP1OTLGoals": SP1OTLGoals,
                "SP1OTLAssists": SP1OTLAssists,
                "SP1OTLAssists2": SP1OTLAssists2,
                "SP1Goals2Comb": SP1Goals2Comb,
                "SP1WAComb": SP1WAComb,
                "SP1OTLAComb2": SP1OTLAComb2,
                "Player2":player_name2 + " " + team2 + " Season ending in " + season2,
                "SP2WGoals":SP2WGoals,
                "SP2WAssists":SP2WAssists,
                "SP2WAssists2": SP2WAssists2,  
                "SP2OTLGoals": SP2OTLGoals,
                "SP2OTLAssists": SP2OTLAssists,
                "SP2OTLAssists2": SP2OTLAssists2,
                "SP2Goals2Comb": SP2Goals2Comb,
                "SP2WAComb": SP2WAComb,
                "SP2OTLAComb2": SP2OTLAComb2,
                "team1_total": team1_total,
                "team2_total": team2_total,
                "team1_name": team1 + " total goals in " + season1,
                "team2_name": team2 + " total goals in " + season2,
                "percent1": "Percent of team goals involving " + player_name1,
                "percent2": "Percent of team goals involving " + player_name2,}


    (pd.DataFrame.from_dict(data=game_dict, orient='index')
   .to_csv('templates/game_dict.csv', header=False))

    return render_template("complete.html")


 
if __name__ == "__main__":
    app.run(debug=True)

