import pg8000

# Connect to default postgres database
conn = pg8000.connect(
    host="localhost",
    port=5432,
    user="postgres",
    password="1111",
    database="postgres"
)

# Set autocommit to create database
conn.autocommit = True

cursor = conn.cursor()

# Check if database exists
cursor.execute("SELECT 1 FROM pg_database WHERE datname = 'demo_alembic_db'")
exists = cursor.fetchone()

if exists:
    print("Database 'demo_alembic_db' already exists")
else:
    # Create database
    cursor.execute("CREATE DATABASE demo_alembic_db")
    print("Database 'demo_alembic_db' created successfully!")

cursor.close()
conn.close()
