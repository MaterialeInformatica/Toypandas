import numpy
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
    s1 = Series(5, 6, 7)
    s2 = Series('a', 'b', 'c')
    s3 = Series(123, 546, 678)
    d = concat(s1, s2)

    d.append(s3)
    assert len(d) == 4
    assert d.indexlocate[3].indexlocate[0] == 123
    assert d.indexlocate[3].indexlocate[1] == 546

    d.append(Series(1))
    assert len(d) == 5
    assert d.indexlocate[4].indexlocate[0] == 1
    assert numpy.isnan(d.indexlocate[4].indexlocate[1])


def test_drop():
    s1 = Series(1, 2, 3)
    s2 = Series(4, 5, 6)
    d = concat(s1, s2)
    d.rename(0, 'col0')
    d.rename(1, 'col1')

    assert len(d) == 3
    assert len(d.columns) == 2

    d.drop(1)
    assert len(d) == 2
    assert len(d.columns) == 2


    d.drop('col1')
    assert len(d) == 2
    assert len(d.columns) == 1


def test_dropna():
    s1 = Series(1, numpy.NaN, 2, 1)
    s2 = Series(None, 'hello', 2, 1)
    s3 = Series(7, 8, 2, 1)
    s3 = Series(7, 8, 2, 1)
    d = concat(s1, s2, s3)

    res = d.dropna(0)
    assert len(res) == 2
    assert len(res.columns) == 3

    res = d.dropna(1)
    assert len(res) == 4
    assert len(res.columns) == 1


def test_dropduplicates():
    s1 = Series(4, 5, 6)
    d = concat(s1, s1)

    d = d.drop_duplicates()
    assert len(d) == 3

    d.append(Series(5, 5))
    assert len(d) == 4

    d = d.drop_duplicates()
    d.show()
    assert len(d) == 3


def test_isnull():
    s1 = Series(1, numpy.NaN)
    s2 = Series(None, 'hello')
    d = concat(s1, s2)
    result = d.isnull()

    assert len(result) == 2
    assert result.indexlocate[0].indexlocate[0] == False
    assert result.indexlocate[0].indexlocate[1] == True
    assert result.indexlocate[1].indexlocate[0] == True
    assert result.indexlocate[1].indexlocate[1] == False

def test_rename():
    d = read_csv('tests/data.csv')
    assert d.columns[0] == 'Col1'

    d.rename('Col1', 'NEW_NAME')
    assert d.columns[0] == 'NEW_NAME'