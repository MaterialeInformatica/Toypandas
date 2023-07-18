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

from .dataframe import *
from .series import *