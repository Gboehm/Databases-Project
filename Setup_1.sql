INSERT INTO `projectdb`.`users` (`username`, `password`) VALUES ('Gunnar', '12345');
INSERT INTO `projectdb`.`administrators` (`userid`) VALUES ('1');
INSERT INTO `projectdb`.`cities` (`cityname`) VALUES ('Boston');
INSERT INTO `projectdb`.`streets` (`streetname`,`cityid`) VALUES ('Comm Ave','1');
INSERT INTO `projectdb`.`streets` (`streetname`,`cityid`) VALUES ('Mass Ave','1');
INSERT INTO `projectdb`.`streets` (`streetname`,`cityid`) VALUES ('Huntington Ave','1');
INSERT INTO `projectdb`.`intersections` (`street1`,`street2`) VALUES ('3', '2');
INSERT INTO `projectdb`.`features` (`streetid`, `description`) VALUES ('3', 'Bike Path');
INSERT INTO `projectdb`.`features` (`streetid`, `description`) VALUES ('1',' Buffered Bike Path');
INSERT INTO `projectdb`.`incidents` (`streetid`, `address`,`severity`) 
VALUES ('2', '484 Massachusetts Ave', 'Light: No Injuries');
INSERT INTO `projectdb`.`incidents` (`streetid`, `address`,`severity`,`description`) 
VALUES ('1', '281 Comm Ave', 'Fatal', 'Head decapitated. Body continued pedaling for several miles.');
INSERT INTO `projectdb`.`incidents` (`intersectionid`, `address`,`severity`,`description`) 
VALUES ('1', 'Huntington Ave & Mass Ave', 'Light: Scrapes and Bruises', 'Driver at fault, blind right turn.');
INSERT INTO `projectdb`.`features` (`streetid`,`startaddress`,`endaddress`,`description`)
 VALUES ('2', '25', '860','Shared Bike Lane');
INSERT INTO `projectdb`.`features` (`streetid`,`startaddress`,`endaddress`,`description`)
 VALUES ('3', '464', '525','Shared Bike Lane');
 INSERT INTO `projectdb`.`features` (`intersectionid`, `description`)
 VALUES ('1', 'Bike Box');
 INSERT INTO `projectdb`.`features` (`streetid`,`startaddress`,`description`)
 VALUES ('2', '320','Hubway Station');