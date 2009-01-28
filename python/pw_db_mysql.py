## passwordCRAWLER ##
#
# Crawl websites to generate password dictionnaries
# Copyright (C) 2008,2009  Philippe Chretien
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
#
# You will find the latest version of this code at the following address:
# http://github.com/pchretien
#
# You can contact me at the following email address:
# philippe.chretien@gmail.com

import MySQLdb

class db_mysql:
    # Database connection default parameter values
    __server = "localhost"
    __username = "root"
    __password = ""
    
    __conn = None
    
    def __init__(self):
        print "reading pw_db_mysql.config configuration file"
        file = open("./pw_db_mysql.config")
        try:
            lines = file.read().splitlines()
            for line in lines:
                print line
                tokens = line.split('=')
                if tokens[0] == "server":
                    self.__server = tokens[1]
                if tokens[0] == "username":
                    self.__username = tokens[1]
                if tokens[0] == "password":
                    self.__password = tokens[1]
        except:
            None
        finally:
            file.close()
            
        print "connecting to the database ..."
        self.__conn = MySQLdb.connect (host = self.__server, user = self.__username, passwd = self.__password, db = "passwordcrawler")
      
    def __del__(self):
           self.dispose()
           
    def dispose(self):
        if(self.__conn != None):
            self.__conn.close()
            self.__conn = None
            
    def saveWord(self, word):
        try:
            cursor = self.__conn.cursor ()
            cursor.execute ("insert into pw_word(word, created) values (%s,NOW())", (word) )
            cursor.close ()        
            self.__conn.commit()
        except:
            return False  
        
        return True          
       
        
    def getWordId(self, word):
        ret = -1        
        try:
            cursor = self.__conn.cursor ()
            cursor.execute ("select id from pw_word where word = %s", (word) )
            ret = int(cursor.fetchone ()[0])
            cursor.close ()
        except:
            None
            
        return ret
    
    
    def saveSite(self, url):
        ret = -1        
        try:
            cursor = self.__conn.cursor ()
            cursor.execute ("insert into pw_site(url, created) values (%s,NOW())", (url) )
            cursor.close ()   
            self.__conn.commit() 
        except:
            # The url already exist ...
            None 
            
        try:
            cursor = self.__conn.cursor ()
            cursor.execute ("select id from pw_site where url = %s", (url) )
            ret = int(cursor.fetchone ()[0])
            cursor.close ()
                 
        except:
            return ret
        
        return ret
            
    def saveSiteWord(self, site_id, word_id):
        try:
            cursor = self.__conn.cursor ()
            cursor.execute ("insert into pw_word_site_xref(site_id, word_id, created) values (%s,%s,NOW())", (site_id, word_id) )
            cursor.close ()   
            self.__conn.commit() 
        except:
            None 
        