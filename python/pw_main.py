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
urls = ["  http://www.Astrophoto.CA  "]

urlDone = []
wordDone = []
database = db("mysql")

def crawlIt(url):
    ret = True
    
    if url.lower().find(".google.") > -1:
        ret = False
    
    if url.lower().find(".live.") > -1:
        ret = False
    
    if url.lower().find(".yahoo.") > -1:
        ret = False
        
    if not ret:
        print "Its a crawler eat crawler world ..."
    
    return ret

# Make sure the URLs passed in parameters are lower case.
# All urls found by the parser are returned in lower case.
for i in range (0,len(urls)):
    urls[i] = urls[i].strip().lower()
    
while depth < maxDepth:
    newUrls = []
    for url in urls:
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
        
        site_id = database.saveSite(url)
        if site_id == -1:
            print "Failed to write/read the url to the database ..."
            continue
                    
        parser = pw_html_parser(url)
        if parser.startParsing() == True:     
            for word in parser.getWords():
                
                # This avoid a unique constraint exception to be 
                # raised by the database
                if not word in wordDone:
                    wordDone.append(word)
                    if database.saveWord(word):
                        print word                        
                
                # Add the word to the database ...
                word_id =  database.getWordId(word)                
                if word_id > -1:
                    database.saveSiteWord(site_id, word_id)
                                                   
            for anchor in parser.getAnchors():
                newUrls.append(anchor)
                
    depth += 1
    
    urls = []
    urls = newUrls[:]

database.dispose()

print "Done."

