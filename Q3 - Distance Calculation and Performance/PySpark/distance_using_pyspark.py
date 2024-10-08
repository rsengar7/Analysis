from pyspark.sql import SparkSession
from pyspark.sql.window import Window
import pyspark.sql.functions as F
import math
import time

# Create a Spark session
spark = SparkSession.builder.appName("Distance_Speed_Calculation").getOrCreate()

# Start time to measure the execution time of the process
start = time.time()

def calculate_distance_speed(df):
    """
    Function to calculate distance and speed in PySpark
    Args:
        df (DataFrame): A PySpark DataFrame containing player coordinates and timestamps.
    Returns:
        DataFrame: A DataFrame containing the total distance and average speed for each player during each play.
    """

    # Define a window specification to partition data by playid and playerid, and order by time_sec.
    # This will be used for calculating values like lagged X_ft, Y_ft, and time_sec for each player in each play.
    window_spec = Window.partitionBy("playid", "playerid").orderBy("time_sec")

    # Calculate lagged values for X_ft, Y_ft, and time_sec using the window specification.
    # These will be used to calculate the distance between consecutive points.
    df = df.withColumn("X_shift", F.lag("X_ft").over(window_spec))
    df = df.withColumn("Y_shift", F.lag("Y_ft").over(window_spec))
    df = df.withColumn("time_shift", F.lag("time_sec").over(window_spec))

    # Calculate the Euclidean distance between consecutive points (X, Y) using the Pythagorean theorem.
    df = df.withColumn("distance", 
                       F.sqrt(F.pow(F.col("X_ft") - F.col("X_shift"), 2) + 
                              F.pow(F.col("Y_ft") - F.col("Y_shift"), 2)))
    
    # Fill any null values (which occur due to the lag function) in the distance column with 0.
    df = df.fillna({'distance': 0})

    # Calculate the total distance covered by each player during each play by summing the 'distance' column.
    total_distance = df.groupBy("playid", "playerid").agg(F.sum("distance").alias("total_distance"))

    # Calculate the total time spent by each player during each play by subtracting the minimum time from the maximum time.
    total_time = df.groupBy("playid", "playerid").agg((F.max("time_sec") - F.min("time_sec")).alias("total_time"))

    # Join the total_distance and total_time DataFrames to combine both metrics.
    result = total_distance.join(total_time, on=["playid", "playerid"])

    # Calculate the average speed in meters per second by dividing total distance by total time.
    # The conversion factor (0.3048) is used to convert feet to meters.
    result = result.withColumn("avg_speed_mps", (F.col("total_distance") / F.col("total_time")) * 0.3048)

    # Handle any division by zero errors by replacing null or infinite values with 0.
    result = result.withColumn("avg_speed_mps", F.when(F.col("avg_speed_mps").isNull(), 0).otherwise(F.col("avg_speed_mps")))

    return result

# Load the CSV file into a PySpark DataFrame
# Args:
#     file_path (str): Path to the CSV file containing player coordinate data.
# Header and inferSchema are set to True for automatic schema inference.
file_path = 'player_coordinate_dataset.csv'  # Replace with your file path

df = spark.read.csv(file_path, header=True, inferSchema=True)

# Repartition the DataFrame based on 'playid' to optimize parallel processing for larger datasets.
df = df.repartition("playid")

# Apply the distance and speed calculation function on the DataFrame.
result = calculate_distance_speed(df)

# Show the results (or save the results to a file)
# result.show()  # This will display the result

# Save the resulting DataFrame to a CSV file, with headers included.
result.write.csv('player_distances_speeds', header=True)

# End time for measuring the total execution time of the process.
end = time.time()

# Print the total time taken for the entire process.
print("Time : ", end - start)
