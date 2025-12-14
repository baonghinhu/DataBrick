df  = spark.read \
    .format("csv") \
    .option('header', 'true') \
    .option('inferSchema', 'true') \
    .load('/Volumes/workspace/nghischemd/source/archive/pokeformslist.csv')
df = df.withColumnRenamed('_c0','id').drop('_c0')


df.write.mode("overwrite") \
        .option("mergeSchema", "true") \
        .format('delta') \
        .saveAsTable("workspace.clean_pokemon.pokeformslist")
