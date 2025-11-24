import sqlite3

def get_con():
  conn = sqlite3.connect("db_bank.db")
  return conn

def init_db():
    conn = get_con()
    sql = conn.cursor()

    sql.execute("""
        CREATE TABLE IF NOT EXISTS accounts (
            account_number TEXT PRIMARY KEY,
            name TEXT,
            balance REAL DEFAULT 0,
            acc_type TEXT DEFAULT 'Regular'
        )
    """)
    
    conn.commit()
    conn.close()
