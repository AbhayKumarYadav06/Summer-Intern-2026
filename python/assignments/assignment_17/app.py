from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder.appName("SalesApp").getOrCreate()

df = spark.read.csv("sales.csv", header=True, inferSchema=True)

# Sort
sorted_df = df.orderBy(col("sales").desc())
print("Sorted Data")
sorted_df.show()

# Top 3
print("Top 3 Products")
sorted_df.limit(3).show()

# Filter
filtered_df = df.filter(col("sales") > 80000)
filtered_df.show()

# Save output
filtered_df.write.mode("overwrite").csv("output/high_sales", header=True)

spark.stop()