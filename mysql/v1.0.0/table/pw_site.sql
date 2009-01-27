CREATE TABLE  `passwordcrawler`.`pw_site` (
  `id` int(10) unsigned NOT NULL auto_increment,
  `domain` varchar(45) NOT NULL,
  `created` datetime NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;