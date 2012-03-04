'''
Created on 2012/2/29

@author: EE
'''
import urllib2
import re
from ftplib import FTP
#from src.lib.BeautifulSoup import BeautifulSoup

site_url = "http://www.sec.gov/Archives/"


#login the ftp
#ftp = FTP('ftp.sec.gov')
#ftp.login()

f_idx = open('../../res/form.idx', 'r') 
lines = f_idx.readlines()

for line in lines:
    #parse the indexing file
    form_type    = line[0:12].strip()
    company_name = line[12:74].strip()
    CIK          = line[74:86].strip()
    date_filed   = line[86:98].strip()
    file_path    = line[98:].strip()
    
    #get the real path of the 10-K report
    if form_type.strip() == "10-K":
        print company_name, date_filed, file_path
        full_url = site_url + file_path
        print full_url        
        
        #fetch content using html protocol
        f_report = urllib2.urlopen(full_url)
        text = f_report.read()
        f_report.close()
        #print text
        
        #parse the html
        #soup = BeautifulSoup(text)
                
        
        
        
        