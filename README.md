# Data Pipeline Project
This is my learning documentation for making data pipeline using PySpark

## Overview

This project implements a data pipeline using Apache Spark. The pipeline involves three main stages:

1. **Ingest**: Loading data from various sources.
2. **Transform**: Processing and transforming the ingested data.
3. **Persist**: Storing the transformed data for further use.

## Setup and Installation

### 1. Python Environment

Ensure that you have a Python environment with PySpark installed. You can set up a Conda environment with PySpark using the following commands:

```powershell
conda create -n spark python=3.10
conda activate spark
pip install pyspark
```

### 2. Set Up Environment Variable
Configure the Python executable path for PySpark by setting the PYSPARK_PYTHON environment variable. This ensures Spark uses the Python interpreter from your Conda environment.

For Windows
Open Command Prompt or PowerShell and run:

```powershell
set PYSPARK_PYTHON=C:\Users\<username>\Anaconda3\envs\spark\python.exe
```
To set this variable permanently:

Right-click on 'This PC' or 'Computer' on the desktop or File Explorer.
Select 'Properties'.
Click on 'Advanced system settings'.
Click the 'Environment Variables' button.
Add a new user or system variable with the following details:
Variable name: PYSPARK_PYTHON
Variable value: C:\Users\<username>\Anaconda3\envs\spark\python.exe

### 3. Running the Pipeline
To run the Spark job, use the spark-submit command. Make sure to replace data_pipeline.py with the path to your script if it's located elsewhere.

bash
Copy code
```powershell
spark-submit --master local[*] --deploy-mode client --num-executors 5 --executor-memory 4g --executor-cores 2 --conf spark.sql.shuffle.partitions=200 --conf spark.pyspark.python=C:\Users\yaffa\Anaconda3\envs\spark\python.exe data_pipeline.py
```

Explanation of Parameters
1. **--master local[*]**: Runs Spark locally with as many worker threads as logical cores on your machine.
2. **--deploy-mode client**: Runs the Spark driver program on the client machine.
3. **--num-executors 5**: Number of executor instances.
4. **--executor-memory 4g**: Amount of memory per executor.
5. **--executor-cores 2**: Number of cores per executor.
6. **--conf spark.sql.shuffle.partitions=200**: Number of partitions to use when shuffling data for joins or aggregations.
7. **--conf spark.pyspark.python**=C:\Users\<username>\Anaconda3\envs\spark\python.exe: Path to the Python executable to use for PySpark.
