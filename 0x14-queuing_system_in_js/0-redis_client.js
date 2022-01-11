import redis from 'redis';
const client = redis.createClient();

client.on('error', function(error) {
  console.error(`Redis client not connected to the server: ${error}`);
});

client.on('connect', function(error) {
  console.error('Redis client connected to the server');
});
