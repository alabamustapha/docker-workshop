## Queries 

```SQL
CREATE OR REPLACE EXTERNAL TABLE `ny_taxis.external_yellow_tripdata`
OPTIONS (
  format="PARQUET",
  uris=[
    "gs://dezoomcamp_hw3_2026-xyz/yellow_tripdata_2024-01.parquet", "gs://dezoomcamp_hw3_2026-xyz/yellow_tripdata_2024-02.parquet",
    "gs://dezoomcamp_hw3_2026-xyz/yellow_tripdata_2024-03.parquet", "gs://dezoomcamp_hw3_2026-xyz/yellow_tripdata_2024-04.parquet",
    "gs://dezoomcamp_hw3_2026-xyz/yellow_tripdata_2024-05.parquet", "gs://dezoomcamp_hw3_2026-xyz/yellow_tripdata_2024-06.parquet"
    ]
);


SELECT * from `ny_taxis.external_yellow_tripdata` LIMIT 10;


CREATE OR REPLACE TABLE `ny_taxis.yellow_tripdata` AS
SELECT * 
FROM `ny_taxis.external_yellow_tripdata`;


SELECT COUNT(*) FROM `ny_taxis.yellow_tripdata`;

SELECT COUNT(*) FROM `ny_taxis.external_yellow_tripdata`;

SELECT COUNT(DISTINCT PULocationID) FROM `ny_taxis.yellow_tripdata`;

SELECT COUNT(DISTINCT PULocationID) FROM `ny_taxis.external_yellow_tripdata`;


SELECT PULocationID FROM `ny_taxis.yellow_tripdata`;

SELECT PULocationID, DOLocationID  FROM `ny_taxis.yellow_tripdata`;

SELECT COUNT(1) FROM  `ny_taxis.yellow_tripdata` WHERE `fare_amount` = 0;


CREATE OR REPLACE TABLE `ny_taxis.yellow_tripdata_optimized`
PARTITION BY DATE(tpep_dropoff_datetime)
CLUSTER BY VendorID
AS
SELECT *
FROM `ny_taxis.external_yellow_tripdata`;


SELECT 
  DISTINCT VendorID 
  FROM `ny_taxis.yellow_tripdata_optimized` 
  WHERE 
    DATE(tpep_dropoff_datetime) >= '2024-03-01' AND 
    DATE(tpep_dropoff_datetime) <= '2024-03-15';

SELECT 
  DISTINCT VendorID 
  FROM `ny_taxis.yellow_tripdata` 
  WHERE 
    DATE(tpep_dropoff_datetime) >= '2024-03-01' AND 
    DATE(tpep_dropoff_datetime) <= '2024-03-15';

SELECT 
  COUNT(*)
  FROM `ny_taxis.yellow_tripdata_optimized`; 
  

```