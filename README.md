# NHL_Player_Comparison

Following the 2017-18 National Hockey League season, Taylor Hall, of the New Jersey Devils, was voted the winner of the Hart Memorial Trophy as the league's most valuable player, narrowly edging out Nathan MacKinnon, of the Colorado Avalanche. Many felt that, despite Hall having ever so slightly better statistics during the season, that MacKinnon should have won as he was seen as the player who carried the Colorado Avalanche and more valuable to their success than Hall was to the Devils. This project, inspired by this Hart Trophy voting, was created to try to determine who was actually the more valuable player, and who should have received the Hart Memorial Trophy.

Included in the repo is the csv for Nathan MacKinnon vs Taylor Hall for the 2017-18 season. Running the comparison.html file in a live server will show that. Running the index.html will allow you to select your own players. 

The following graphs compare the performance of the two searched players for their respective selected season. This data differs from standard season data as there were restrictions on which goals and assists would count so that only goals that helped the team win were counted.

The restrictions are as follows:

1) Any game where the searched player's team loses in regulation is completely removed as the team did not earn any points in the standings.

2) For games that went into overtime, all goals by the searched player count, as all goals were needed to gain the 2 standings points for a win, or the single standings point for an overtime loss.

3) Shootout goals were not counted, as they do not count in standard goal totals.

4) For games that the searched player's team wins in regulation, only the goals scored up to the Game Winning Goal (losing teams' goal total + 1) are counted.

Example: Searched player's team wins 5-2, only the first 3 goals scored by the winning team will be counted, as the remaining 2 goals were not required to win the game.



Select Players to Compare - Player names must be spelled as they appear on www.hockey-reference.com as that is the provider of the game data.

![select](https://user-images.githubusercontent.com/75753889/137570165-d0517222-6d87-4615-87f4-6ea1a74b3465.jpg)

Data Scraping Complete - Due to some connection issues that have not yet been resolved, this will appear when the data scraping has finished and the csv is ready to be read to build the charts. Opening the comparison.html file will show the charts with the newly scraped data.

![complete](https://user-images.githubusercontent.com/75753889/137570253-0c16ae28-86c8-4793-8c34-dd48b3c041b4.jpg)


Split Goals and Assists - Each player's goals and assist totals compared to each other.
![splittotals](https://user-images.githubusercontent.com/75753889/137570283-c7193e44-8b6f-46d1-a469-8c928f6ac8c8.jpg)

Combined Goals and Assists - Each player's combined goals, primary assists, and secondary assists compared to each other.
![combinedtotals](https://user-images.githubusercontent.com/75753889/137570319-d194aca8-a7eb-46f6-b1d2-43860459f1e1.jpg)

Percent Of Team Goals Player Was Involved In

In the following two graphs, the green bar shows the percent of the team's total goals that the searched player was involved in, either by scoring the goal, or providing a primary or secondary assist to the goal scorer. The higher the percentage, the more that player was reponsible for his team's success, thus being more valuable to the team.
![percentp1](https://user-images.githubusercontent.com/75753889/137570343-e07f11e8-3148-456e-b138-85206a327df0.jpg)
![percentp2](https://user-images.githubusercontent.com/75753889/137570347-cf7401a4-f009-4c5d-a126-d3daff376000.jpg)
