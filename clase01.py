# lineplot.py                                                   
import numpy as np
import pylab as pl
# Make an array of x values
x = [1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017]                                           
#Make an array of y values for each x value                                
y = [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 2, 1, 2, 2, 2, 2, 3, 1, 2, 1, 1, 2]
# use pylab to plot x and y                  
pl.plot(x, y)
#Show the plot on the screen                             
pl.savefig('temp1.png')
