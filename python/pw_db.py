## passwordCRAWLER ##
#
# Crawl websites to generate password dictionnaries
# Copyright (C) 2008,2009  Philippe Chretien
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License Version 2
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

from pw_db_mysql import *

class db:
    __dbInstance = None
    
    def __init__(self, dbName):
        if(dbName == "mysql"):
            self.__dbInstance = db_mysql()
        if(dbName == "mssql"):
            self.__dbInstance = None
        if(dbName == "oracle"):
            self.__dbInstance = None
            
    def saveWord(self, word):
        return self.__dbInstance.saveWord(word)
    
    def getWordId(self, word):
        return self.__dbInstance.getWordId(word)
    
    def getAllWords(self):
        return self.__dbInstance.getAllWords()
    
    def saveSite(self, url):
        return self.__dbInstance.saveSite(url)
    
    def getAllSites(self):
        return self.__dbInstance.getAllSites()
    
    def saveSiteWord(self, site_id, word_id):
        return self.__dbInstance.saveSiteWord(site_id, word_id)
            
    def dispose(self):
        self.__dbInstance.dispose()