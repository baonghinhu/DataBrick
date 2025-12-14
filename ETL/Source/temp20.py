df  = spark.read \
    .format("csv") \
    .option('header', 'true') \
    .option('inferSchema', 'true') \
    .load('/Volumes/workspace/nghischemd/source/archive/temp20.csv')

df.display()


df.write.mode("overwrite") \
        .option("mergeSchema", "true") \
        .format('delta') \
        .saveAsTable("workspace.clean_pokemon.temp20")
