'''Descizione modulo'''

from __future__ import annotations

import pandas as pd


class Series(pd.core.series.Series):
    '''Descrizione classe'''
    
    def __init__(self, *args):
        '''
        Descrizione generica.

        :param args: Descrizione.
        '''

        if(len(args) == 0):
            super().__init__()
        #elif (len(args)>1 and isinstance(args[0], pd.core.series.Series)): #controlla che con uello sopra ancora funion
        elif (isinstance(args[0], pd.core.series.Series)): 
            super().__init__(args[0])
        else:
            arg_list = list()
            for elem in args:
                arg_list.append(elem)
            super().__init__(arg_list)

    def __add__(self, other) -> Series:
        '''
        descr
        
        :param other: edsaf
        
        :returns: dfada
        '''

        return Series(super().__add__(other))
        
    def __getitem__(self, *args) -> Series:
        '''
        asdfsadf
        
        :param args: sadfad
        
        :returns: sdfasdf
        '''
        #print(type(args))
        #print(args)
        if isinstance(args[0], pd.core.series.Series):
            temp = super().__getitem__(args[0])
            temp.reset_index(drop=True, inplace=True)
            return Series(temp)

    @property
    def indexlocate(self) -> Locating_s:
        '''
        Descrizione generica.

        :returns: Descr return.
        '''

        return Locating_s(self)

    def apply(self, function) -> Series:
        '''
        Descrizione generica.

        :param function: Descrizione.

        :returns: Descr return.
        '''

        aux = Series(super().apply(function))
        return aux

    def append(self, elem):
        '''
        Descrizione generica.

        :param elem: Descrizione.
        '''

        if(len(self) <= 1):
            self.astype(type(elem))
            self.loc[len(self)] = elem
        else:
            self.loc[len(self)] = elem

    def drop(self, *elem):
        '''
        Descrizione generica.

        :param elem: Descrizione.
        '''

        if (len(elem) == 0):
            size = self.size - 1
            super().drop(size, inplace=True) 
            self.reset_index(drop=True, inplace=True)
        else:
            try:
                super().drop(elem[0], inplace=True)
                self.reset_index(drop=True, inplace=True)
            except KeyError:
                print("Index might not exist")

    def astype(self, tp) -> Series:
        '''
        Descrizione generica.

        NON E` FORSE MEGLIO RINOMINARE IN as_type ?
        e tp in new_type (non puoi usare type)
        (occhio al refactoring)

        :param tp: Descrizione.

        :returns: Descr return.
        '''
        self = Series(super().astype(tp, copy=False))
        return self

        #return serie(super().astype(tp, copy=False))
        
    def dropna(self) -> Series:
        '''
        Descr

        :returns: adfasf
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
            #sys.stdout = open(os.devnull, 'w')
            #return self

    def fillna(self, ph):
        '''descr
        
        :param ph: asdfasd - non si capisce cosa vuol dire ph
        '''
        Series(super().fillna(ph, inplace=True))


class Locating_s(pd.core.indexing._iLocIndexer):
    '''Descrizione modulo'''
    def __init__(self, val):
        '''
        descr
        
        :param val: descr
        '''
        
        super().__init__("iloc", val)
        self.s = pd.core.frame.Series(val)
    
    def __getitem__(self, *args):
        '''
        descr
        
        :param args: descr

        :returns: descr
        '''

        # series with one element lost their key
        #print(args)
        #print(type(args[0]))
        if(isinstance(args[0],slice)):
            return Series(super().__getitem__(args[0]))
        elif (self.s.empty or (len(self.s.index) <= args[0])):
            raise IndexError("Series indexer is out-of-bounds")
        else: 
            return super().__getitem__(args[0]) # ho tolto casting a series()
    
    def __setitem__(self, *args) -> Series:
        '''
        descr

        :param args: descr

        :returns: descr
        '''
        if(len(self.s.index) > args[0]):
            if(len(self.s.index) == 1):
                #self.s.astype(type(args[1]))
                return Series(super().__setitem__(args[0],args[1]))
            else:
                return Series(super().__setitem__(args[0],args[1]))
        else:
            raise IndexError("Series indexer is out-of-bounds")
