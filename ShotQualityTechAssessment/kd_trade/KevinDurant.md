** KD TO THE KNICKS **

Initially I was thinking how would it look to see Kevin Durant on the Warriors after the 2023-2024 season, where he makes his return to the Warriors to reclaim another title for Stephen Curry following the departure of Klay Thompson, however after realizing this data set was set in 2021-22, the year the Warriors won, I figured it would be pretty uninteresting to see those effects. So as a New York native, let me annoy the public and make KD switch NY alliances, Kevin Durant to the New York Knicks.

The New York Knicks in the 2021-2022 season saw a roster, that for the first time in a long time, had some potential to make something happen in the league, however that something to happen wouldn't amount to anymore than some playoff wins. But what if they were able to bring someone in like KD to be that player they could rely on, takeover the big moments, and become the difference in their championship dreams.

Thought Process:
To begin, I need prepare my data for further analysis on how Kevin Durant would affect the new lineup he would be getting into, the players that made up the Knicks most common starting 5 was Rj Barrett, Evan Fournier, Alec Burks, Julius Randle and Mitchell Robinson. There are a few other players that made the mix where there was a 5 with Kemba Walker, but the lineup stated before was the lineup that was most common (Basketball-Reference).

    so the starting five is:
    PG: Evan Fournier
    SG: RJ Barrett:
    SF: Kevin Durant
    PF: Julius Randle
    C: Mitchell Robinson

    and the existing starting five on the Brooklyn Nets is:
    PG: James Harden
    SG: Joe Harris
    SF: Kevin Durant
    PF: Blake Griffin
    C: Nick Claxton

    In approaching this problem, its going to be really interesting to see how the usage of KD is going to impact the Knicks, Randle was definitely the go to guy in big moments and was an all star in 2021, 2023 and 2024 so with KD on the team, would Randle have been an all star? Will the Knicks benefit in the welcoming of a super star? Is a championship a possibility? Lets see.

    ** Data Cleaning: **

    Since I was working with the Knicks and Nets, I first needed to filter for just these two teams as the rest of the league meant nothing to the dynamic of how Kevin Durant impacted his team and how he would impact his future team.
    Then I needed to search for rows that included scoring information, so information like the jumpball or the end of a period don't have any relevance to the ppg of each player.
    Then I realized that instead of filtering based on description, just filter based on when the score goes up (maybe for either the knicks or the nets)
    In Addition, when there are no players in the first player column, that directly means that the event wasnt a scoring event so it wasn't necessary to include events that didn't have a player 1 in it

    The first thing after filtering out the information I needed, is to understand what exactly is the best way of sorting this all



    First I needed to calculate each players usage rate in scoring plays and understand how they play with each other in both existing rosters, this will act as a new feature for use

** Model Selection: **
For understanding the points per game of this new starting 5, I believe the impact of KD will be linear to that of his teammates as the ppg of his will directly impact the points of his teammates, so lets see how linear regression would work with this situation, this assumes that shot attempts are redistributed evenly and doesn't take into account fatigue, changes in play style and is directly based on the data given
