import os
import sys

# Prevent psycopg2 from reading .pgpass and other system files
os.environ['PGPASSFILE'] = 'nul'  # Windows null device
os.environ['PGSYSCONFDIR'] = 'C:\\temp'  # Non-existent or empty dir
os.environ['PGSERVICEFILE'] = 'nul'
os.environ['PGCLIENTENCODING'] = 'UTF8'

print("Environment variables set")

try:
    import psycopg2
    
    # Try direct connection with explicit parameters
    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        user="postgres",
        password="1111",
        dbname="demo_alembic_db",
        client_encoding='UTF8',
        options='-c client_encoding=UTF8'
    )
    print("✓ Direct psycopg2 connection successful!")
    
    cursor = conn.cursor()
    cursor.execute("SELECT version();")
    version = cursor.fetchone()[0]
    print(f"✓ PostgreSQL version: {version[:50]}...")
    
    cursor.close()
    conn.close()
    
except Exception as e:
    print(f"✗ Error: {type(e).__name__}: {e}")
