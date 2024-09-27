# Fall 2024 Technical Assessment

** Modeling **

    Given you have access to play by plays for all professional leagues globally, the wide range of available data gives us a lot of variety in creating a model for predicting if a shot is made in the Euroleague

    How would you approaching the modeling question?
        This problem can be classified into a binary classification problem where each shot attempt has two outcomes: the shot is made (we can represent that result with a 1) or the shot being missed (represented as 0).

        Inputs: X = [play by play game data, location data represented with x and y coordinates]
        Target Variable: Y = [shot_made]


        For our play by play data I think the besst features to include into our input should include:
            - Defensive distancing from the shot taker
            - Type of shot (layup, dunk, mid-range, 3 pointer, etc)
            - Player details (Shot selection patternm, position, usage)
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
                - Of course if there are more defenders with similar "pressure" levels to the shooter can definitely decrease liklihood of shot makes
            - Distance of shooter to the basket
            - Angle of shooter to the basket

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
            - Begin by applying a Logistical Regression model to develop some beginning understanding of how relevant some features are but then
            using a Random Forest model as this relationship isn't necessarily linear so models such as Linear Regression wouldn't provide much
            information on the goal at hand
            - Decision Tree models in this case would be super helpful as it provides us with a clear understanding of "Player A took X shot, did he make it or did he miss it" and with the data we have, we can move towards determining which shots were higher percentage vs lower percentage
            - XGBoost definitely can play a role in handling as large of a data set and as a tree based model, it has existing ways of handling missing values and hypertuning capabilities which can filter for more reliable data.
                - This method is also very common within sports analytics and can provide us with insights as to whcih features contribute most to a players performance and ability to make shots

        ** Model Training **
            - Oversampling/Undersampling: In basketball, the range of shot selection definitely isn't equal (but to be fair in the past decade 3 pointers definitely have sky rocketed in percentage of shots taken), so its important to utilize both processes when needed to introduce balance between the majority and the minority class, whether that includes too many layups being taken into account or too few 3 above the arch 3s, this is a crucial component in providing "reliable" data
            - Cross Validation: Given the large range of the data set, using cross validation can be considered because



        ** Model Maintenance **




        ** Production Workflow **




        ** Hardware Constraints **

** Database **

** Data Processing **
