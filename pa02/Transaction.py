import sqlite3


def to_tran_dict(trantuple):
    ''' transaction is a transaction tuple (rowid, name, desc)'''
    tran = {'item #':trantuple[0], 'amount':trantuple[1], 'category':trantuple[2], 'date': trantuple[3], 'desc': trantuple[4]}
    return tran

def to_tran_dict_list(trantuples):
    ''' convert a list of transaction tuples into a list of dictionaries'''
    return [to_tran_dict(tran) for tran in trantuples]

class Transaction():

    def __init__(self, dbfile):
        con= sqlite3.connect(dbfile)
        cur = con.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS transactions
                    (amount real, category text, date text, description text)''')
        con.commit()
        con.close()
        self.dbfile = dbfile
    
    def select_all(self):
        ''' return all of the transactions as a list of dicts.'''
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute("SELECT item #,* from transactions")
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return to_tran_dict_list(tuples)
