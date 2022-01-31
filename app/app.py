import sqlite3

def get_auth_db():
    """
    input  : nothing
    output : a database with a message table
    
    Build a connection to the database. And build a table messages 
    with columns(id, handle, and message)
    """
    # check if message_db in g attribute
    if 'message_db' not in g:
        g.message_db = sqlite3.connect('messages_db.sqlite')

    # check if messages exists in message_db
    cmd = \
            """
            CREATE TABLE messages(
                id INTEGER UNIQUE,
                handle TEXT,
                message TEXT);
            """
    cursor = g.message_db.cursor()
    cursor.execute(cmd)
    cursor.closs()
    return g.message_db

def insert_message(request):
    """
    input  : a request form that has user input information
    output : nothing

    Add a new row of data into the messages table by SQL command. 
    Each row contains id, handle, and message. 
    id      : the current row number of table add one.
    handle  : the handle given by user
    message : the message given by user
    """
    # connect the database
    g.message_db = sqlite3.connect('messages_db.sqlite')
    cursor = g.message_db.cursor()
    # get the current row number in table messages
    cursor.execute("SELECT * FROM messages;")
    cur_row = cursor.fetchall() #current row num
    # modify id
    id = cur_row + 1
    # insert a new row into message table
    cmd = \
        """
        INSERT INTO message
        VALUES ({0}, {1}, {2});
        """.format(id, request.form["handle"], request.form["message"])
    cursor.execute(cmd)
    # run commit to ensure a new row has been saved into messages
    g.message_db.commit()
    g.message_db.close()

