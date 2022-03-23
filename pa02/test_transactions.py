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
    tran1 = {'amount':'12','category':'food', 'date': '2020/06/12', 'desc:': 'testtest'}
    tran2 = {'amount':'15','category':'not food', 'date': '2020/07/12', 'desc:': 'testing again'}
    tran3 = {'amount':'13','category':'toys', 'date': '2020/06/12', 'desc:': 'lego batman'}
    id1=empty_db.add(tran1)
    id2=empty_db.add(tran2)
    id3=empty_db.add(tran3)
    yield empty_db
    empty_db.delete(id3)
    empty_db.delete(id2)
    empty_db.delete(id1)


@pytest.mark.add
def test_add(med_db):
    ''' add a category to db, the select it, then delete it'''

    tran0 = {'amount':'12',
            'category':'see if it works',
            'date': '2019/05/22',
            'desc': 'test desc'
            }
    trans0 = med_db.select_all()
    rowid = med_db.add(tran0)
    trans1 = med_db.select_all()
    assert len(trans1) == len(trans0) + 1
    tran1 = med_db.select_one(rowid)
    assert tran1['amount']==tran0['amomunt']
    assert tran1['category']==tran0['category']
    assert tran1['date']==tran0['date']
    assert tran1['desc']==tran0['desc']

@pytest.mark.delete
def test_delete(med_db):
    ''' add a category to db, delete it, and see that the size changes'''
    # first we get the initial table
    trans0 = med_db.select_all()

    # then we add this category to the table and get the new list of rows
    trans0 = {'amount':'50','category':'books', 'date': '2020/06/13', 'desc:': 'textbook'}
    rowid = med_db.add(trans0)
    trans1 = med_db.select_all()

    # now we delete the category and again get the new list of rows
    med_db.delete(rowid)
    trans2 = med_db.select_all()

    assert len(trans0)==len(trans2)
    assert len(trans2) == len(trans1)-1