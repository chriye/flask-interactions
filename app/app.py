import sqlite3

def get_auth_db():
    """
    """
    # check if message_db in g attribute
    if 'message_db' not in g:
        g.message_db = sqlite3.connect('messages_db.sqlite')

    # check if messages exists in message_db
    cmd = \
            """
            CREATE TABLE messages(
                id INTEGER,
                handle TEXT,
                message TEXT);
            """
    cursor = g.message_db.cursor()
    cursor.excute(cmd)
    return g.message_db

def insert_message(request):
    
