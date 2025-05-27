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

def get_all_summary():
    conn = sqlite3.connect('articles.db')
    c = conn.cursor()
    c.execute('''SELECT id, summary FROM Data''')
    result = c.fetchall()
    conn.close()
    print(result)

def cli_menu():
    while True:
        print("\n====== Article Summary CLI ======")
        print("1. View all summaries")
        print("2. View summary by ID")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ").strip()

        if choice == '1':
            get_all_summary()
        elif choice == '2':
            try:
                article_id = int(input("Enter article ID: "))
                get_summary_by_id(article_id)
            except ValueError:
                print("Invalid ID. Please enter a number.")
        elif choice == '3':
            print("Exiting CLI. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")



if __name__ == "__main__":
    create_articles_table()
    cli_menu()

    


