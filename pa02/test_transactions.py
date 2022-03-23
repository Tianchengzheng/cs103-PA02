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
