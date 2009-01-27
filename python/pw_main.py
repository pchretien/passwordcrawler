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
urls = ["http://www.philippe-chretien.com/index.htm"]
done = []

database = db("mysql")

while depth < maxDepth:
    newUrls = []
    for url in urls:
        if not url.strip().startswith("http"):
            continue
                
        print "[", depth, "] >>>", url, "<<<"
        
        if url in done:
            print "already processed ..."
            continue
                    
        parser = pw_html_parser(url)
        if parser.startParsing() == True:        
            for word in parser.getWords():
                # Add the word to the database ...
                database.saveWord(word)
                               
            for anchor in parser.getAnchors():
                newUrls.append(anchor)
                
        done.append(url)
        
    depth += 1
    
    urls = []
    urls = newUrls[:]

database.dispose()

print "Done."

