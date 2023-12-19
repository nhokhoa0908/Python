from itertools import count
import sqlite3
from unicodedata import name
from prettytable import PrettyTable

conn = sqlite3.connect('Trace.sqlite')
cur = conn.cursor()
cur.execute('DROP TABLE IF EXISTS Providers')
cur.execute('''CREATE TABLE Providers (Pname TEXT, Pcount INTEGER, Pwarning TEXT)''')
fname = input('Enter file name: ')
if len(fname) < 1:
    fname = 'Trace.txt'
fh = open(fname)
for line in fh:
    if not line.startswith("Name: "): continue
    pieces = line.split('-')
    name = pieces[1]
    cur.execute('SELECT Pcount FROM Providers WHERE Pname= ? ', (name,))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Providers (Pname, Pcount)
            VALUES (?, 1)''', (name,))
    else:
        cur.execute('UPDATE Providers SET Pcount = Pcount + 1 WHERE Pname= ?',(name,))
cur.execute('UPDATE Providers SET Pwarning = "High risk" WHERE Pcount > 1')
cur.execute('UPDATE Providers SET Pwarning = "Normal" WHERE Pcount <= 1')          
cur.execute('SELECT * FROM Providers ORDER BY Pcount DESC')

table = PrettyTable(['Pname','Pcount','Pwarning'])
cur.execute('SELECT * FROM Providers ORDER BY Pcount DESC')
dns_server = cur.fetchall()
for server in dns_server:
    table.add_row(server)
print("Troubleshoot wired LAN related issues:")
print(table)

conn.commit()