from flask import Flask
import os
import mysql.connector

app = Flask(__name__)

DB_HOST = os.getenv("DB_HOST", "mariadb")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME", "kubeforge")
APP_TITLE = os.getenv("APP_TITLE", "KubeForge Demo1")

def get_connection():
    return mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )

@app.route("/")
def home():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS visits (
            id INT PRIMARY KEY AUTO_INCREMENT,
            visited_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    cursor.execute("INSERT INTO visits () VALUES ()")
    conn.commit()

    cursor.execute("SELECT COUNT(*) FROM visits")
    visits = cursor.fetchone()[0]

    cursor.close()
    conn.close()

    return f"""
    <h1>{APP_TITLE}</h1>
    <h2>Visite: {visits}</h2>
    <p>Pod Flask collegato a MariaDB su Kubernetes.</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
