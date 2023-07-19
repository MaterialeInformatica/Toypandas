'''Descizione modulo'''

from __future__ import annotations

import pandas as pd


class Series(pd.core.series.Series):
    '''Represenation of a series of values (usually a column).'''
    
    def __init__(self, *args):
        '''
        Initialize a Series with the given values.

        :param args: Individual values or already existing Series.
        '''

        if(len(args) == 0):
            super().__init__()
        elif (isinstance(args[0], pd.core.series.Series)): 
            super().__init__(args[0])
        else:
            super().__init__(args)

    def __add__(self, other) -> Series:
        '''
        Sums two series row by row.
        
        :param other: The other series to sum.
        
        :returns: A new series in which each value is the sum of the two rows.
        '''

        return Series(super().__add__(other))
        
    def __getitem__(self, match: pd.core.series.Series) -> Series:
        '''
        Returns only the rows matching the argument.
        
        :param match: A Series of booleans (True/False). If an element is True, it will be returned.  
        
        :returns: A new Series with only the elements matching the argument.
        '''

        result = super().__getitem__(match)
        result.reset_index(drop=True, inplace=True)
        return Series(result)

    @property
    def indexlocate(self) -> Locating_s:
        '''
        Locate an element by index.

        :returns: The element.
        '''

        return Locating_s(self)

    def apply(self, function) -> Series:
        '''
        Apply a function of each value of the Series.

        :param function: Function to apply to each element.

        :returns: The resulting Series.
        '''

        aux = Series(super().apply(function))
        return aux

    def append(self, elem):
        '''
        Appends a value at the end of the Series.

        :param elem: The value to append.
        '''

        if(len(self) <= 1):
            self.astype(type(elem))
        self.loc[len(self)] = elem

    def drop(self, index=None):
        '''
        Removes a given element from the Series.

        :param elem: The index of the element to remove. If not specified, remove the last element.
        '''

        if (index is None):
            size = self.size - 1
            super().drop(size, inplace=True) 
            self.reset_index(drop=True, inplace=True)
            return

        try:
            super().drop(index, inplace=True)
            self.reset_index(drop=True, inplace=True)
        except KeyError:
            print("Index might not exist")

    def astype(self, dtype) -> Series:
        '''
        Cast a Series to type ``dtype``.

        :param dtype: Data type

        :returns: This Series, properly cast.
        '''
        self = Series(super().astype(dtype, copy=False))
        return self
        
    def dropna(self) -> Series:
        '''
        Removes all NaN values.

        :returns: This Series, without NaN values.
        '''

        self = pd.core.series.Series(self)
        self = self.dropna()
        self.reset_index(drop=True, inplace=True)
        return Series(self) 
        
    def show(self):
        '''
        descr
        '''
        
        tipi = set()
        if (len(self.index) == 0):
            print("Empty series")
        for elem in self.index:
            if (pd.isnull(self.loc[elem])):
                print(elem, "NaN")
            else:
                print(elem, self.loc[elem])
            tipi.add(type(self.loc[elem]))
        if (len(tipi) > 1):
            print("name: ", self.name, " dtype: object")
        else:
            tipi = str(tipi)
            if(tipi == "{<class 'numpy.int64'>}" or tipi == "{<class 'int'>}"):
                print("name: ", self.name, " dtype: int")
            if(tipi == "{<class 'str'>}"):
                print("name: ", self.name, " dtype: str")
            if(tipi == "{<class 'numpy.float64'>}" or tipi == "{<class 'float'>}"):
                print("name: ", self.name, " dtype: float")
            if(tipi == "{<class 'numpy.bool_'>}" or tipi == "{<class 'bool'>}"):
                print("name: ", self.name, " dtype: bool")

    def fillna(self, value):
        '''
        Fill missing values with the given value.
        
        :param value: Value to use to fill holes.
        '''
        
        Series(super().fillna(value, inplace=True))


class Locating_s(pd.core.indexing._iLocIndexer):
    '''Index-based locator for Series'''
    def __init__(self, val):
        '''
        Initialize an index locator from a Series
        
        :param val: The Series
        '''
        
        super().__init__("iloc", val)
        self.s = pd.core.frame.Series(val)
    
    def __getitem__(self, *args):
        '''
        Return the element(s) in the required position(s).
        
        :param args: Index of the row to return or condition to apply to whole Series.

        :returns: The element(s) in the required position(s).
        '''

        if(isinstance(args[0],slice)):
            return Series(super().__getitem__(args[0]))
        elif (self.s.empty or (len(self.s.index) <= args[0])):
            raise IndexError("Series indexer is out-of-bounds")
        else: 
            return super().__getitem__(args[0]) # ho tolto casting a series()
    
    def __setitem__(self, *args) -> Series:
        '''
        Set the given position to the given value.

        :param args: Position and new value.

        :returns: The Series.
        '''
        if(len(self.s.index) > args[0]):
            if(len(self.s.index) == 1):
                #self.s.astype(type(args[1]))
                return Series(super().__setitem__(args[0],args[1]))
            else:
                return Series(super().__setitem__(args[0],args[1]))
        else:
            raise IndexError("Series indexer is out-of-bounds")
