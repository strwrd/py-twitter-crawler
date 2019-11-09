CREATE DATABASE IF NOT EXISTS `twitter-crawler-db`;

USE `twitter-crawler-db`;

DROP TABLE IF EXISTS `tweet`;

CREATE TABLE IF NOT EXISTS `tweet` (
  `id` char(36) NOT NULL,
  `text` text NOT NULL,

  PRIMARY KEY(`id`)
);