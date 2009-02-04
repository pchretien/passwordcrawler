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