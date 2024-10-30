python -m  pipreqs.pipreqs --force .

# Initialize migrations (only run this once)
flask db init

# Create a migration script (run this after each model change)
flask db migrate -m "Describe your changes"

# Apply migrations to the database
flask db upgrade

# Roll back the latest migration if needed
flask db downgrade
