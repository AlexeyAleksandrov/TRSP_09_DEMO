import os
import sys

# Set environment variable before importing psycopg2
os.environ['PGCLIENTENCODING'] = 'UTF8'
os.environ['LANG'] = 'en_US.UTF-8'

print(f"PGCLIENTENCODING: {os.environ.get('PGCLIENTENCODING')}")
print(f"Python encoding: {sys.getdefaultencoding()}")

try:
    import psycopg2
    print("psycopg2 imported successfully")
    
    # Try direct connection
    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        user="postgres",
        password="1111",
        dbname="demo_alembic_db"
    )
    print("Direct psycopg2 connection successful!")
    
    cursor = conn.cursor()
    cursor.execute("SELECT version();")
    print(f"PostgreSQL version: {cursor.fetchone()[0]}")
    
    cursor.close()
    conn.close()
    
except Exception as e:
    print(f"Error: {type(e).__name__}: {e}")
    import traceback
    traceback.print_exc()
