

def pipeline(args):
    from pyspark.sql import SparkSession
    from utils.gcp.get_files import smart
    spark = SparkSession \
        .builder \
        .appName("pipeline") \
        .getOrCreate()
    
    files = smart(args['source'])
    data = spark.read.format("avro").load(files)
    data = cleaning(data)
    data = encrypt(data)
    data = profiling(data)
    data.write(arg['sink'])
    
    
    pass