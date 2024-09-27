import pandas as pd
import numpy as np

csv_file = "nba_data_modeling_engineer.csv"

chunk_size = 10**6


filtered_data = []

# Loop through the file in chunks and filter for the Knicks and Nets
# As this involves Kevin Durants last team and future team, it only makes sense to only
# focus on play data of these teams
for chunk in pd.read_csv(csv_file, chunksize=chunk_size):
    # Filter for rows where the team is either 'Knicks' or 'Nets'
    filtered_chunk = chunk[
        (chunk["slugTeamHome"] == "NYK")
        | (chunk["slugTeamHome"] == "BKN")
        | (chunk["slugTeamAway"] == "NYK")
        | (chunk["slugTeamAway"] == "BKN")
    ]

    # Append the filtered chunk to the list
    filtered_data.append(filtered_chunk)

filtered_df = pd.concat(filtered_data)

# Save the filtered data to a new CSV file
filtered_df.to_csv("filtered_KD_data.csv", index=False)
