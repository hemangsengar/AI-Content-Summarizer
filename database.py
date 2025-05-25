import sqlite3


def db():
    conn = sqlite3.connect('Data.db')
    c = conn.cursor()

    c.execute('''
        CREATE TABLE IF NOT EXISTS Data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            quote TEXT,
            author TEXT,
            raw_content TEXT,
            preprocessed_content TEXT,
            ai_summary TEXT
            
        )
    ''')

def insert_quote(quote, author, raw_content=None, preprocessed_content=None, ai_summary=None):
    conn = sqlite3.connect('Data.db')
    c = conn.cursor()
    c.execute('''
        INSERT INTO Data (quote, author, raw_content, preprocessed_content, ai_summary)
        VALUES (?, ?, ?, ?, ?)
    ''', (quote, author,raw_content, preprocessed_content, ai_summary))
    conn.commit()
    conn.close()



