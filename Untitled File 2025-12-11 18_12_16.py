from pyspark.sql.functions import *
from pyspark.sql.types import *

df = spark.read.table("samples.bakehouse.media_customer_reviews")

display(df)