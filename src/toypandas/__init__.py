"""A library for educational purposes to simplify the syntax and notional machine of Python Pandas."""


# -- Configuration -------------------------------------------------------------------------------------
import warnings # to avoid future warnings from pandas
warnings.simplefilter(action='ignore', category=FutureWarning)

import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 20, 'figure.figsize': (10, 8)}) # set font and plot size to be larger


# -- Import submodule content --------------------------------------------------------------------------
from .dataframe import *
from .series import *