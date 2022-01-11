import redis from 'redis';
const client = redis.createClient();

client.on('error', function(error) {
  console.error(`Redis client not connected to the server: ${error}`);
});

client.on('connect', function(error) {
  console.error('Redis client connected to the server');
});

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, redis.print);
}

function displaySchoolValue(schoolName) {
  client.get(schoolName, function(err, reply) {
    console.log(reply);
  });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
