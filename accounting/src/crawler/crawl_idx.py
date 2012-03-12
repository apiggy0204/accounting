'''
Created on 2012/3/2

@author: Chris Chao
'''
from ftplib import FTP
import sys

def getbinary(ftp, filename, outfile=None):
    # fetch a binary file
    if outfile is None:
        outfile = sys.stdout    
    ftp.retrbinary("RETR " + filename, outfile.write)
    
def gettext(ftp, filename, outfile=None):
    # fetch a text file
    if outfile is None:
        outfile = sys.stdout
    # use a lambda to add newlines to the lines read from the server
    ftp.retrlines("RETR " + filename, lambda s, w=outfile.write: w(s+"\n"))    

def getIndexFiles(start_year, start_qtr):
    #login the ftp
    ftp = FTP('ftp.sec.gov')
    ftp.login()
    
    for year in range(2005, 2013):    
        for QTR in range(1, 5):            
            if (year==start_year and QTR>=start_qtr) or year > start_year:
                source_path = "edgar/full-index/" + str(year) + "/QTR" + str(QTR) + "/form.idx"
                dest_path   = "../../res/" + str(year) + "_" + str(QTR) + ".idx"
                print source_path
                print dest_path     
                dest = open(dest_path, "wb")
                getbinary(ftp, source_path , dest)
                
    ftp.close()

getIndexFiles(2005, 1)