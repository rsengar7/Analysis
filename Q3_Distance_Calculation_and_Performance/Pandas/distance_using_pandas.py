import pandas as pd
import numpy as np
import time

# Start time to measure the execution time of the process
start = time.time()

def calculate_distance_speed(df):
    """
    Function to calculate distance and speed in a pandas DataFrame
    Args:
        df (DataFrame): A pandas DataFrame containing player coordinates and timestamps.
    Returns:
        DataFrame: A DataFrame containing the total distance and average speed for each player during each play.
    """
    
    # Sorting the data by 'playid', 'playerid', and 'time_sec' to ensure calculations happen in correct time order
    df = df.sort_values(by=['playid', 'playerid', 'time_sec'])
    
    # Shift the X, Y, and time columns to calculate differences between consecutive points
    # Group by 'playid' and 'playerid' to shift within each player's play session
    df['X_shift'] = df.groupby(['playid', 'playerid'])['X_ft'].shift(1)
    df['Y_shift'] = df.groupby(['playid', 'playerid'])['Y_ft'].shift(1)
    df['time_shift'] = df.groupby(['playid', 'playerid'])['time_sec'].shift(1)
    
    # Calculate the Euclidean distance between consecutive points using the distance formula
    df['distance'] = np.sqrt((df['X_ft'] - df['X_shift'])**2 + (df['Y_ft'] - df['Y_shift'])**2)
    
    # For the first point in each group (where no previous point exists), fill the distance as 0
    df['distance'].fillna(0, inplace=True)
    
    # Calculate the total distance run by each player during each play by summing the distances
    total_distance = df.groupby(['playid', 'playerid'])['distance'].sum().reset_index(name='total_distance')
    
    # Calculate the total time spent by each player during each play (difference between max and min time)
    total_time = df.groupby(['playid', 'playerid'])['time_sec'].apply(lambda x: x.max() - x.min()).reset_index(name='total_time')
    
    # Merge the total distance and total time DataFrames to combine both metrics
    result = pd.merge(total_distance, total_time, on=['playid', 'playerid'])
    
    # Calculate the average speed in meters per second by dividing total distance by total time
    # The conversion factor (0.3048) is used to convert feet to meters
    result['avg_speed_mps'] = (result['total_distance'] / result['total_time']) * 0.3048
    
    # Replace any infinite or NaN values with 0 in cases where total_time might be 0 (to avoid division by zero)
    result.replace([np.inf, -np.inf], 0, inplace=True)
    result['avg_speed_mps'].fillna(0, inplace=True)
    
    return result

# Load the large dataset from a CSV file into a pandas DataFrame
# Args:
#     file_path (str): Path to the CSV file containing player coordinate data.
file_path = 'player_coordinate_dataset.csv'  # Replace this with your actual file path

df = pd.read_csv(file_path)

# Apply the distance and speed calculation function on the DataFrame
result = calculate_distance_speed(df)

# Output the result to a CSV file or print the results
# Save the result DataFrame to a CSV file with headers
result.to_csv('player_distances_speeds.csv', index=False)
print("Results saved to 'player_distances_speeds.csv'")

# End time for measuring the total execution time of the process
end = time.time()

# Print the total time taken for the entire process
print("Time : ", end - start)
