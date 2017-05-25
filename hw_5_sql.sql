-- MySQL dump 10.13  Distrib 5.7.17, for Win64 (x86_64)
--
-- Host: localhost    Database: my_scheme_py
-- ------------------------------------------------------
-- Server version	5.7.18-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `artificial_intelligence`
--

DROP TABLE IF EXISTS `artificial_intelligence`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `artificial_intelligence` (
  `_ID` int(11) NOT NULL AUTO_INCREMENT,
  `_NAME` char(32) NOT NULL,
  `_DEVELOPER` char(32) NOT NULL,
  PRIMARY KEY (`_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `artificial_intelligence`
--

LOCK TABLES `artificial_intelligence` WRITE;
/*!40000 ALTER TABLE `artificial_intelligence` DISABLE KEYS */;
INSERT INTO `artificial_intelligence` VALUES (1,'|shave|','|SLADE|'),(2,'|shave2|','|SLADE2|'),(3,'|shave3|','|SLADE3|');
/*!40000 ALTER TABLE `artificial_intelligence` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `artificial_network`
--

DROP TABLE IF EXISTS `artificial_network`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `artificial_network` (
  `_ID` int(11) NOT NULL AUTO_INCREMENT,
  `_NAME` varchar(45) NOT NULL,
  PRIMARY KEY (`_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `artificial_network`
--

LOCK TABLES `artificial_network` WRITE;
/*!40000 ALTER TABLE `artificial_network` DISABLE KEYS */;
INSERT INTO `artificial_network` VALUES (1,'|shave|'),(2,'|shave2|'),(3,'|shave3|');
/*!40000 ALTER TABLE `artificial_network` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `human_ai`
--

DROP TABLE IF EXISTS `human_ai`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `human_ai` (
  `_ID` int(11) NOT NULL AUTO_INCREMENT,
  `_NAME` varchar(32) NOT NULL,
  `_DEVELOPER` varchar(32) NOT NULL,
  `_GENDER` varchar(32) NOT NULL,
  `_AGE` int(11) NOT NULL,
  PRIMARY KEY (`_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `human_ai`
--

LOCK TABLES `human_ai` WRITE;
/*!40000 ALTER TABLE `human_ai` DISABLE KEYS */;
INSERT INTO `human_ai` VALUES (1,'|shave|','|SLADE|','22',22),(2,'|shave2|','|SLADE2|','22',22),(3,'|shave3|','|SLADE3|','22',22);
/*!40000 ALTER TABLE `human_ai` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-04-27 17:06:30
