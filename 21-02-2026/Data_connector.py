import sqlite3
import pandas as pd

# 1. Connect to Database
conn = sqlite3.connect("internship.db")
cursor = conn.cursor()

print("Connected to internship.db")

# 2. Create interns table
cursor.execute("""
CREATE TABLE IF NOT EXISTS interns (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    track TEXT,
    stipend INTEGER
);
""")

# 3. Create mentors table
cursor.execute("""
CREATE TABLE IF NOT EXISTS mentors (
    mentor_id INTEGER PRIMARY KEY AUTOINCREMENT,
    mentor_name TEXT,
    track TEXT
);
""")

conn.commit()
print("Tables created successfully")

# 4. Insert interns data
cursor.execute("SELECT COUNT(*) FROM interns")
if cursor.fetchone()[0] == 0:
    cursor.executemany("""
    INSERT INTO interns (name, track, stipend) VALUES (?, ?, ?);
    """, [
        ("Ramesh", "Data Science", 15000),
        ("Sneha", "Web Dev", 12000),
        ("Aditi", "AI", 18000),
        ("Kiran", "Cyber Security", 16000),
        ("Pooja", "Data Science", 15000)
    ])
    print("Interns data inserted")

# 5. Insert mentors data
cursor.execute("SELECT COUNT(*) FROM mentors")
if cursor.fetchone()[0] == 0:
    cursor.executemany("""
    INSERT INTO mentors (mentor_name, track) VALUES (?, ?);
    """, [
        ("Dr. Ananya", "Data Science"),
        ("Mr. Rahul", "Web Dev"),
        ("Ms. Priya", "AI"),
        ("Mr. Karthik", "Cyber Security")
    ])
    print("Mentors data inserted")

conn.commit()

# 6. Verify Tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print("Tables in database:", cursor.fetchall())

# 7. SQL JOIN → Pandas
query = """
SELECT 
    interns.name AS intern_name,
    interns.track,
    mentors.mentor_name
FROM interns
INNER JOIN mentors
ON interns.track = mentors.track;
"""

df = pd.read_sql_query(query, conn)

print("\nJOIN Result Loaded Into Pandas:\n")
print(df)

# 8. Close Connection
conn.close()
print("\nDatabase connection closed")