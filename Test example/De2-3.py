from itertools import count
from msilib.schema import tables
import sqlite3
from unicodedata import name
from prettytable import PrettyTable

conn = sqlite3.connect('DNSList.sqlite')
cur = conn.cursor()
cur.execute('DROP TABLE IF EXISTS Providers')
cur.execute('''CREATE TABLE Providers (IP TEXT, Reliability INTEGER, Description TEXT)''')
fname = input('Enter file name: ')
if len(fname) < 1:
    fname = 'DNSList.txt'
fh = open(fname)
for line in fh:
    if not line.startswith("IP Address:"): continue
    pieces = line.split(":")
    name = pieces[1]
    rel = pieces[2]
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Providers (IP, Reliability)
            VALUES (?, ?)''', (name,rel))
cur.execute('UPDATE Providers SET Description = "Normal" WHERE Reliability > 50')
cur.execute('UPDATE Providers SET Description = "Low" WHERE Reliability <= 50')          

table = PrettyTable(['IP','Reliability','Description'])
cur.execute('SELECT * FROM Providers ORDER BY Reliability DESC')
dns_server = cur.fetchall()
for server in dns_server:
    table.add_row(server)
print("DNS server list:")
print(table)

conn.commit()


