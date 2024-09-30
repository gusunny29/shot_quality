import pandas as pd
import numpy as np

csv_file = "nba_data_modeling_engineer.csv"

chunk_size = 10**6
filtered_data = []

# Loop through the file in chunks
for chunk in pd.read_csv(csv_file, chunksize=chunk_size):
    # Filter for rows where the team is either 'Hawks' or 'Spurs' (for Murray's and Young's teams)
    team_columns = chunk.columns[chunk.columns.str.contains("Team", case=False)]
    player_columns = chunk.columns[chunk.columns.str.contains("namePlayer", case=False)]

    # Filter for rows where any of the team columns contain 'ATL' (Hawks) or 'SAS' (Spurs)
    filtered_chunk = chunk[
        (
            chunk[team_columns].apply(
                lambda col: col.astype(str).str.contains("ATL")
                | col.astype(str).str.contains("SAS")
            )
        ).any(axis=1)
    ]

    # Filter for rows where any player column contains 'Dejounte Murray' or 'Trae Young'
    filtered_chunk_players = filtered_chunk[
        (
            chunk[player_columns].apply(
                lambda col: col.astype(str).str.contains("Dejounte Murray")
                | col.astype(str).str.contains("Trae Young")
            )
        ).any(axis=1)
    ]

    # Optionally filter for specific event types (e.g., shooting events)
    filtered_events = filtered_chunk_players[
        filtered_chunk_players["numberEvent"]
        > 2  # Replace with your specific event filter if needed
    ]

    # Append the filtered chunk to the list
    filtered_data.append(filtered_events)

# Concatenate all chunks into one DataFrame
filtered_df = pd.concat(filtered_data)

# Save the filtered data to a new CSV file
filtered_df.to_csv("filtered_murray_young_data.csv", index=False)
