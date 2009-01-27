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
            
    def saveDevice(self, name, address, username):
        try:
            # First time insertion to the bt_device table. If the address 
            # already exist the database raise an exception 
            cursor = self.__conn.cursor ()
            cursor.execute ("insert into bt_device(address, createdby, created) values (%s,%s,NOW())", (address, username) )
            cursor.close ()
        except:
            # Nothing to do here. This exception is raised mostly because the 
            # device already exist in the database
            None
            
        if len(name) > 0:
            try:
                # Try a first insertion. If the address already exist, a database
                # exception is throwed
                cursor = self.__conn.cursor ()
                cursor.execute ("insert into bt_device_name(address, name, createdby, created, updated) values (%s,%s,%s,NOW(),NOW())", (address, name, username) )
                cursor.close ()
            except:
                try:
                    # The address already exist, We then check if the
                    # name is the same
                    cursor = self.__conn.cursor ()
                    cursor.execute ("select count(*) from bt_device_name where address=%s and name=%s", (address, name))
                    exist = int(cursor.fetchone ()[0])
                    cursor.close ()

                    # The name is different. We update the name of the
                    # device to match the new one
                    if exist == 0:
                        print "    bluetooth device name changed to %s" % (name)
                        cursor = self.__conn.cursor ()
                        cursor.execute ("update bt_device_name set name=%s, createdby=%s, updated=NOW() where address=%s", (name, username, address) )
                        cursor.close ()
                except:
                    print "    bluetooth device name %s update failed" % (name)
                    
        self.__conn.commit()

    def savePing(self, address, location, username):
        # Keep a timestamp of every time the address is recorded in a specific
        # location
        cursor = self.__conn.cursor ()
        cursor.execute ("insert into bt_ping(address, location, created, createdby) values (%s,%s,NOW(),%s)", (address, location, username) )
        cursor.close ()
        
        self.__conn.commit()
        