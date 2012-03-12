'''
Created on 2012/3/12

@author: EE
'''
import urllib2
import re
from ftplib import FTP
from lib.BeautifulSoup import BeautifulSoup 
from src.extract.extract import parseHeader

class Crawler:
    
    def __init__(self):
        self.site_url = "http://www.sec.gov/Archives/"                 
    
    def getTextFiles(self, idx):
        
        #read indexing files
        f_idx = open(idx, 'r') 
        lines = f_idx.readlines()  
        f_idx.close()  
        
        for line in lines:
            #parse the indexing file
            form_type    = line[0:12].strip()
            company_name = line[12:74].strip()
            CIK          = line[74:86].strip()
            date_filed   = line[86:98].strip()
            file_path    = line[98:].strip()
            
            #get the real path of the 10-K report
            if form_type.strip() == "10-K":    
                                                            
                full_url = self.site_url + file_path
                print full_url        
                new_filename = "../../res/" + CIK + "_" + company_name +  "_" +  date_filed + ".txt"
                print new_filename
                
                #download content using html protocol
                f_report = urllib2.urlopen(full_url)
                text = f_report.read()
                f_report.close()
                
                #Write into a file            
                f = open(new_filename, 'w')
                f.write(text)
                f.close()                                
    
        
    def getAllTextFiles(self, start_year, start_qtr):
        
        for year in range(2005, 2013):
            for qtr in range(1, 5):            
                if( year == start_year and qtr >= start_qtr) or year > start_year :
                    index_file_name = "../../res/" + str(year) + "_" + str(qtr) + ".idx"
                    print index_file_name
                    self.getTextFiles(index_file_name)
    
    
