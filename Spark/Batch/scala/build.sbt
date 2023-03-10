name := "Spark Streaming With Kafka"

version := "1.0"

scalaVersion := "2.12.15"

libraryDependencies += "org.apache.spark" %% "spark-core" % "3.2.0"
libraryDependencies += "org.apache.spark" %% "spark-sql" % "3.2.0" % "provided"

<dependency>
      <groupId>org.apache.spark</groupId>
      <artifactId>spark-sql-kafka-0-10_2.11</artifactId>
      <version>2.4.0</version>
</dependency>