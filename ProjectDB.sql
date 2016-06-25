-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema ProjectDB
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema ProjectDB
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `ProjectDB` DEFAULT CHARACTER SET utf8 ;
USE `ProjectDB` ;

-- -----------------------------------------------------
-- Table `ProjectDB`.`cities`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ProjectDB`.`cities` (
  `cityid` INT NOT NULL AUTO_INCREMENT,
  `cityname` VARCHAR(64) NOT NULL,
  PRIMARY KEY (`cityid`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ProjectDB`.`streets`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ProjectDB`.`streets` (
  `streetid` INT NOT NULL AUTO_INCREMENT,
  `streetname` VARCHAR(64) NULL,
  `cityid` INT NULL,
  PRIMARY KEY (`streetid`),
  INDEX `cityid_idx` (`cityid` ASC),
  CONSTRAINT `cityid`
    FOREIGN KEY (`cityid`)
    REFERENCES `ProjectDB`.`cities` (`cityid`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ProjectDB`.`intersections`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ProjectDB`.`intersections` (
  `intersectionid` INT NOT NULL AUTO_INCREMENT,
  `street1` INT NULL,
  `street2` INT NULL,
  PRIMARY KEY (`intersectionid`),
  INDEX `street1_idx` (`street1` ASC),
  INDEX `street2_idx` (`street2` ASC),
  CONSTRAINT `street1`
    FOREIGN KEY (`street1`)
    REFERENCES `ProjectDB`.`streets` (`streetid`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `street2`
    FOREIGN KEY (`street2`)
    REFERENCES `ProjectDB`.`streets` (`streetid`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ProjectDB`.`incidents`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ProjectDB`.`incidents` (
  `incidentid` INT NOT NULL AUTO_INCREMENT,
  `streetid` INT NULL,
  `intersectionid` INT NULL,
  `address` VARCHAR(64) NULL,
  `severity` VARCHAR(64) NULL,
  `description` VARCHAR(140) NULL,
  PRIMARY KEY (`incidentid`),
  INDEX `streetid_idx` (`streetid` ASC),
  INDEX `intersectionid_idx` (`intersectionid` ASC),
  CONSTRAINT `streetid`
    FOREIGN KEY (`streetid`)
    REFERENCES `ProjectDB`.`streets` (`streetid`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `intersectionid`
    FOREIGN KEY (`intersectionid`)
    REFERENCES `ProjectDB`.`intersections` (`intersectionid`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ProjectDB`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ProjectDB`.`users` (
  `userid` INT NOT NULL AUTO_INCREMENT,
  `username` VARCHAR(45) NOT NULL,
  `password` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`userid`),
  UNIQUE INDEX `userid_UNIQUE` (`userid` ASC),
  UNIQUE INDEX `username_UNIQUE` (`username` ASC))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ProjectDB`.`change_requests`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ProjectDB`.`change_requests` (
  `requestid` INT NOT NULL AUTO_INCREMENT,
  `userid` INT NULL,
  `featureid` INT NULL,
  `changetype` VARCHAR(10),
  `streetid` INT NULL,
  `intersectionid` INT NULL,
  `startaddress` VARCHAR(64) NULL,
  `endaddress` VARCHAR(64) NULL,
  `description` VARCHAR(240) NULL,
  `approved` INT NULL DEFAULT NULL,
  PRIMARY KEY (`requestid`),
  INDEX `streetid_idx` (`streetid` ASC),
  INDEX `intersectionid_idx` (`intersectionid` ASC),
  INDEX `userid_idx` (`userid` ASC),
  CONSTRAINT `feature_id`
	FOREIGN KEY (`featureid`)
    REFERENCES `ProjectDB`.`features` (`featureid`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `street_id`
    FOREIGN KEY (`streetid`)
    REFERENCES `ProjectDB`.`streets` (`streetid`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `intersection_id`
    FOREIGN KEY (`intersectionid`)
    REFERENCES `ProjectDB`.`intersections` (`intersectionid`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `user_id`
    FOREIGN KEY (`userid`)
    REFERENCES `ProjectDB`.`users` (`userid`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ProjectDB`.`features`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ProjectDB`.`features` (
  `featureid` INT NOT NULL AUTO_INCREMENT,
  `streetid` INT NULL,
  `intersectionid` INT NULL,
  `startaddress` VARCHAR(64) NULL,
  `endaddress` VARCHAR(64) NULL,
  `description` VARCHAR(140) NULL,
  PRIMARY KEY (`featureid`),
  INDEX `streetid_idx` (`streetid` ASC),
  INDEX `intersectionid_idx` (`intersectionid` ASC),
  CONSTRAINT `streestid`
    FOREIGN KEY (`streetid`)
    REFERENCES `ProjectDB`.`streets` (`streetid`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `intersectionsid`
    FOREIGN KEY (`intersectionid`)
    REFERENCES `ProjectDB`.`intersections` (`intersectionid`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ProjectDB`.`administrators`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ProjectDB`.`administrators` (
  `userid` INT NOT NULL,
  PRIMARY KEY (`userid`),
  INDEX `fk_administrators_users1_idx` (`userid` ASC),
  UNIQUE INDEX `users_userid_UNIQUE` (`userid` ASC),
  CONSTRAINT `fk_administrators_users1`
    FOREIGN KEY (`userid`)
    REFERENCES `ProjectDB`.`users` (`userid`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
