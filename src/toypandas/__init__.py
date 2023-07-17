"""A library for educational purposes to simplify the syntax and notional machine of Python Pandas."""

import warnings # to avoid future warnings from pandas
warnings.simplefilter(action='ignore', category=FutureWarning)

import pandas as pd 
# from pandas import Series, DataFrame, concat
# from numpy import nan, isnan
import re
# import itertools
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 20, 'figure.figsize': (10, 8)}) # set font and plot size to be larger

# could be improved by also overriding loc
# "ilocate": iloc (numerical index)
# sempre reindex (anche se faccio una query, risultato avrà indici ordinati da 0)
# sum(), mean() stampa ancora tipi di dato originale
# describe is ok

from .dataframe import Dataframe
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


#def series(*arg):
#    lista = list()
#    for elem in arg:
#        lista.append(elem)
#    return series(lista)

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
