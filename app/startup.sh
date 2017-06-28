# Start db
mongod --fork --logpath /var/log/mongod.log

# Run the import script
python scripts/import_data.py

# Run the web app
python doodle/doodle.py

