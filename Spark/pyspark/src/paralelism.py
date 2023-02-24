from pyspark import SparkConf, SparkContext

# configure Spark
conf = SparkConf().setAppName("My PySpark App")
conf = conf.setMaster("spark://<IP_ADDRESS_OF_MASTER_NODE>:7077")
conf = conf.set("spark.cores.max", "3") # use 3 machines in parallelism
conf = conf.set("spark.executor.memory", "1g") # use 1GB of memory per machine

# create Spark context
sc = SparkContext(conf=conf)

# perform Spark operations here
rdd = sc.parallelize([1, 2, 3, 4, 5])
print(rdd.sum())

# stop Spark context
sc.stop()

from pyspark import SparkConf, SparkContext

class PySparkApp:
    def __init__(self):
        # configure Spark
        self.conf = SparkConf().setAppName("My PySpark App")
        self.conf = self.conf.setMaster("spark://<IP_ADDRESS_OF_MASTER_NODE>:7077")
        self.conf = self.conf.set("spark.cores.max", "3") # use 3 machines in parallelism
        self.conf = self.conf.set("spark.executor.memory", "1g") # use 1GB of memory per machine

        # create Spark context
        self.sc = SparkContext(conf=self.conf)
        
    def run_app(self):
        # perform Spark operations here
        rdd = self.sc.parallelize([1, 2, 3, 4, 5])
        print(rdd.sum())

    def stop_app(self):
        # stop Spark context
        self.sc.stop()

if __name__ == "__main__":
    app = PySparkApp()
    app.run_app()
    app.stop_app()
