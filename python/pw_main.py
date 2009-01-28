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

import sys
import urllib
from urlparse import urlparse
from HTMLParser import HTMLParser

from pw_db import *
from pw_util import *
from pw_html_parser import *

urls = []
maxDepth = 1
force = 0
siteOnly = 1

# Initialize application parameters
if len(sys.argv) < 2:
    print " usage: pw_main.py URL [depth (1)] [force 0:1 (0)] [site only 0:1 (1)]"
    quit()

# The first site to crawl ...    
urls.append( sys.argv[1].strip().lower() )
urlparts = urlparse.urlparse(sys.argv[1])
hostname = urlparts[1]

if len(sys.argv) > 2:
    maxDepth = int(sys.argv[2])
    
if len(sys.argv) > 3:
    force = int(sys.argv[3])
    
if len(sys.argv) > 4:
    siteOnly = int(sys.argv[4])

urlDone = []
wordDone = []
database = db("mysql")

if force == 0:    
    urlDone = database.getAllSites()
    
wordDone = database.getAllWords()
    
for depth in range(0, maxDepth):
    newUrls = []
    for url in urls:
        # Only browse http content
        if not url.startswith("http"):
            continue
        
        print "[", depth+1, "] >>>", url, "<<<"
        
        if url in urlDone:
            print "already processed ..."
            continue
        
        urlDone.append(url)
            
        if not crawlIt(url):
            continue
        
        if siteOnly == 1 and url.find(hostname) < 0:
            print "This url is not part of the site"
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
    
    urls = []
    urls = newUrls[:]

database.dispose()

print "Done."

