import psycopg2

connection = psycopg2.connect('dbname=explre')
cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id serial PRIMARY KEY,
        username VARCHAR(255) NOT NULL,
        password VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL,
        first_name VARCHAR(255) NOT NULL,
        last_name VARCHAR(255) NOT NULL,
        is_admin BOOLEAN NOT NULL DEFAULT FALSE,
        created_at TIMESTAMP NOT NULL DEFAULT NOW());
""")
cursor.execute("""
    INSERT INTO users (username, password, email, first_name, last_name, is_admin)
    VALUES ('admin', 'admin', 'admin@explre.com','Isophel','Natwijuka','true');
""")
connection.commit()

cursor.close()
connection.close()