'''Descrizione modulo'''

from __future__ import annotations

import pandas as pd

from .series import Series


def concat(*arg) -> Dataframe:
    '''
    Concatenate an arbitrary number of series #
    Concatenate an arbitrary number of dataframe #

    :param arg: Descrizione.

    :returns: Descr return.
    '''

    lista = list()
    df = True
    for a in arg:
        lista.append(a)
        df = df and isinstance(a,Dataframe) # concat dataframes or series
    if(df == True):
        return Dataframe(pd.concat(lista, ignore_index=True))
    else:
        return Dataframe(pd.concat(lista, axis = 1))

def concat_df(tpl) -> Dataframe:
    '''
    Descrizione generica.

    :param tpl: Descrizione. - non si capisce cosa sia tpl dal nome (tupla?) - se la funzione e` concat df ha senso mettere df come nome argomento

    :returns: Descr return.
    '''

    lista = list()
    for a in tpl:
        lista.append(a)
    return Dataframe(pd.concat(lista, axis = 1))

# Posso specificare la colonna per index oppure default (indice numerico da 0)
def read_csv(csv: str, **kwargs) -> Dataframe:
    '''
    Descrizione generica.

    :param csv: Descrizione.
    :param kwargs: Descrizione 2.

    :returns: Descr return.
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
    '''Descrizione classe'''

    def __init__(self, *args):
        '''
        asdflkjs
        
        :param args: asdfas
        '''

        super().__init__(*args)
        
    @property
    def indexlocate(self) -> Locating:
        '''
        adshf

        :returns: adskfh
        '''

        return Locating(self)

    def show(self):
        '''
        ti ho corretto la funzione -> prima ritornavi self (te la stampava solo perche` sei in modalita` interattiva).
        ora ti stampa correttamente sempre

        :returns: sdlkfj
        '''

        print(self)
 
    def __getitem__(self, *args) -> Series | Dataframe:
        '''
        adfag
        
        :param args:

        :returns: asdfsaf
        '''

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

    def isnull(self) -> Dataframe:
        '''
        asdlkfhasd

        :returns: asdfkjl
        '''

        return Dataframe(super().isnull())


    def rename(self, *args):
        '''
        laskdhf

        :param args: askjdfhk
        '''
        
        if (len(args) == 2):
            super().rename(columns={args[0]:args[1]}, inplace=True)
        else:
            raise ValueError("I expect two arguments: old column name, new column name")


class Locating(pd.core.indexing._iLocIndexer):
    '''descr classe'''

    def __init__(self, val):
        '''
        defasdf
        
        :param val: dafaf
        '''
        
        super().__init__("iloc", val)
        self.df = pd.core.frame.DataFrame(val)

    def __getitem__(self, *args) -> Series | Dataframe:
        '''
        dafdasf
        
        :param args: sdafsaf

        :returns: sadfj
        '''

        if (isinstance(args[0], int)):
            #print(series(super().__getitem__(args[0])))
            return Series(super().__getitem__(args[0]))
        else:
            return Dataframe(super().__getitem__(args[0]))
    
    def __setitem__(self, *args) -> Dataframe:
        '''
        sadlkfjsldf

        :param args: asdfsf

        :returns: sadlfkjasl
        '''
        
        if(len(self.df.index) > args[0]):
            return Dataframe(super().__setitem__(args[0],args[1]))
        else:
            raise IndexError("Series indexer is out-of-bounds")
