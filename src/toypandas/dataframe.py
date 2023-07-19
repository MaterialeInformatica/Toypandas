'''Descrizione modulo'''

from __future__ import annotations

import pandas as pd
import re

from .series import Series


def concat(*args) -> Dataframe:
    '''
    Concatenate an arbitrary number of Series or Dataframes into a single Dataframe.

    :param arg: Series or Dataframes.

    :returns: A single Dataframe, containing all values provided.
    '''

    if len(args) == 0:
        return Dataframe()

    df = True
    for arg in args:
        df = df and isinstance(arg, Dataframe) # concat dataframes or series
    
    if(df):
        return Dataframe(pd.concat(args, ignore_index=True))
    return Dataframe(pd.concat(args, axis = 1))

def concat_df(tpl) -> Dataframe:
    lista = list()
    for a in tpl:
        lista.append(a)
    return Dataframe(pd.concat(lista, axis = 1))

# Posso specificare la colonna per index oppure default (indice numerico da 0)
def read_csv(csv: str, **kwargs) -> Dataframe:
    '''
    Read data from a csv file.

    :param csv: Path to the csv file.
    :param kwargs: Descrizione 2.

    :returns: A Dataframe reprentation of the csv.
    '''

    # transforming kwargs into a string
    if(len(kwargs)>1):
        string = str(list(kwargs.values()))
        value_str = re.sub("\['", "", string)
        value_str = re.sub("'\]","", value_str)
        return Dataframe(pd.read_csv(csv, index_col = value_str))
    else:
        return Dataframe(pd.read_csv(csv, index_col = False))



class Dataframe(pd.core.frame.DataFrame):
    '''Representation of a table, composed of rows and columns.'''

    def __init__(self, *args):
        '''
        Initialize a new Dataframe. 
        
        :param args: Create a copy of either a Series of an existing Dataframe.
        '''

        super().__init__(*args)
        
    @property
    def indexlocate(self) -> Locating:
        '''
        Locate a row by index.

        :returns: The row (Series).
        '''

        return Locating(self)

    def show(self):
        '''
        Print the contents of the Dataframe to screen
        '''

        print(self)
 
    def __getitem__(self, *args) -> Series | Dataframe:
        if ((type(args) == tuple) and (type(args[0]) == str)):
            return Series(super().__getitem__(args[0]))
        
        elif ((type(args) == tuple) and (type(args[0]) == int)):
            return Series(super().__getitem__(args[0]))

        elif ((type(args) == tuple) and (type(args[0]) == float)):
            return Series(super().__getitem__(args[0]))
        
        elif (type(args) == tuple and type(args[0]) == tuple):
            d = Dataframe()
            list_col = list()
            for elem in args[0]:
                s = Series(super().__getitem__(elem))
                list_col.append(s)
            tuple_col = tuple(list_col)
            d = concat_df(tuple_col)
            return d
     
        elif (isinstance(args[0], pd.core.series.Series)):
            temp = super().__getitem__(args[0])
            temp.reset_index(drop=True, inplace=True)
            return Dataframe(temp)

    # semplificazione: se aggiungo riga + lunga, perdo dati aggiuntivi, se + corta mette dei nan
    # one row (series), more rows (dataframe: you can also use concat())
    def append(self, obj):
        '''
        sadsdf

        :param obj: sadfasf
        '''

        if(not(isinstance(obj, Series)) and not(isinstance(obj,Dataframe))):
            raise TypeError("Can only add series or dataframe")

        elif(isinstance(obj, Series)):
            s = Series()
            for v, n in zip(obj.values, self.columns):
                s.loc[n] = v
            s.name = len(self.index)
            self.__init__(super().append(s, ignore_index=True))
        elif(isinstance(obj, Dataframe)):
            for k,r in obj.iterrows():
                self.loc[len(self.index)] = r
        
    def drop(self, item):
        '''
        sadfasfs
        
        :param item: dfasf
        '''

        if(isinstance(item, int)):
            super().drop(item, inplace=True)
            self.reset_index(drop=True, inplace=True)
        elif(isinstance(item, str)):
            super().drop(item, inplace=True, axis=1)

    def dropna(self, **kargs) -> Series | Dataframe:
        '''
        kjasdf

        :param kwargs: asdfjkh

        :returns: asdkfh
        '''

        if (len(kargs) > 1):
            raise Exception("Error. Axis must be 0 or 1 (row or column).")    
        elif ((kargs == {}) or (next(iter(kargs.keys())) == "axis" and next(iter(kargs.values())) == 0)):
            temp = super().dropna()
            if (len(temp.index) == 1):
                return Series(temp)
            else:
                return Dataframe(temp)

        elif (next(iter(kargs.keys())) == "axis" and next(iter(kargs.values())) == 1):
            temp = super().dropna(axis=1)
            if (len(temp.index) == 1):
                return Series(temp)
            else:
                return Dataframe(temp)
        else:
            raise ValueError("The axis value must be 0 or 1 (row or column respectively)")     

    def drop_duplicates(self) -> Series | Dataframe:
        '''
        asfasbjkasd
        
        :returns: askfjsalj
        '''

        self = super().drop_duplicates()
        if (len(self.index) == 1):
            return Series(self)
        else:
            return Dataframe(self)

    def isnull(self):
        '''
        asdlkfhasd

        :returns: asdfkjl
        '''

        return Dataframe(super().isnull())


    def rename(self, old_name: str, new_name: str):
        '''
        Rename a column from ``old_name`` to ``new_name``.

        :param old_name: The old name of the column. 
        :param new_name: The new name of the column. 
        '''
        
        super().rename(columns={old_name:new_name}, inplace=True)


class Locating(pd.core.indexing._iLocIndexer):
    '''Index-based locator for Dataframes'''

    def __init__(self, val):
        '''
        Initialize an index locator from a Dataframe
        
        :param val: The Dataframe
        '''
        
        super().__init__("iloc", val)
        self.df = pd.core.frame.DataFrame(val)

    def __getitem__(self, *args) -> Series | Dataframe:
        '''
        Return the element(s) in the required position(s).
        
        :param args: Index of the row to return or condition to apply to whole Dataframe.

        :returns: The element(s) in the required position(s).
        '''

        if (isinstance(args[0], int)):
            return Series(super().__getitem__(args[0]))
        else:
            return Dataframe(super().__getitem__(args[0]))
    
    def __setitem__(self, *args) -> Dataframe:
        '''
        Set the given position to the given value.

        :param args: Position and new value.

        :returns: The Dataframe.
        '''
                
        if(len(self.df.index) > args[0]):
            return Dataframe(super().__setitem__(args[0],args[1]))
        else:
            raise IndexError("Series indexer is out-of-bounds")
