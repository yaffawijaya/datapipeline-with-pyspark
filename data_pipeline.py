import ingest, transform, persist

import findspark
findspark.init()

import pyspark
import pyspark.sql
from pyspark.sql import SparkSession

class DataPipeline:
    def run_pipeline(self):
        print("Data pipeline with VIM")
        ingest_process = ingest.Ingest(self.spark)
        ingest_process.ingest_data()
        transform_process = transform.Transform()
        transform_process.transform_data()
        persist_process = persist.Presist()
        persist_process.presist_data()

        return
    
    def create_spark_session(self):
        self.spark = SparkSession.builder\
                    .appName("Data Pipeline")\
                    .enableHiveSupport()\
                    .getOrCreate()
                    

if __name__ == "__main__":
    pipeline = DataPipeline()
    pipeline.create_spark_session()
    pipeline.run_pipeline()
