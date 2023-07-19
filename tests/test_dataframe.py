import pytest
from toypandas import Dataframe, Series, concat, read_csv


def test_concat():
    # empty dataframe
    assert len(concat()) == 0

    # series
    s1 = Series(4, 5, 6)
    s2 = Series(7, 8, 9)

    d1 = concat(s1, s2)
    assert len(d1) == 3
    assert d1.indexlocate[0].indexlocate[0] == 4
    assert d1.indexlocate[0].indexlocate[1] == 7
    assert d1.indexlocate[1].indexlocate[0] == 5
    assert d1.indexlocate[1].indexlocate[1] == 8
    assert d1.indexlocate[2].indexlocate[0] == 6
    assert d1.indexlocate[2].indexlocate[1] == 9

    # dataframe
    d2 = concat(d1, d1)
    assert len(d2) == 6
    assert d2.indexlocate[0].indexlocate[0] == 4
    assert d2.indexlocate[0].indexlocate[1] == 7
    assert d2.indexlocate[1].indexlocate[0] == 5
    assert d2.indexlocate[1].indexlocate[1] == 8
    assert d2.indexlocate[2].indexlocate[0] == 6
    assert d2.indexlocate[2].indexlocate[1] == 9
    assert d2.indexlocate[3].indexlocate[0] == 4
    assert d2.indexlocate[3].indexlocate[1] == 7
    assert d2.indexlocate[4].indexlocate[0] == 5
    assert d2.indexlocate[4].indexlocate[1] == 8
    assert d2.indexlocate[5].indexlocate[0] == 6
    assert d2.indexlocate[5].indexlocate[1] == 9


def test_readcsv():
    d = read_csv('tests/data.csv')

    assert len(d) == 3
    assert d.indexlocate[0].indexlocate[0] == 'abc'
    assert d.indexlocate[0].indexlocate[1] == 123
    assert d.indexlocate[1].indexlocate[0] == 'def'
    assert d.indexlocate[1].indexlocate[1] == 456
    assert d.indexlocate[2].indexlocate[0] == 'ghi'
    assert d.indexlocate[2].indexlocate[1] == 789


def test_append():
    pass


def test_drop():
    pass


def test_dropna():
    pass


def test_dropduplicates():
    pass

def test_isnull():
    pass


def test_rename():
    d = read_csv('tests/data.csv')
    assert d.columns[0] == 'Col1'

    d.rename('Col1', 'NEW_NAME')
    assert d.columns[0] == 'NEW_NAME'