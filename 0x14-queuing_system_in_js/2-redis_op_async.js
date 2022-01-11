import redis from 'redis';
import { promisify } from 'util';

const client = redis.createClient();

const clientGetAsync = promisify(client.get).bind(client);

client.on('error', function(error) {
  console.error(`Redis client not connected to the server: ${error}`);
});

client.on('connect', function(error) {
  console.error('Redis client connected to the server');
});

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, redis.print);
}

async function displaySchoolValue(schoolName) {
  console.log(await clientGetAsync(schoolName));
}

(async () => {
  await displaySchoolValue('Holberton');
  await setNewSchool('HolbertonSanFrancisco', '100');
  await displaySchoolValue('HolbertonSanFrancisco');
})();
