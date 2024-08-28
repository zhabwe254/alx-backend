Redis Setup on macOS
This guide provides detailed instructions on installing and running Redis on macOS using Homebrew, along with basic usage commands.

Table of Contents
Prerequisites
Installation
Install Homebrew
Install Redis
Start Redis
Verify Installation
Basic Usage
Setting and Getting a Key-Value
Stopping Redis
Redis Dump
Basic Redis Commands
License
Prerequisites
Before proceeding with Redis installation, ensure the following:

You are on macOS.
Homebrew (the macOS package manager) is installed.
Installation
Install Homebrew
If Homebrew is not installed, open your terminal and execute the following command to install it:

bash
Copy code
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
Install Redis
Once Homebrew is installed, install Redis by running:

bash
Copy code
brew install redis
Start Redis
You can start Redis either as a service or in the background.

To start Redis as a service, use:

bash
Copy code
brew services start redis
Alternatively, to run Redis in the background:

bash
Copy code
redis-server &
Verify Installation
Once Redis is running, check if it is working properly by pinging the server:

bash
Copy code
redis-cli ping
If the installation is successful, the response should be:

bash
Copy code
PONG
Basic Usage
Setting and Getting a Key-Value
Set a key-value pair in Redis:
bash
Copy code
redis-cli set Holberton School
Retrieve the value for the key Holberton:
bash
Copy code
redis-cli get Holberton
The output should display:

bash
Copy code
"School"
Stopping Redis
To stop the Redis server, run:

bash
Copy code
brew services stop redis
If you started Redis with redis-server &, use the following commands to stop it:

List the running Redis processes:
bash
Copy code
ps aux | grep redis-server
Terminate the process:
bash
Copy code
kill <PID_of_redis-server>
Redis Dump
The Redis dump file, dump.rdb, is located in /usr/local/var/db/redis/ on macOS. To utilize the dump file in your project:

Copy the dump.rdb file to your project folder:
bash
Copy code
cp /usr/local/var/db/redis/dump.rdb /path/to/your/project/
This file will contain the saved state of your Redis database.

Basic Redis Commands
Here are some fundamental Redis commands to use:

SET <key> <value>: Set the value of a key.
GET <key>: Retrieve the value of a key.
DEL <key>: Remove the specified key from Redis.
PING: Check if the Redis server is responsive.
FLUSHALL: Clear the entire Redis database.
For a more comprehensive list of commands, refer to the Redis documentation.
