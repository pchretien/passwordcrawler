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
from HTMLParser import HTMLParser

from pw_db import *
from pw_html_parser import *

depth = 0
maxDepth = 4
urls = ["http://www.astrophoto.ca"]
urlDone = []
wordDone = []
database = db("mysql")

def crawlIt(url):
    if url.lower().find(".google.") > -1:
        print "Its a crawler eat crawler world ..."
        return False
    
    if url.lower().find(".live.") > -1:
        print "Its a crawler eat crawler world ..."
        return False
    
    if url.lower().find(".yahoo.") > -1:
        print "Its a crawler eat crawler world ..."
        return False
    
    return True

while depth < maxDepth:
    newUrls = []
    for url in urls:
        # Clear trailing and tailing white spaces
        url = url.strip().lower()
        
        # Only browse http content
        if not url.startswith("http"):
            continue
        
        print "[", depth, "] >>>", url, "<<<"
        
        if url in urlDone:
            print "already processed ..."
            continue
        
        urlDone.append(url)
            
        if not crawlIt(url):
            continue
                    
        parser = pw_html_parser(url)
        if parser.startParsing() == True:        
            
            for word in parser.getWords():
                
                # This avoid a unique constraint exception to be 
                # raised by the database
                if word in wordDone:
                    continue
                
                # Add the word to the database ...
                word = word.lower()
                if database.saveWord(word):
                    print word
                    wordDone.append(word)
                                                   
            for anchor in parser.getAnchors():
                newUrls.append(anchor)
                
    depth += 1
    
    urls = []
    urls = newUrls[:]

database.dispose()

print "Done."

