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

#login the ftp
ftp = FTP('ftp.sec.gov')
ftp.login()

for year in range(2005, 2012):    
    for QTR in range(1, 5):
        source_path = "edgar/full-index/" + str(year) + "/QTR" + str(QTR) + "/form.idx"
        dest_path   = "../../res/form" + str(year) + "_" + str(QTR) + ".idx"
        print source_path
        print dest_path     
        dest = open(dest_path, "wb")
        getbinary(ftp, source_path , dest)
        
ftp.close()        

#fetch content using ftp protocol
#FTP.storbinary(command, file[, blocksize, callback, rest])
#print ftp.sendcmd("cd edgar/full-index/")        
#ftp.retrbinary( "RETR edgar/full-index/2010/QTR1/form.idx", "../../res/2010/form1.idx")
