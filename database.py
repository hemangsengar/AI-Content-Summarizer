import sqlite3


def create_articles_table():
    conn = sqlite3.connect('articles.db')
    c = conn.cursor()

    c.execute('''
        CREATE TABLE IF NOT EXISTS Data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            author TEXT,
            content TEXT,
            summary TEXT,
            source_url TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            
        )
    ''')
    conn.commit()
    conn.close()

def store_article(data: dict[str, str]):
    conn = sqlite3.connect('articles.db')
    c = conn.cursor()
    c.execute('''
        INSERT INTO Data (title, author, content, summary, source_url)
        VALUES (?, ?, ?, ?, ?)
    ''', (data['title'], data['author'], data['content'], 
          data['summary'], data['source_url']))
    conn.commit()
    conn.close()

    
    
    
    
    
def get_summary_by_id(article_id: int):
    conn = sqlite3.connect('articles.db')
    c = conn.cursor()
    c.execute('''SELECT summary FROM Data WHERE id = ?''', (article_id, ))

    result = c.fetchone()
    print(result[0])
    conn.commit()
    conn.close()



if __name__ == "__main__":
    get_summary_by_id(article_id=1)
    


