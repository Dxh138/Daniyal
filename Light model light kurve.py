# -*- coding: utf-8 -*-
"""
Created on Thu Mar 27 16:31:33 2025

@author: daniy
"""


import lightkurve as lk 
import numpy as np 
from lightkurve import search_targetpixelfile, search_lightcurve
import matplotlib.pyplot as plt
import pandas as pd

search_result = lk.search_lightcurve('K2-237', author='K2')

#download the lightcurve - can use e.g. search_result[0,5].download_all() to only download the first 5
lc_collection = search_result.download_all()
#remove any NaNs from the fluxes, as these like to cause problems
lc = lc_collection.stitch().remove_nans()

time = lc.time.value
flux = lc.flux.value
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 5))  # Bigger figure
plt.scatter(time, flux, s=5, alpha=0.5, color='red')  # Smaller points, transparency
plt.xlim(2860,2880)
plt.xlabel("Time (days)")
plt.ylabel("Flux")
plt.title("Light Curve of K2-237")
plt.grid(True, linestyle="--", alpha=0.7)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.show()

