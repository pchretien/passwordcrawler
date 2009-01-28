-------------------------------------------------------------------------------
-- passwordCRAWLER --
-------------------------------------------------------------------------------

Python files:
	- python/pw_db.py
	- python/pw_db_mysql.py
	- python/pw_main.py
	- pw_html_parser.py
	
Database files:
	- mysql/v1.0.0/table/pw_word.sql
	- mysql/v1.0.0/table/pw_site.sql
	- mysql/v1.0.0/table/pw_word_site_xref.sql
	
Other files:
	- README.txt 			this file
	- LICENSE.txt 			GPL license
	- .project			Eclipse project file
	- .pydevproject			Eclipse PyDev project file
	- python/pw_db_mysql.config	MySql connection parameters
	
Dependencies:
	- MySql database server
	  http://www.mysql.com/
	  
	- MySqldb library for python
	  http://sourceforge.net/projects/mysql-python

This program crawls websites to generate password dictionnaries. All the 
password generation code is provided as uncoupled plugin so it is easy to 
reuse the actual crawler for some other purpose.

You will find the latest version of this code at the following address:
http://github.com/pchretien

You can contact me at the following email address:
philippe.chretien@gmail.com

Thank you,

Philippe Chrétien