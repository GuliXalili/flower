import sqlite3 as sql

con = sql.connect("odamlar.db")

mal = con.cursor()
mal1 = con.cursor()
mal2 = con.cursor()
mal3 = con.cursor()
mal4 = con.cursor()

mal.execute('''
CREATE TABLE IF NOT EXISTS Studentlar(
    ism TEXT,
    fam TEXT,
    yosh INTEGER
)            
'''),

mal1.execute('''
CREATE TABLE IF NOT EXISTS Programmistlar(
    ism TEXT,
    fam TEXT,
    yosh INTEGER
)             
'''),

mal2.execute('''
CREATE TABLE IF NOT EXISTS Bekorchilar(
    ism TEXT,
    fam TEXT,
    yosh INTEGER
)
''')

mal3.execute('''
CREATE TABLE IF NOT EXISTS Stuardessalar(
    buyi FLOAT,
    vazni FLOAT,
    uniforma TEXT
    )
    ''')

mal4.execute('''
CREATE TABLE IF NOT EXISTS Pilotlar(
    buyi FLOAT,
    vazni FLOAT,
    uniforma TEXT
    )
    ''')
