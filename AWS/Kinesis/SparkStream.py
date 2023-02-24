from pyspark import SparkConf, SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kinesis import KinesisUtils, InitialPositionInStream

# Configure o Spark
conf = SparkConf().setAppName("KinesisStreamExample")
sc = SparkContext(conf=conf)
ssc = StreamingContext(sc, batchInterval)

# Defina as credenciais da AWS e os detalhes do fluxo Kinesis
awsAccessKeyId = "your_access_key"
awsSecretKey = "your_secret_key"
streamName = "your_stream_name"
endpointUrl = "https://kinesis.us-west-2.amazonaws.com"

# Crie o fluxo de dados Kinesis
kinesisStream = KinesisUtils.createStream(
    ssc, streamName, endpointUrl, awsAccessKeyId, awsSecretKey,
    InitialPositionInStream.LATEST, batchInterval
)

# Faça o processamento dos dados do fluxo aqui
kinesisStream.foreachRDD(processData)

# Inicie o fluxo de dados
ssc.start()
ssc.awaitTermination()
