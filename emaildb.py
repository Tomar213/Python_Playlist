import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()
cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

fh = open("mbox.txt")
org = dict()
bst = list()
for line in fh:
    if line.startswith("From: "):
        newline = line.rstrip("\n")
        lst = newline.split(" ")
        domain = lst[1].split("@")[1]
        cur.execute('SELECT count FROM Counts WHERE org = ? ', (domain,))
        row = cur.fetchone()
        if row is None:
            cur.execute('''INSERT INTO Counts (org, count)
                        VALUES (?, 1)''', (domain,))
        else:
            cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
                        (domain,))
        conn.commit()


sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

print("Counts:")
for row in cur.execute(sqlstr) :
    print (str(row[0]), row[1])
print("data uploaded ")
# # print(bst)
# for dom in bst:
#     org[dom]= org.get(dom,0)+1
#
# print(org)
# fh.close()
#
# {'uct.ac.za': 383, 'media.berkeley.edu': 224, 'umich.edu': 1964, 'iupui.edu': 2144, 'caret.cam.ac.uk': 628, 'gmail.com': 100, 'indiana.edu': 712, 'et.gatech.edu': 68, 'vt.edu': 440, 'lancaster.ac.uk': 56, 'ucdavis.edu': 4, 'ufp.pt': 112, 'txstate.edu': 68, 'stanford.edu': 48, 'whitman.edu': 68, 'rsmart.com': 32, 'fhda.edu': 4, 'bu.edu': 56, 'unicon.net': 36, 'loi.nl': 36, 'utoronto.ca': 4}