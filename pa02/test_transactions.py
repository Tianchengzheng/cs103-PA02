'''
test_categories runs unit and integration tests on the category module
'''

import pytest
from transactions import Transaction

@pytest.fixture
def dbfile(tmpdir):
    ''' create a database file in a temporary file system '''
    return tmpdir.join('test_transactions.db')

@pytest.fixture
def empty_db(dbfile):
    ''' create an empty database '''
    db = Transaction(dbfile)
    yield db

@pytest.fixture
def small_db(empty_db):
    ''' create a small database, and tear it down later'''
    tran1 = {'amount':12,'category':'food', 'date': '2020/06/12', 'desc': 'testtest'}
    tran2 = {'amount':15,'category':'not food', 'date': '2020/07/12', 'desc': 'testing again'}
    tran3 = {'amount':13,'category':'toys', 'date': '2020/06/12', 'desc': 'lego batman'}
    id1=empty_db.add(tran1)
    id2=empty_db.add(tran2)
    id3=empty_db.add(tran3)
    yield empty_db
    empty_db.delete(id3)
    empty_db.delete(id2)
    empty_db.delete(id1)


@pytest.fixture
def med_db(empty_db):
    ''' create a small database, and tear it down later'''
    tran1 = {'amount':12,'category':'food', 'date': '1900/02/02', 'desc': 'testtest'}
    tran2 = {'amount':15,'category':'not food', 'date': '1900/02/02', 'desc': 'testing again'}
    tran3 = {'amount':13,'category':'toys', 'date': '2020/02/11', 'desc': 'lego batman'}
    tran4 = {'amount':122,'category':'food', 'date': '2019/08/16', 'desc': 'testtest'}
    tran5 = {'amount':132,'category':'toys', 'date': '2017/07/22', 'desc': 'legos'}
    tran6 = {'amount':126,'category':'food', 'date': '2021/09/02', 'desc': 'testtesttest'}
    tran7 = {'amount':159,'category':'not food', 'date': '2022/07/03', 'desc': 'testingtesting'}
    tran8 = {'amount':130,'category':'toys', 'date': '2022/03/18', 'desc': 'legossss'}
    tran9 = {'amount':121,'category':'food', 'date': '2018/06/11', 'desc': 't'}
    tran10 = {'amount':153,'category':'not food', 'date': '2010/02/12', 'desc': 'testing...'}
    tran11 = {'amount':12,'category':'toys', 'date': '2021/06/12', 'desc': 'legoooo'}
    tran12 = {'amount':153,'category':'not food', 'date': '2018/05/18', 'desc': 'testingggg'}
    id1=empty_db.add(tran1)
    id2=empty_db.add(tran2)
    id3=empty_db.add(tran3)
    id4=empty_db.add(tran4)
    id5=empty_db.add(tran5)
    id6=empty_db.add(tran6)
    id7=empty_db.add(tran7)
    id8=empty_db.add(tran8)
    id9=empty_db.add(tran9)
    id10=empty_db.add(tran10)
    id11=empty_db.add(tran11)
    id12=empty_db.add(tran12)
    yield empty_db
    empty_db.delete(id12)
    empty_db.delete(id11)
    empty_db.delete(id10)
    empty_db.delete(id9)
    empty_db.delete(id8)
    empty_db.delete(id7)
    empty_db.delete(id6)
    empty_db.delete(id5)
    empty_db.delete(id4)
    empty_db.delete(id3)
    empty_db.delete(id2)
    empty_db.delete(id1)

@pytest.mark.add
def test_add(med_db):
    ''' add a category to db, the select it, then delete it'''

    tran0 = {'amount': 12,
            'category':'see if it works',
            'date': '2019/05/22',
            'desc': 'test desc'
            }
    trans0 = med_db.select_all()
    rowid = med_db.add(tran0)
    trans1 = med_db.select_all()
    assert len(trans1) == len(trans0) + 1
    tran1 = med_db.select_one(rowid)
    assert tran1['amount']==tran0['amount']
    assert tran1['category']==tran0['category']
    assert tran1['date']==tran0['date']
    assert tran1['desc']==tran0['desc']

@pytest.mark.delete
def test_delete(med_db):
    ''' add a category to db, delete it, and see that the size changes'''
    # first we get the initial table
    trans0 = med_db.select_all()

    # then we add this category to the table and get the new list of rows
    trans0 = {'amount':50,'category':'books', 'date': '2020/06/13', 'desc': 'textbook'}
    rowid = med_db.add(trans0)
    trans1 = med_db.select_all()

    # now we delete the category and again get the new list of rows
    med_db.delete(rowid)
    trans2 = med_db.select_all()

    assert len(trans0)==len(trans2)
    assert len(trans2) == len(trans1)-1


@pytest.mark.summarizedate
def test_summarizedate(med_db):
    newdb = med_db.summarize_by_date()
    dbrow = newdb.select_one(1)
    assert dbrow['date']=='1900/02/02'
    assert dbrow['amount']==27