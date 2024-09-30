import pandas as pd
import numpy as np
import sklearn.linear_model as LinearRegression

csv_file = "nba_data_modeling_engineer.csv"

chunk_size = 10**6


filtered_data = []

# Loop through the file in chunks and filter for the Knicks and Nets
# As this involves Kevin Durants last team and future team, it only makes sense to only
# focus on play data of these teams
for chunk in pd.read_csv(csv_file, chunksize=chunk_size):
    # Filter for rows where the team is either 'Knicks' or 'Nets'
    team_columns = chunk.columns[chunk.columns.str.contains("Team", case=False)]
    player_team_columns = chunk.columns[
        chunk.columns.str.contains("teamPlayer1", case=False)
    ]

    # Filter for rows where any of the team columns contain 'NYK' or 'BKN'
    filtered_chunk = chunk[
        (
            chunk[team_columns].apply(
                lambda col: col.astype(str).str.contains("NYK")
                | col.astype(str).str.contains("BKN")
            )
        ).any(axis=1)
    ]
    # filtered_chunk_with_score = filtered_chunk[
    #     filtered_chunk["slugScore"].apply(lambda x: isinstance(x, str))
    # ]

    # double check
    filter_no_players = filtered_chunk[
        filtered_chunk["namePlayer1"].apply(lambda x: isinstance(x, str))
    ]

    # Examine misses
    filter_knicks_nets_shooting = filter_no_players[
        (
            chunk[player_team_columns].apply(
                lambda col: col.astype(str).str.contains("NYK")
                | col.astype(str).str.contains("BKN")
            )
        ).any(axis=1)
    ]

    filtered_chunks_shooting_events = filter_knicks_nets_shooting[
        filter_knicks_nets_shooting["numberEvent"] > 2
    ]

    # Append the filtered chunk to the list
    filtered_data.append(filtered_chunks_shooting_events)

filtered_df = pd.concat(filtered_data)

# Save the filtered data to a new CSV file
filtered_df.to_csv("filtered_KD_data.csv", index=False)
