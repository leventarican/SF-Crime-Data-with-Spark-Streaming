> How did changing values on the SparkSession property parameters affect the throughput and latency of the data?

Better _processed rows per second_ performance.

> What were the 2-3 most efficient SparkSession property key/value pairs? Through testing multiple variations on values, how can you tell these were the most optimal?

Setting SparkSession config `spark.sql.shuffle.partitions` from default value `200` to `10` was efficient. The number of processed row increased ~ 4-5 times. Whereas `spark.executor.memory` with 8g has no effect.
\
Also `spark.broadcast.checksum` or `spark.storage.memoryMapThreshold` seems to have small effects.
\
https://spark.apache.org/docs/latest/sql-performance-tuning.html
https://spark.apache.org/docs/latest/configuration.html
