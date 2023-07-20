from toypandas.series import *
import pandas as pd
import numpy

def test_create():
    s0 = Series()
    assert len(s0) == 0

    s1 = Series('Bob', 'Alice', 'Ted', 'Carol')

    assert len(s1) == 4
    assert s1.indexlocate[0] == 'Bob'
    assert s1.indexlocate[1] == 'Alice'
    assert s1.indexlocate[2] == 'Ted'
    assert s1.indexlocate[3] == 'Carol'

    s2_pd = pd.Series([4, 9, 8])
    s2 = Series(s2_pd)
    assert len(s2) == 3
    assert s2.indexlocate[0] == 4
    assert s2.indexlocate[1] == 9
    assert s2.indexlocate[2] == 8

def test_apply():
    s = Series(2, 0, 5, 9, 11)

    s2 = s.apply(lambda x: x*2)

    assert len(s2) == 5
    assert s2.indexlocate[0] == 4
    assert s2.indexlocate[1] == 0
    assert s2.indexlocate[2] == 10
    assert s2.indexlocate[3] == 18
    assert s2.indexlocate[4] == 22

def test_getitem():
    s = Series(2, 0, 5, 9, 11)

    s2 = s[s >= 5]

    assert len(s2) == 3
    assert s2.indexlocate[0] == 5
    assert s2.indexlocate[1] == 9
    assert s2.indexlocate[2] == 11

def test_append():
    s = Series(22, 1, 15)
    
    assert len(s) == 3

    s.append(0)
    assert len(s) == 4
    assert s.indexlocate[3] == 0

def test_astype():
    s = Series(1, 2)

    assert type(s.indexlocate[0]) == numpy.int64
    assert type(s.indexlocate[1]) == numpy.int64

    s = s.astype(float)
    assert type(s.indexlocate[0]) == numpy.float64 
    assert type(s.indexlocate[1]) == numpy.float64

def test_dropna():
    s = Series(5, numpy.NaN, 6)
    s = s.dropna()

    assert len(s) == 2
    assert s.indexlocate[0] == 5
    assert s.indexlocate[1] == 6

def test_fillna():
    s = Series(5, numpy.NaN, 6)
    s.fillna(0)

    assert len(s) == 3
    assert s.indexlocate[0] == 5
    assert s.indexlocate[1] == 0
    assert s.indexlocate[2] == 6

def test_show_empty(capsys):
    s = Series()
    s.show()
    captured = capsys.readouterr()
    assert captured.out.strip() == 'Empty series'

# need more testing for different show scenarios and for Locating_s