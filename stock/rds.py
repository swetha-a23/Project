import psycopg2

try:
    # Establish a connection to the PostgreSQL database
    conn = psycopg2.connect(
        host='stock123.czs3pf6sndfm.us-east-1.rds.amazonaws.com',
        port=5432,
        user='postgres',
        password='Aarthi_stock012'
    )
    
    # Check the connection status
    if conn.status == psycopg2.extensions.STATUS_READY:
        print("Connection to the database is successful!")
    else:
        print("Connection failed.")
        
    # Close the connection
    conn.close()
    
except psycopg2.Error as e:
    print("Error connecting to the database:", e)
