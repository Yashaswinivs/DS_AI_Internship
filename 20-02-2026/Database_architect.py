import sqlite3

# 1. Create / Connect to database
conn = sqlite3.connect("internship.db")

# 2. Create cursor object
cursor = conn.cursor()

# 3. Create interns table
cursor.execute("""
CREATE TABLE IF NOT EXISTS interns (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    track TEXT,
    stipend INTEGER
)
""")

# 4. Insert sample data
data = [
    ("Amit", "Data Science", 12000),
    ("Neha", "Web Development", 10000),
    ("Rahul", "Cyber Security", 15000),
    ("Priya", "Data Science", 13000),
    ("Kiran", "AI & ML", 18000)
]

cursor.executemany("INSERT INTO interns (name, track, stipend) VALUES (?, ?, ?)", data)

# 5. Commit changes
conn.commit()

# 6. SELECT Query: Retrieve only name and track
cursor.execute("SELECT name, track FROM interns")

# 7. Fetch and display results
rows = cursor.fetchall()

print("Intern Name  |  Track")
print("-------------------------")

for row in rows:
    print(row[0], " | ", row[1])

# 8. Close connection
conn.close()