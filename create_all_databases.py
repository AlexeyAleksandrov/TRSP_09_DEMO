import pg8000

databases = [
    'demo_crud_db',
    'demo_alembic_db',
    'demo_migrations_db',
    'demo_revisions_db',
    'demo_seeding_db',
    'demo_rollbacks_db'
]

conn = pg8000.connect(
    host="localhost",
    port=5432,
    user="postgres",
    password="1111",
    database="postgres"
)

conn.autocommit = True
cursor = conn.cursor()

for db_name in databases:
    cursor.execute(f"SELECT 1 FROM pg_database WHERE datname = '{db_name}'")
    exists = cursor.fetchone()
    
    if exists:
        print(f"[OK] Database '{db_name}' already exists")
    else:
        cursor.execute(f"CREATE DATABASE {db_name}")
        print(f"[OK] Database '{db_name}' created successfully!")

cursor.close()
conn.close()

print("\n[OK] All databases are ready!")
