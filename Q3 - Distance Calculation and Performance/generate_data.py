import pandas as pd
import uuid
import random
import numpy as np

# Function to generate a large dataset with multiple plays and players
def generate_large_dataset(num_plays, num_players, num_entries_per_play, stationary_ratio=0.2):
    """
    :param num_plays: Number of unique plays (playid)
    :param num_players: Number of players per play (playerid)
    :param num_entries_per_play: Number of entries (time samples) per player per play
    :param stationary_ratio: Fraction of players in each game who move very little or stay stationary
    :return: A DataFrame simulating the dataset
    """
    
    for num in range(num_plays):
        data = []
        print(num)
        playid = str(uuid.uuid4())
        stationary_players = random.sample(range(num_players), int(stationary_ratio * num_players))
        
        for playerid in range(num_players):
            time = 0
            x_start = random.uniform(70.0, 80.0)
            y_start = random.uniform(50.0, 60.0)
            
            for entry in range(num_entries_per_play):
                if playerid in stationary_players:
                    # Stationary or slightly moving players: small variations in X and Y
                    x_ft = x_start + random.uniform(-0.05, 0.05)
                    y_ft = y_start + random.uniform(-0.05, 0.05)
                else:
                    # Moving players: larger random movements
                    x_ft = x_start + random.uniform(-5.0, 5.0)
                    y_ft = y_start + random.uniform(-5.0, 5.0)
                
                time_sec = np.round(time, 6)
                time += random.uniform(0.01, 0.1)
                data.append([playid, playerid, x_ft, y_ft, time_sec])

    # Creating the DataFrame
    df = pd.DataFrame(data, columns=['playid', 'playerid', 'X_ft', 'Y_ft', 'time_sec'])
    df.to_csv("Data/player_data_"+str(num)+".csv")
        
    return df

# Generate a dataset with 100 plays, 10 players per play, and 50 entries per player
df = generate_large_dataset(num_plays=5000, num_players=20, num_entries_per_play=50)

# # Save the generated dataset to a CSV file
# df.to_csv('player_coordinate_dataset.csv', index=False)

# print("Dataset generated and saved as 'large_dataset.csv'")
