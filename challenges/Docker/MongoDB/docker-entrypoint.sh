#!/bin/bash

/usr/bin/mongod --fork --logpath /var/log/mongodb.log

/usr/bin/mongoimport --db servicesdb --collection restaurants --file /data/files/restaurant.json

tail -1000f /var/log/mongodb.log