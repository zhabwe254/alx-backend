import { promisify } from 'util';
import redis from 'redis';

const client = redis.createClient();
client.on('connect', () => {
    console.log('Redis client connected to the server');
});
client.on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err.message}`);
});

const getAsync = promisify(client.get).bind(client);

async function displaySchoolValue(schoolName) {
    const value = await getAsync(schoolName);
    console.log(value);
}

function setNewSchool(schoolName, value) {
    client.set(schoolName, value, redis.print);
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
