import pyspark
import pyspark.sql
from pyspark.sql import SparkSession
from pyspark.sql.types import *

class Ingest:
    def __init__(self, spark):
        self.spark = spark

    def ingest_data(self):
        print("Ingesting data...")
        my_list = [('a', 1), ('b', 2), ('c', 3)]
        df = self.spark.createDataFrame(my_list, ['letter', 'number'])
        df.show()