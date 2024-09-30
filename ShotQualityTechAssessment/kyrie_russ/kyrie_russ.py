import pandas as pd

csv_file = "nba_data_modeling_engineer.csv"

chunk_size = 10**6
filtered_data = []

# Loop through the file in chunks
for chunk in pd.read_csv(csv_file, chunksize=chunk_size):
    # Columns related to player names
    player_columns = chunk.columns[chunk.columns.str.contains("namePlayer", case=False)]

    # Filter for rows where any player column contains 'Kyrie Irving' or 'LeBron James'
    filtered_chunk_players = chunk[
        (
            chunk[player_columns].apply(
                lambda col: col.astype(str).str.contains("Kyrie Irving")
                | col.astype(str).str.contains("LeBron James")
            )
        ).any(axis=1)
    ]

    filtered_data.append(filtered_chunk_players)


filtered_df = pd.concat(filtered_data)

filtered_df.to_csv("filtered_kyrie_lebron_data.csv", index=False)
