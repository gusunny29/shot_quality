# Fall 2024 Technical Assessment

## Modeling

Given you have access to play by plays for all professional leagues globally, the wide range of available data gives us a lot of variety in creating a model for predicting if a shot is made in the Euroleague

How would you approach the modeling question?
This problem can be classified into a binary classification problem where each shot attempt has two outcomes: the shot is made (we can represent that result with a 1) or the shot being missed (represented as 0).

Inputs: X = [play by play game data, location data represented with x and y coordinates]
Target Variable: Y = [shot_made]

For our play by play data I think the best features to include into our input should include:

- Defensive distancing from the shot taker
- Type of shot (layup, dunk, mid-range, 3 pointer, etc)
- Player details (Shot selection pattern, position, usage)
  This in combination with our player locations will allow for detailed features that will directly affect the accuracy of our model

In addition, the need to clean, train, predict and evaluate the model will tell us all we need to know which will explained further

** Cleaning **

Highly essential in developing accurate results as invalid data can skew the results inaccurately

- Since our data consists of all play by play data, we want to filter it to only include plays that involve a shot as moments like the tip off or a steal don't affect the outcome of a shot attempt
- Discarding moments that contain missing information that would be crucial to predicting shot makes
- Cleaning out outliers and rows with invalid/incomplete data

** Feature Engineering **

In building and training our Euroleague model, the features we provide directly determine the accuracy our our results. Given the access we have to the play by play data from the 2021-2022 NBA season, here are some features that we can compose to train our model:

Physical Features:

- Nearest defender(s) distance from the shooter
  - Of course if there are more defenders with similar "pressure" levels to the shooter can definitely decrease likelihood of shot makes
- Distance of shooter to the basket
- Angle of shooter to the basket
- Calculating the pentagonal area of the defensive positioning and their relation to the shot and understanding how that affects the shot attempt

Contextual Features:

- What quarter is it? How much time is left?
- Is the shooter blowing the team out, getting blown out, or is the game a close one where a bucket is needed now?
  - Perhaps based on the player and their patterns/shooting percentages in past clutch moments
- Minutes played up to the point of the shot
  - have many continuous minutes has the player been on the floor
  - how many total minutes has the player been on the floor

** Model Selection **

From reading this project, it seems there can be a few ways to derive accurate predictions but this would potentially be a way I would go about
analyzing this study

- Begin by applying a Logistical Regression model to develop some beginning understanding of how relevant some features are but then using a Random Forest model as this relationship isn't necessarily linear so models such as Linear Regression wouldn't provide much information on the goal at hand
- Decision Tree models in this case would be super helpful as it provides us with a clear understanding of "Player A took X shot, did he make it or did he miss it" and with the data we have, we can move towards determining which shots were higher percentage vs lower percentage
- XGBoost definitely can play a role in handling as large of a data set and as a tree based model, it has existing ways of handling missing values and hypertuning capabilities which can filter for more reliable data. - This method is also very common within sports analytics and can provide us with insights as to which features contribute most to a players performance and ability to make shots

** Model Training **

- Oversampling/Undersampling: In basketball, the range of shot selection definitely isn't equal (but to be fair in the past decade 3 pointers definitely have sky-rocketed in percentage of shots taken) and a majority of shots also miss, so it's important to utilize both processes when needed to introduce balance between the majority and the minority class, whether that includes too many layups being taken into account or too few 3 above the arch 3s, this is a crucial component in providing "reliable" data
- Cross Validation: Given the large range of the data set, using cross validation can be considered to avoid overfitting due to the fact its difficult to make an absolute prediction on shots attempted as it's not always reliant to assume the context is just an open shot and can be a combination of variables to affect the outcome

** Model Maintenance **

- To begin, in attempts to maintain the accuracy of our model, its essential after certain periods of time, testing and training with the most recent data (whether that be after half a season, a full season, a new draft class or trades) and if the performance falls, retraining and testing would be beneficial
- To expedite the process and reduce human error after training the model successfully, setting up automation for testing would be highly beneficial as retrieving consistent updates on the state of the model would be ideal
- Maintain the data pipelines and warehouses, ensure security of model (given this is most likely a product that shouldn't be publically accessible unless subscripted), and ensure robust api endpoints to confirm the expected data that is coming in

** Production Workflow **

- After practices, scrimmages, full euroleague games/seasons, the model should be runnable on the dataset and predict efficiently
- This can go along with ensuring data pipelines as the ability to hit the api and feed new shots into the model should produce accurate predictions, at any time for whatever size of data
- Handling larger datasets in parallel threads to avoid memory or performance issues and to handle the ingestion efficiently
- Of course if the ability to have too much memory for use would be nice, but if not accessible, definitely finding ways to be efficient is important

** Hardware Constraints and their effects on production**

Given the fact we have data from every play of every league globally, hardware constraints are definitely going to be an issue unless you have access to an incredible amount of memory and storage space

- Memory Constraints:
  - Perhaps undersampling less features or leagues at a time
    - This can be relevant in cleaning, I would attempt to compare the Euroleague to leagues which are comparable in skill rather than including all leagues in the world.
    - This can also lead to less accurate predictions as we could be leaving out possibly impactful information
- Connection and Latency
  - Picking and Choosing which models to deploy when
    - For example using the simple logistic regression to calculate a given shot's probability for quick not memory intensive results and then for maybe a full 5 game stretch of plays using a combination of models as you are mostly interested in the results, not really dependent on the time it takes to retrieve it

Conclusion:
In attempting to build a model for the Euroleague in predicting the success of shots definitely requires a good mixture of features (from spatial calculations and player habits to types of shots and angular components) this process can definitely become complex while also attempting to make this robust enough where its efficient and usable to the customers its sold to. With the model training, testing and maintenance process, its easy to become lost in which processes to pursue with but in the case with shot success, a mixture of logistic regression and random forest training caters to probability nicely and can provide some accurate predictions directly related to the goal. In eliminating latency and performance issues, finding cloud based environments or container applications such as Docker would definitely help in deploying in a production sense.

## Database

Building a database that should be delivering a single stream of box scores and play by play to API users from different sports sources definitely has its complexities to it.

** Database Design **

The Database that would fit this structure the best would be a relational database, maybe in mySQL, Snowflake, PostgreSQL, as it supports complex joins for different aggregations of league specific data requests.

- Using a NoSQL Database could work in this instance but with the relations and structure that can be expected with these tables, it only makes sense to use a relational database

** Type of Schema **

Given that the intended result is a single stream of box scores and play by play to API users, we need tables for:

- Players - Teams - Games - Box Scores - Play by Play - Season - League (NCAA, NBA)
- Each of these should be a separate table instead of including duplicates of instances across more broad categories
- A good common ground that can be used in aggregating data in the context of massive data sets is by indexing dates/times to increase efficiency in finding data
- Can also utilize partitioning across said game dates and time of game to breakdown the data set further to optimize accessing and finding data efficiently

- For organization purposes, also storing the source of each data point is important

- as we are handling data from multiple sources, very ideal to have access to the source of the data for validation

  - in addition, with different structures and formats of data from different sources, for player name display, play by play descriptions and etc, its not common for EVERY system to use the same formatting and wording, so coming up with a standard format across each of the categories and data is important

** Security **

- Authentication
- Implementing 2 Factor Authentication and maintaining API key management is at the forefront of security and only those that have access to this should be granted that access.
- Role of User
  - In teams/companies, assigning roles based on the type of user is important and based on that said role, determining what permissions they have in accessing apis/data and manipulating data
- Encryption:
  - Restricting and preventing access from outside users is crucial in protecting the data from getting into the wrong hands at rest and in transit so encrypting the storage warehouses and communication between the API and warehouse is critical

** Performance and Cost **

- This was discussed before but as we are working with a relational database, indexing and partitioning the database is crucial for speed and efficiency
  - Indexing on Player/Game Ids - Partitioning on play by play types, leagues, game dates
- Transitioning over to a Cloud based database such as AWS RDS or DynamoDB could be beneficial over large scales of data and high API requests

** Data Quality **

- Data Cleaning
  - Crucial in keeping good quality data as this filters our noise, outliers, null/NA values, and provides accurate training data to models and analysis
- in doing this, setting pipelines for extracting, transforming and loading data to take the multitude of data sources and standardizing it into the form needed for our database warehouses purposes
- Consistent testing and data checks from software engineers in times of bugs and conflicts that need to be resolved
- Validate choices of data as reliable and factual as the introduction of faulty data and untruthful data invalidates the data as a whole

** Data Integrity **

To keep the data accurate and consistent throughout its history and future, data integrity practices should always be maintained:

- The use of consistent foreign keys is essential to depict the relationship between tables so the direction of information is understood
- Updating and manipulating data follows an update all or don't do anything procedure as failure to do so can cause faults in the tables in association with the change
- Data Back up and Recovery are crucial: in the midst of mistakes or disaster, having a reliable restore of information is critical
- Checksums and hash functions to verify data hasn't been corrupted or tampered with
  - In ingesting the data from different basketball sources, verifying that the data matches the original source data as the checksum of the origin and destination should match, and if not deny the ingestion
    - this same process follows for hash functions

** Robust ID System **

Using robust ID system for distinguishing between leagues, games, players, teams and plays from the play by play data is essential in ensuring accurate lookups, efficient processing and quicker accessing times

- First off, its important to global unique ids for leagues, games, players and teams because in the case of duplicate keys, there lacks the quality of our data and introduces conflicts when attempting to aggregate data
- GUIDs are important as they don't care what source the data comes from and in turn avoids conflicts of different data being represented by different IDs and super scalable as they don't risk collisions
- Ex: A team will be given its own id and regardless of what source that comes from, the data changes will be reflected on this one team

- ID Mapping for the different sources
  With each source having a different system for managing their data, it will be important to map a source to an ID to ensure that you are ingesting the correct changes for the correct entity
- Ex: Jeremy Lin has an ID of 1 on ESPN, 2 on NBA, 3 on NCAA (go Harvard) and 4 on Basketball Reference
  - Mapping each of these platforms to a common internal ID to make sure that the data goes to the right place which can be done with some scripting
- introducing a cross reference table to store new IDs when ingested just as another level of consistency and assurance that the data you are passing in is correct and being directed to the right location
  - This same procedure can be used for players, teams, and games
- Versioning Records:
  - Given the scope of how vast this data can get, introducing versioning to the data is important to reflecting the most recent updated data when records are updated on a game to game/ play to play basis
  - Given that versioning updates the data and reflects the most recent, its nice to have access to the past versions of the data for historical analysis and general backup if needed

Overall, there can be a lot to be said about the balances of performance vs cost, database design of ingesting multiple basketball sources on play by play data, quality, authentication and so on. By integrating a robust ID system with standardizing information from these sources, you can implement a fast and efficient structure that allows users of the warehouse and API to access their needed data accurately and securely. In addition, as the system grows more and more with greater capabilities, introducing cloud based databases could be crucial and ensure growth.

## Data Processing

When there are various streams of data processing, it is possible to discover that the play by play data and box score are not lining up correctly, its crucial to understand how to resolve the problem

** Error Detection **

- With the fact we have multiple streams of data that should be reporting the same data, the first thing we can integrate for validation is cross Source Validation, basically by comparing one piece of data with the same piece of data from other streams, we can determine where the discrepancy lies and send an alert for any discrepancy for further review
- Automated Comparison Checking:
  After a game, automatically run a test on the play by play data and the box score to determine where the issue lies - if the play by play data shows two events tha correlate in a player getting a steal and the box score say that one, the comparison checking would forwards an alert that there is an issue
- Lastly, we can also integrate a threshold for the whole system with automated checks, where if there are more than a certain percentage of issues and discrepancies with the processing, there must be an issue with the higher level and can be reviewed afterwards

** Delivery of Potentially Erroneous Information **

- Flagging and Alerting: As discussed before when discrepancies arise, its imperative to issue an indictor in the client and server side to understand where/why issues arise.
- In light of an issue, its important to proceed with sending the rest of the data aside from the steals, in cases where they want a full game report and the numbers, halting the process because of one stat issue isn't ideal as the customer most likely should have access to the rest of their requested data
  - It is also to set up versioning and options for the customer where they can ask for certain versions of data or lastly if they would want to wait for the resolved data
- This is more client side (I know the question asked for product side)
  - Although this is not ideal for the accuracy ensured from our end, being transparent with the clients is imperative in creating trust and communication and this can be done by providing indications on when issues arise, when they are being looked into and when they are resolved which can be done through customized alerts

** Error resolution **

With issues that arise, its always important to understand how to proceed with a proper resolution process to resolve conflicts

- Automated Resolution
  - With a steal, setting up automated review of plays around the surrounding steal can be a simple indicator to detect if said play was a steal or was not
  - Overall, setting up these checks for simple discrepancies followed by a way to fix them, whether that be from an algorithm or existing model
- Next, Manual Resolution: - in the instances with more severe discrepancies, having those discrepancies outputted to a page or dashboard is imperative in seeing "Ok what screwed up and why did it screw up" to allow the data engineering to review and understand the issues and proceed to resolve them
  - This can range from listing the game, players involved, game state, play type, sources involved
  - In cases where this is a consistent issue, submitting a review of the source data from the provider is important as well
    - Regardless, this can be an automated or manual process for discrepancies that arise because data providers need to be updated on the state of their products and data as well
- Lastly, once an issue is resolved, updating the existing database with the incorrect data to reflect the resolved issues and communicate this to the users to then continue accessing their data as expected

- With the knowledge and need to prevent this type of issue from happening again, we can also introduce machine learning or prediction algorithms to improve the detection of potential issues before they may arise which is based on previously recorded issues and play types that have previously caused discrepancies
- In addition we can provide avenues for users to report their findings and problems to us from maybe a report button or application
  - This not only provides transparency and user satisfaction but can also be helpful for us in making sure our data is as updated and correct as possible

Issues are always going to arise, unfortunately its not possible for our data to always be perfect, but we can do everything we can to get as close to that as possible. Through a structured and organized process we can resolve discrepancies efficiently through automation and manual review while also providing not only the our customers but also our providers with insight and knowledge on the issues at hand to decrease conflicts and improve reliability. Lastly, with delivering potentially erroneous data, we introduce trust, reliability and transparency across ShotQuality with an eagerness to deliver data as expected
