## ETL Process for Updating Target Table from Multiple Data Sources

This task is all about setting up an ETL (Extract, Transform, Load) pipeline that takes data from three different sources (Sales, Inventory, and Product) and brings it all together into a single target table. The idea is to make sure the data is always up-to-date, even when the sources update at different rates.

### Architecture Overview

This system integrates data from three different sources: Sales, Inventory, and Product. These sources are combined into a central table in Snowflake called product_performance, ensuring the target table is always up to date with the latest information from each source.

- Architecture Diagram : 
[Architecture Diagram of the Process](https://github.com/rsengar7/Analysis/blob/main/Q4%20-%20System%20Design/Screenshots/ETL.drawio.png)

### Steps in the ETL Process
1. Data Ingestion from OLTP to OLAP system
2. Data Processing
3. Orchestration to process data changes at different rates
4. Use an updated Target Table for Business Analysis, Visualization or Machine Learning models.
5. Error Handling and Logging
