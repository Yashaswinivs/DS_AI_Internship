import sqlite3

# Connect to database (creates file if not exists)
conn = sqlite3.connect("internship.db")
cursor = conn.cursor()

# CREATE TABLE
cursor.execute("""
CREATE TABLE IF NOT EXISTS interns (
    id INTEGER PRIMARY KEY,
    name TEXT,
    track TEXT,
    stipend INTEGER
);
""")

# INSERT SAMPLE DATA
data = [
    (1, 'Aditi', 'Data Science', 7000),
    (2, 'Rahul', 'Web Dev', 5000),
    (3, 'Sneha', 'Data Science', 6000),
    (4, 'Arjun', 'AI', 8000),
    (5, 'Meera', 'Web Dev', 5500)
]

cursor.executemany("INSERT OR IGNORE INTO interns VALUES (?, ?, ?, ?)", data)

conn.commit()

# FILTER QUERY
print("📌 Data Science interns with stipend > 5000:\n")

filter_query = """
SELECT * FROM interns
WHERE track = 'Data Science' AND stipend > 5000;
"""

cursor.execute(filter_query)
for row in cursor.fetchall():
    print(row)

# AGGREGATE QUERY
print("\n📊 Average stipend per track:\n")

avg_query = """
SELECT track, AVG(stipend)
FROM interns
GROUP BY track;
"""

cursor.execute(avg_query)
for row in cursor.fetchall():
    print(f"{row[0]} → Avg Stipend: {row[1]:.2f}")

# COUNT QUERY
print("\n👥 Number of interns per track:\n")

count_query = """
SELECT track, COUNT(*)
FROM interns
GROUP BY track;
"""

cursor.execute(count_query)
for row in cursor.fetchall():
    print(f"{row[0]} → Total Interns: {row[1]}")

# Close connection
conn.close()