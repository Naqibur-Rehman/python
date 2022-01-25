import sqlite3

db = sqlite3.connect("contacts.sqlite")
name = input("Enter the name : ")

# details = "SELECT * FROM contacts WHERE name = ?"
# cursor1 = db.cursor()
# cursor1.execute(details, (name,))
#
# for row in cursor1:
#     print(row)
#
# cursor1.close()

# for row in db.execute("SELECT * FROM contacts WHERE name = ?", (name,)):
for row in db.execute("SELECT * FROM contacts WHERE name LIKE ?", (name,)):
    print(row)
db.close()