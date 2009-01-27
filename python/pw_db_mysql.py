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
            cursor.execute ("insert into pw_word(word, created) values (%s,NOW())", (word.lower()) )
            cursor.close ()        
            self.__conn.commit()
            print word
        except:
            None
            
    
        