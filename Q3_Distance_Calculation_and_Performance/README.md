## Player Distance and Speed Calculation

### Overview

This section contains two scripts—one in Pandas and the other in PySpark—designed to calculate how far players run during a play and their average speed based on X and Y coordinates on the field. The dataset is structured around multiple plays and players, with each player's position recorded at different points in time.

For large datasets, performance optimization is critical. The provided solutions compare both a Pandas and a PySpark implementation, demonstrating how PySpark outperforms Pandas when handling large-scale data (e.g., datasets with over 80 million rows).

### Features
- Calculate the total distance each player runs during a play.
- Compute the average speed (in meters per second) of each player.
- Efficiently handle large datasets with both Pandas and PySpark solutions.

### Calculate Distance using Euclidean Distance Formula
Euclidean distance is a mathematical concept that measures the straight-line distance between two points in a Euclidean space. It is named after the ancient Greek mathematician Euclid, who is often referred to as the "father of geometry". The formula for calculating Euclidean distance is based on the Pythagorean Theorem and can be expressed as:

$$d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$$

The Euclidean distance formula is used to calculate the straight-line distance between two points on a 2D plane, based on their x and y coordinates. It measures how far apart the two points are by taking the square root of the sum of the squared differences between their x and y values.

### Python (Pandas) Implementation

The pandas script is designed to handle moderate-sized datasets and lag with big data:
- Sorting the data based on playid, playerid, and time_sec.
- Calculating the Euclidean distance between consecutive player positions.
- Summing the total distance and calculating the average speed by dividing total distance by total time.

This solution is suitable for datasets that fit into memory. It may become slow or impractical when scaling to large datasets, e.g., millions of rows.

### PySpark Implementation

The pyspark script provides a more scalable solution by leveraging distributed computing, making it ideal for big data applications.
- Lag functions are used to calculate the differences in X, Y coordinates and time.
- The Euclidean distance is computed between consecutive player positions.
- PySpark efficiently processes large datasets using partitioning and distributed computation.

The PySpark solution is designed for big data environments. Testing with datasets of 80 million rows demonstrated its efficiency and scalability, with significant improvements over the Pandas solution in terms of execution time and resource handling.

### Performance Comparison
We processed a dataset containing 80 million rows to compare the performance of both implementations:
- Pandas: While efficient for small datasets, Pandas struggled with larger datasets, leading to increased memory consumption and longer execution times.
- PySpark: Demonstrated significant improvements in execution time and scalability, particularly for larger datasets.

### Conclusion
In conclusion, PySpark is more efficient and better suited for handling large datasets, especially when scaling to millions of rows.
