import streamlit as st
import psycopg2

st.set_page_config(page_title="Docker Compose Demo", page_icon="🐳", layout="centered")

st.title("🐳 Streamlit + PostgreSQL in Docker")
st.write("This app is running inside Docker, and it connects to a PostgreSQL database running in another container.")

# Database connection
try:
    conn = psycopg2.connect(
        host="db",          # hostname of PostgreSQL service (from docker-compose)
        dbname="testdb",
        user="testuser",
        password="testpass"
    )
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS visitors (name TEXT);")

    name = st.text_input("Enter your name:", "")
    if st.button("Save to Database"):
        if name:
            cur.execute("INSERT INTO visitors (name) VALUES (%s);", (name,))
            conn.commit()
            st.success(f"Saved '{name}' to the database!")

    st.subheader("Visitors")
    cur.execute("SELECT name FROM visitors;")
    rows = cur.fetchall()
    if rows:
        for row in rows:
            st.write(f"- {row[0]}")

    cur.close()
    conn.close()
except Exception as e:
    st.error(f"Database connection failed: {e}")
