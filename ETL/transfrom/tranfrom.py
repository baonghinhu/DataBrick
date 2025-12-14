from pyspark.sql.functions import *
from pyspark.sql.types import *

df_pokemon = spark.read.table("workspace.clean_pokemon.pokedataset")
df_temp20 = spark.read.table("workspace.clean_pokemon.temp20")

# df_temp20 = df_temp20.withColumnRenamed('Sp.Atk','Attack')
df_temp20 = df_temp20.select(col('id').alias('id_temp20'),'Is_Mega','Is_Gmax','Form')
df = df_pokemon.join(df_temp20, df_pokemon.id == df_temp20.id_temp20, 'full')
df = df.withColumn(
    "rank",
    when(col("Total_Stats") >= 500, lit("Gold"))
    .when(col("Total_Stats") >= 400, lit("Silver"))
    .when(col("Total_Stats") >= 300, lit("Bronze"))
    .otherwise(lit("None"))
)

df.write.mode("overwrite") \
        .format('delta') \
        .option("mergeSchema", "true") \
        .saveAsTable("workspace.nghischemd.pokemon")

