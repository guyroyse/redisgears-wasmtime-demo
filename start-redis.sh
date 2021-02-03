docker image pull redislabs/redismod

docker run \
  -p 6379:6379 \
  -v `pwd`/redis:/data \
  redislabs/redismod \
  --loadmodule /var/opt/redislabs/lib/modules/redisgears.so \
  --dir /data
