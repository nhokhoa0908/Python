from itertools import count
import sqlite3
from unicodedata import name
from prettytable import PrettyTable

conn = sqlite3.connect('Mark.sqlite')
cur = conn.cursor()
cur.execute('DROP TABLE IF EXISTS Marks')
cur.execute('''CREATE TABLE Marks (ID TEXT, Name TEXT, Math FLOAT, Physic FLOAT, Chemis FLOAT, Sum FLOAT, Result TEXT)''')
fname = input('Enter file name: ')
if len(fname) < 1:
    fname = 'Data.txt'
fh = open(fname)
for line in fh:
    if not line.startswith("A"): continue
    pieces = line.split()
    IID = pieces[0]
    NName = pieces[1] + " " + pieces[2] + " " + pieces[3]
    MMath = pieces[4]
    PPhysic = pieces[5]
    CChemis = pieces[6]
    
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Marks (ID, Name, Math, Physic, Chemis)
            VALUES (?, ?, ? ,? ,?)''', (IID, NName, MMath, PPhysic, CChemis))
        cur.execute('UPDATE Marks SET Sum = Math + Physic + Chemis WHERE ID= ?',(IID,))
cur.execute('UPDATE Marks SET Result = "Not pass" WHERE Sum < 15')
cur.execute('UPDATE Marks SET Result = "Pass" WHERE Sum >= 15')          
cur.execute('SELECT * FROM Marks ORDER BY Sum DESC')

table = PrettyTable(['ID', 'Full Name', 'Math', 'Physic', 'Chemis', 'Sum', 'Result'])
cur.execute('SELECT * FROM Marks ORDER BY Sum DESC')
dns_server = cur.fetchall()
for server in dns_server:
    table.add_row(server)
print("Student list:")
print(table)

conn.commit()