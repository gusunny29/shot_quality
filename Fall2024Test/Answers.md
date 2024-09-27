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



        ** Model Selection **


        ** Model Training **



        ** Model Maintenance **




        ** Production Workflow **




        ** Hardware Constraints **

** Database **

** Data Processing **
