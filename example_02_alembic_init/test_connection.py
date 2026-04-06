import sys
print(f"Python encoding: {sys.getdefaultencoding()}")
print(f"File system encoding: {sys.getfilesystemencoding()}")

try:
    from database import DATABASE_URL, engine
    print(f"DATABASE_URL: {DATABASE_URL}")
    print(f"DATABASE_URL type: {type(DATABASE_URL)}")
    print(f"DATABASE_URL bytes: {DATABASE_URL.encode('utf-8')}")
    
    print("\nTrying to connect...")
    with engine.connect() as conn:
        result = conn.execute("SELECT 1")
        print("Connection successful!")
        print(f"Result: {result.fetchone()}")
except Exception as e:
    print(f"Error: {type(e).__name__}: {e}")
    import traceback
    traceback.print_exc()
