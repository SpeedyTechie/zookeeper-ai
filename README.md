# Zookeeper
Zookeeper is an AI for managing Yahoo! Fantasy Football teams.

## Configuration
To start configuring Zookeeper, run zookeeper-ai.py. If it is the first time you have run Zookeeper, it will ask for a Client ID and Client Secret. To get this information you will have to [create an app on the Yahoo! Developer Network](https://developer.yahoo.com/apps/create). When creating the app, the 'Application Type' should be 'Installed Application'. For 'API Permissions', select 'Fantasy Sports'. Once you have created the app and entered your ID and Secret, Zookeeper will walk you through authorizing access to your Yahoo! account. Complete the process, and Zookeeper is now ready to do it's job.

If you previously configured Zookeeper, but would like to reset it, just delete data.txt.

## Using Zookeeper
To start using Zookeeper, simply run zookeeper-ai.py. For now, there's nothing else you can do. It currently will only return a JSON array containing the Yahoo! Fantasy Football position types. If you see the array, everything is configured properly.
