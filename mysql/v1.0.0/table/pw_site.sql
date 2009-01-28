CREATE TABLE  `passwordcrawler`.`pw_site` (
  `id` int(10) unsigned NOT NULL auto_increment,
  `url` varchar(45) NOT NULL,
  `created` datetime NOT NULL,
  PRIMARY KEY  (`id`),
  CONSTRAINT unique_url UNIQUE (url)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;