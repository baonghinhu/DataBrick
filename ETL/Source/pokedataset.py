from pyspark.sql.functions import *
from pyspark.sql.types import *

df  = spark.read \
    .format("csv") \
    .option('header', 'true') \
    .load("/Volumes/workspace/nghischemd/source/archive/pokedataset.csv")
df = df.withColumnRenamed('Height(m)', 'Height')
df = df.withColumnRenamed('Weight{kg}', 'Weight')

df.write.mode("overwrite").saveAsTable("workspace.clean_pokemon.pokedataset")
