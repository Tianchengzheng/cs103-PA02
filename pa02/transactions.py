import sqlite3


def to_tran_dict(trantuple):
    ''' transaction is a transaction tuple (item#, amount, category, date, desc)'''
    tran = {'itemnum':trantuple[0], 'amount':trantuple[1], 'category':trantuple[2], 'date': trantuple[3], 'desc': trantuple[4]}
    return tran

def to_tran_dict_date(trantuple):
    tran = {'date':trantuple[0], 'total':trantuple[1]}
    return tran

def to_tran_dict_list(trantuples):
    ''' convert a list of transaction tuples into a list of dictionaries'''
    return [to_tran_dict(tran) for tran in trantuples]

class Transaction():

    def __init__(self, dbfile):
        con = sqlite3.connect(dbfile)
        cur = con.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS transactions
                    (amount real, category text, date text, desc text)''')
        con.commit()
        con.close()
        self.dbfile = dbfile
    
    def select_all(self):
        ''' return all of the transactions as a list of dicts.'''
        con = sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute("SELECT rowid, * from transactions")
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return to_tran_dict_list(tuples)
    
    def add(self, item):
        ''' add a transaction to the transactions table.
            this returns the item# of the inserted element
        '''
        con = sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute("INSERT INTO transactions VALUES(?,?,?,?)",(item['amount'],item['category'], item['date'], item['desc']))
        con.commit()
        cur.execute("SELECT last_insert_rowid()")
        last_item = cur.fetchone()
        con.commit()
        con.close()
        return last_item[0]

    def delete(self, item):
        con = sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute("DELETE FROM transactions WHERE rowid =  ?", item)
        con.commit()
        con.close()

    # Iria Wang
    def summarize_by_date(self):
        con = sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute('SELECT date, sum(amount) FROM transactions GROUP BY date')
        by_date = cur.fetchall()
        con.close()
        return to_tran_dict_date(by_date)

    # Iria Wang
    def summarize_by_month(self):
        con = sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute('SELECT sum(amount) FROM transactions GROUP BY substr(date, 1, 7)')
        by_date = cur.fetchall()
        con.close()
        return to_tran_dict_list(by_date)
    
    # Iria Wang
    def summarize_by_year(self):
        con = sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute('SELECT sum(amount) FROM transactions GROUP BY substr(date, 1, 4)')
        by_date = cur.fetchall()
        con.close()
        return to_tran_dict_list(by_date)

    # Tiancheng Zheng
    def summarize_by_category(self):
        con = sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute('SELECT sum(amount) FROM transactions GROUP BY category')
        by_category = cur.fetchall()
        con.close()
        return to_tran_dict_list(by_category)
    
    

    def select_one(self,rowid):
        ''' return a transaction with a specified rowid '''
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute("SELECT rowid,* from transactions where rowid=(?)",(rowid,) )
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return to_tran_dict(tuples[0])