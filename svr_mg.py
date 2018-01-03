# -*- coding: utf-8 -*-
"""
Created on Wed Jan 3 07:07:24 2018

@author: gmiliar (George Ch. Miliaresis)
Selective Variance Reduction by George Ch.Miliaresis
Ver. 2018.01 (winpython implementation, https://winpython.github.io/)
Details in https://github.com/miliaresis/SVR
           https://sourceforge.net/u/miliaresis/profile/
       and my web pages:  https://about.me/miliaresis
           https://sites.google.com/site/miliaresisg/
------------------------------------------------------------------------------
TO LOAD your data, define an appropriate header for example dataLST in file
          svr_data_headers.py.
For HELP see the comments in FUNCTION Processing_constants  within the
          file svrmg_myf.py, as well as the HELP.txt & the files
          MODIS_LST01data_Link.txt & DAYMET_Pdata_Link.txt (comments included)
          as well as the comments in function phead (file: svr_data_headers.py)
THEN return here and in  the main body of this progam (2nd function call)
          and CHANGE the NAME of the 2nd function from data_headers.dataLST to
          data_headers.XYZXY (XYZXY is the name of your data header) otherwise
          the data header dataLST will be used and the files within a subdir
          named data will be processed
------------------------------------------------------------------------------
"""
from svrmg_myf import Processing_constants
from svrmg_myf import data_imv_read
from svrmg_myf import MainRun
import svr_data_headers


#  1st FUNCTION CALL -------------- Defines clustering & tiff import options...
clustering_options, tiff_import_options = Processing_constants()
#  2nd FUNCTION CALL ---------------Selects the data file (header) to work with
[GeoExtent, FigureLabels, row, col, LabelHLatLonLST, LabelLST, LabelLSTxls,
 Lmin, Lmax, Rmin, Rmax, vectorsfile, LDatadir, Tiffimporttype, cluster_method
 ] = svr_data_headers.dataLST(clustering_options, tiff_import_options)
#  3rd FUNCTION CALL -------------- IMPORTS the data files, creates the vectors
data, row, col, continue1 = data_imv_read(row, col, vectorsfile, LDatadir,
                                          len(LabelLST), Tiffimporttype)
#  4th FUNCTION call -------------- Starts the processing of vectors ---------
if continue1 == 'yes':
    MainRun(data, row, col, GeoExtent, FigureLabels, LabelHLatLonLST, LabelLST,
            LabelLSTxls, Lmin, Lmax, Rmin, Rmax, cluster_method,
            clustering_options)
else:
    print('----> Check the data files')
