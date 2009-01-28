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

import urllib
import urlparse
from HTMLParser import HTMLParser

class pw_html_parser(HTMLParser):
    __MINIMUM_LENGTH = 4
    
    __url = ""
    __words = []
    __anchors = []

    def __init__(self, url):
        self.__url = url
        HTMLParser.__init__(self)
        
    def startParsing(self):
        try:
            page = urllib.urlopen(self.__url).read()
        except:
            print "failed to open the page %s ", (self.__url)
            return False
        
        try:
            self.feed(page)
            self.close()
        except:
            print "failed to parse the page %s " % (self.__url)
            return False
        
        return True
        
    def handle_data(self, data):
        separators = (".", ",", "'", ";", ":", "!", "?", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+", "=", "{", "}", "[", "]", "|", "\\", "\"", "<", ">", "/", "~", "`")
        for sep in separators:
            data = data.replace(sep, " ")
            
        if len(data.strip()) < self.__MINIMUM_LENGTH:
            return
        
        tokens = data.split()
        for word in tokens:
            
            # Numbers are rejected ...
            if word.isdigit():
                continue
            
            if len(word) >= self.__MINIMUM_LENGTH:
                # Add the word to the database ...
                self.__words.append(word)
                
    def handle_starttag(self, tag, attrs):
        if tag == "a":
            for k, v in attrs:
                if k == "href":
                    anchor = urlparse.urljoin(self.__url, v, allow_fragments = True)
                    self.__anchors.append(anchor)
                    break
    
    def getWords(self):
        return self.__words
    
    def getAnchors(self):
        return self.__anchors
    
    
    
    