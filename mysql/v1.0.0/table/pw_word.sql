CREATE TABLE  `passwordcrawler`.`pw_word` (
  `id` int(10) unsigned NOT NULL auto_increment,
  `word` varchar(45) NOT NULL,
  `created` varchar(45) NOT NULL,
  PRIMARY KEY  (`id`),
  CONSTRAINT unique_word UNIQUE (word)
) ENGINE=InnoDB AUTO_INCREMENT=1345 DEFAULT CHARSET=latin1;