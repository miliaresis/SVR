# -*- coding: utf-8 -*-
"""
Created on Mon May  9 16:37:09 2016

@author: gmiliar (George Ch. Miliaresis)
Selective Variance Reduction by George Ch.Miliaresis
Ver. 2016.02 (winpython implementation, https://winpython.github.io/)
Details in http://miliaresis.tripod.com
           https://sourceforge.net/u/miliaresis/profile/
       and Environmental Image Analysis Course
           https://dl.dropboxusercontent.com/u/16217596/webOctave/_octave.html
"""


def phead(xy, ML, row, col, x, x2, x3, Lmn, Lmx, Rmn, Rmx, vfile, LDIR, T, cm):
    """PRINT DATA HEADER.
        DATA files are in a subdir named eg. data, data2, in the dir where the
        3 scripts are stored. If a vector data file is used rows & cols of the
        initial images are required for image from vector reconstruction (other
        wise the rows & cols supplied in data header, are overwritten by those
        read from image files).
       The vector representation (csv file) of tif images
        1st column = vector ID (both data/no-data) are numbered in sequential
           order with ids.Then no data pixels are removed.During reconstruction
           for image creation,missing ids are considered as no-data pixels.
         2, 3, 4 columns = H, LAT, LON
         5- .... columns = multi-temporal data
         In vector representation, each CSV column is an image
       The tif image filenames in the data dir, are fixed :
         MASK, DEM, LAT (for y or latitude), LON (for X or longitude) and
         01, 02, 03, .....11, 12 .... THE NAMES ARE CASE SENSITIVE and they are
         determined automatically from the script (as well as the dimension of
         the feature space -> length of tics list), so you should preserve them
         in your data dir.
    """
    Headers_ALL = ['dataLST', 'data8dayLST', 'dataDAYMET']
    print('Labels for x-axis, y-axis of images/histograms:\n        ', ML)
    print('Geographic extent of data: ', xy)
    print('AXES legends & Tables headers for rows  & columns',
          '\n   ', x2, '\n   ', x, '\n   ', x3)
    print('Domain of histograms,     LST: ', Lmn, Lmx, ' RLST: ', Rmn, Rmx)
    print('Vectors file: ', vfile)
    print('Subdir with images or vector files= ', LDIR)
    print('Clustering method: ', cm)
    print('Method for TIF file import: ', T)
    print('row=', row, ' col=', col, '    valid with vectors-else overwritten')
    print('\nData headers available: ', Headers_ALL)


def dataLST(clustering_options, tiff_import_options):
    """MODIS AQUA 2007 night, monthly averaged LST """
    print('\n---> MODIS AQUA 2007 night-monthly LST, 0.05 deg, Lat/Lon, WGS84')
# Main figure labels (title, x-axis, y-axis)
    ML = ['LST, deg. Celsius', 'Longitude, deg.', 'Latitude, deg.']
    # Geograhic extent (X-LON-min, X-LON-max, Y-LAT-min, Y-LAT-max)
    xy = [-124, -112, 32, 44]
# tics for axes of figures and cross-correlation matrix
    x2 = ['J', 'F', 'M', 'A', 'M', 'J', 'J', 'A', 'S', 'O', 'N', 'D']
    x = ['H', 'Lat', 'Lon'] + x2
    x3 = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
          'August', 'September', 'October', 'November', 'December']
# Histograms domain for data (eg. LST) & reconstructed data (eg. RLST)
    Lmin = -30
    Lmax = 40
    Rmin = -15
    Rmax = 15
# clustering method: Kmeans refined by NBG
    clustering_method = clustering_options[1]
# PIL Library is used for TIF file import
    T = tiff_import_options[0]
# csv vector filename (if used instead of tif images)
    vfile = 'd.csv'
# Sub-directory for image files or vector matrix
    LDIR = 'data'
# Rows & Cols for image reconstruction from vectors (if vector csv is used)
    row = 240
    col = 240
    phead(xy, ML, row, col, x, x2, x3, Lmin, Lmax, Rmin, Rmax, vfile, LDIR,
          T, clustering_method)
    return (xy, ML, row, col, x, x2, x3, Lmin, Lmax, Rmin, Rmax, vfile, LDIR,
            T, clustering_method)


def data8dayLST(clustering_options, tiff_import_options):
    """8-day LST data, 1-km, SW USA, MODLAND Integerized Sinusoidal Grid  """
    print('\n--->8-day LST data, 1-km, SW USA, MODLAND Integr. Sin. Grid')
# Main figure labels (title, x-axis, y-axis)
    ML = ['LST, deg. Celsius', 'X, km', 'Y, km']
    # Geograhic extent (X-LON-min, X-LON-max, Y-LAT-min, Y-LAT-max)
    xy = [-11119.5, -10007.5, 3333.9, 4447.8]
# tics for axes of figures and cross-correlation matrix
    x2 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13',
          '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24',
          '25', '26', '27', '28', '39', '30', '31', '32', '33', '34', '35',
          '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46']
    x = ['H', 'Y', 'X'] + x2
    x3 = x2
# Histograms domain for data (eg. LST) & reconstructed data (eg. RLST)
    Lmin = -30
    Lmax = 40
    Rmin = -15
    Rmax = 15
# clustering method: Kmeans refined by NBG
    clustering_method = clustering_options[1]
# SKITimage Librady is used for TIF file import
    T = tiff_import_options[1]
# csv vector filename (if used instead of tif images)
    vfile = 'LST8day.csv'
# Sub-directory for image files or vector matrix
    LDIR = 'data3'
# Rows & Cols for image reconstruction from vectors (if vector csv is used)
    row = 1200
    col = 1200
    phead(xy, ML, row, col, x, x2, x3, Lmin, Lmax, Rmin, Rmax, vfile, LDIR, T,
          clustering_method)
    return (xy, ML, row, col, x, x2, x3, Lmin, Lmax, Rmin, Rmax, vfile, LDIR,
            T, clustering_method)


def dataDAYMET(clustering_options, tiff_import_options):
    """Annual DAYMET precipitation data, 1-km, SW USA  """
    print(""""\n---> DAYMET annual precipitation data for SW USA, Lambert
    Conformal Conic projection, 1 km""")
# Main figure labels (title, x-axis, y-axis)
    ML = ['Precipitation, mm/yr', 'X, km', 'Y, km']
    # Geograhic extent (X-LON-min, X-LON-max, Y-LAT-min, Y-LAT-max)
    xy = [-1950, -725, -1144, 222]
# tics for axes of figures and cross-correlation matrix
    x2 = ['2003', '2004', '2005', '2006', '2007', '2008', '2009',
          '2010', '2011', '2012', '2013', '2014']
    x = ['H', 'Y', 'X'] + x2
    x3 = ['2003', '2004', '2005', '2006', '2007', '2008', '2009',
          '2010', '2011', '2012', '2013', '2014']
# Histograms domain for data (eg. LST) & reconstructed data (eg. RLST)
    Lmin = 0
    Lmax = 1500
    Rmin = -600
    Rmax = 600
# Clustering method: Kmeans refined by NBG
    clustering_method = clustering_options[1]
# SKITimage Librady is used for TIF file import
    T = tiff_import_options[1]
# csv vector filename (if used instead of tif images)
    vfile = 'daymet.csv'
# Sub-directory for image files or vector matrix
    LDIR = 'data2'
# Rows & Cols for image reconstruction from vectors (if vector csv is used)
    row = 1366
    col = 1225
    phead(xy, ML, row, col, x, x2, x3, Lmin, Lmax, Rmin, Rmax, vfile, LDIR, T,
          clustering_method)
    return (xy, ML, row, col, x, x2, x3, Lmin, Lmax, Rmin, Rmax, vfile, LDIR,
            T, clustering_method)
