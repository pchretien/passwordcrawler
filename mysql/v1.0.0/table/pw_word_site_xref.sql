CREATE TABLE  `passwordcrawler`.`pw_word_site_xref` (
  `id` int(10) unsigned NOT NULL auto_increment,
  `word_id` int(10) unsigned NOT NULL,
  `site_id` int(10) unsigned NOT NULL,
  `created` datetime NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;