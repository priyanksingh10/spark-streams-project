# Spark Structured Streaming Project

1. How did changing values on the SparkSession property parameters affect the throughput and latency of the data?
    ### For configuration 1: 
        maxOffsetsPerTrigger - 30
        core - 2
        spark.executor.memory - 8g
        spark.driver.memory - 8g

    ### Results for configuration 1:
        numInputRows : 29
        inputRowsPerSecond : 0.48333333333333334
        processedRowsPerSecond : 3.702285203625686
        Below are number from stage 3 of DAG
        Peak Execution Memory: 32.8 MB
        Task Time: 10s
        Max GC Time: 29ms
        Max Scheduler Delay: 17 ms

    ### For configuration 2: 
        maxOffsetsPerTrigger - 200
        core - 2
        spark.executor.memory - 8g
        spark.driver.memory - 8g

    ### Results for configuration 2:
        numInputRows : 199
        inputRowsPerSecond : 11.098098265573586
        processedRowsPerSecond : 16.939053455907388
        Below are number from stage 3 of DAG
        Peak Execution Memory: 32.8 MB
        Task Time: 12s
        Max GC Time: 24ms
        Max Scheduler Delay: 10 ms

    ### For configuration 3:
        maxOffsetsPerTrigger - 200
        core - 4
        spark.executor.memory - 8g
        spark.driver.memory - 8g

    ### Results for configuration 3:
        numInputRows : 199
        inputRowsPerSecond : 8.098098265573586
        processedRowsPerSecond : 17.425925923625686
        Below are number from stage 3 of DAG:
        Peak Execution Memory: 16.8 MB
        Task Time: 25s
        Max GC Time: 23ms
        Max Scheduler Delay: 36 ms

    ### For configuration 4:
        maxOffsetsPerTrigger - 200
        core - 10
        spark.executor.memory - 8g
        spark.driver.memory - 8g

    ### Results for configuration 4:
        numInputRows : 199
        inputRowsPerSecond : 3.65412512165115
        processedRowsPerSecond : 18.425925925925924
        Below are number from stage 3 of DAG:
        Peak Execution Memory: 8.8 MB
        Task Time: 53s
        Max GC Time: 20ms
        Max Scheduler Delay: 18 ms



2. What were the 2-3 most efficient SparkSession property key/value pairs? 
Through testing multiple variations on values, how can you tell these were the most optimal?

    - The most effient value during my 6 runs were the once related to maxoffsetsize of 200 with 2 cores (numbers above) (maxOffsetsPerTrigger size kept 200 for all configurations)

    -  The memory consumption for the job was stable and would decrease with increasing number of cores. The Peak Execution memory never went above 32.8 MB for 200 offset count with 2 cores. For more than 2 cores, the memory usage went down for the same offset number configuration, but the tasks took more time almost 2 times when core was doubled and 4 times for 10 cores. From the data above, it seems that with more cores, the time taken for task serialization increased significantly which increased the total task execution time. Even repartitioning the RDD didn't have much impact on the performance for 4 cores or 10 cores for this offset.