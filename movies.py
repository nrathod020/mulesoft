import sqlite3

conn = sqlite3.connect('movies.db')
# create a cursor
c = conn.cursor()

# create a table
'''c.execute("""CREATE TABLE tb(
        moviename text,
        actorname text,
        actressname text,
        releaseyear text,
        directorname
    )""")'''

# Insert Record
'''c.execute("INSERT INTO tb VALUES ('sarrinodu','allu arjun','rakul preet singh','2016','boyapati srinu')") 
c.execute("INSERT INTO tb VALUES ('san andreas','dwayne johnson','alexandra deadrio','2015','brad peyton')")
c.execute("INSERT INTO tb VALUES ('satyameva jayate 2','john abrahm','divya khosla','2021','milap zaveri')")
c.execute("INSERT INTO tb VALUES ('pushpa','allu arjun','rashmika mandana','2021','sukumar')")
c.execute("INSERT INTO tb VALUES ('tadap','ahan shetty','tara sutariya','2021','milan luthria')")
'''

# update
'''c.execute("""UPDATE tb SET actressname='Rakul Preet'
    WHERE moviename = 'sarrinodu'
    """) '''

# delete
'''c.execute("DELETE from tb WHERE moviename = 'tadap'") '''

# drop
'''c.execute("DROP TABLE tb") '''

c.execute("SELECT * FROM tb")

fields = c.fetchall()
for field in fields:
    print(field)

conn.commit()

conn.close()