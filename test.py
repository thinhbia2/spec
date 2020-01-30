import time
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.image as img
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
from scipy.optimize import curve_fit
import scipy.integrate as integrate
import scipy.special as special
from scipy.integrate import quad
import scipy.signal
import numpy as np

import rfiles
import prdata

from lmfit.models import LorentzianModel, SplitLorentzianModel

import tkinter as tk
from tkinter import filedialog
from tkinter import *

import os

if os.name == 'nt':
	dir_slash = '\\' #Windows
else:
	dir_slash = '/' #others

matplotlib.rcParams.update({'font.size': 11})

exposure_time = 10 #integration time for each spectrum
legend_name = 'emitter'
title_name = 'PL spectra'

root = tk.Tk()
root.withdraw()
files = filedialog.askopenfilenames()

save_path = os.path.dirname(files[0]) + dir_slash + 'Results_' + time.strftime("%Y%m%d_%H%M%S")
os.mkdir(save_path)

if files[0].lower().endswith('.spe'):
	for i in files:
		data = rfiles.load_spe(i)
		file_saved_name = os.path.basename(i)
		np.savetxt(save_path + dir_slash + file_saved_name.lower().replace(".spe", "_raw.csv"), data, delimiter = ',')
		#routine(X)


elif files[0].lower().endswith('.txt'):
	data = rfiles.load_txt(files[0])
	for i in files[1:]:
		data1 = rfiles.load_txt(i)
		data = np.concatenate((data, data1[:, 1][:, np.newaxis]), axis=1)
	file_saved_name = os.path.basename(files[0])
	np.savetxt(save_path + dir_slash + file_saved_name.lower().replace(".txt", "_raw.csv"), data, delimiter = ',')


# def routine(X)
#     fig, ax = plt.subplots()
#     image1 = ax.imshow(X[1:, 1].T, cmap=plt.cm.rainbow, interpolation='none', aspect='auto')
#     plt.xlabel('Wavelength (nm)')
#     plt.ylabel('Time (sec)')
#     plt.title('PL time series')
#     plt.colorbar(image1,shrink=0.6)
    
#     #plt.tight_layout()
#     plt.savefig('C:\\Users\\Toan\\Processed_data\\PL_time_series_zoomed%s.jpg' % i, dpi = 600, format = 'jpg')
#     df.to_csv('C:\\Users\\Toan\\Processed_data\\PL_time_series_data_zoomed%s.csv' % i, index = False, header = False)
#     plt.gcf().clear()
#     del df
#     del image1
# def _3Lorentzian(x, amp1, cen1, sig1, amp2,cen2,sig2):
#     return (amp1*sig1/(np.pi*((x-cen1)**2+sig1**2)) + amp2*sig2/(np.pi*((x-cen2)**2+sig2**2)))

# popt, pcov = curve_fit(_3Lorentzian, data[:, 0], data[:, 1], p0=[100,580,16,30,630,20])
# print(popt)
# #print(out.fit_report(min_correl=0.25))
# plt.plot(data[:,0], data[:,1], 'r:', label='raw')
# plt.plot(data[:,0], _3Lorentzian(data[:, 0], *popt), 'k-', label='Fit')
# plt.legend(loc='best')
# plt.show()


print('Done')
