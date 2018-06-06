-- MySQL dump 10.13  Distrib 5.7.17, for Win64 (x86_64)
--
-- Host: localhost    Database: syoku
-- ------------------------------------------------------
-- Server version	5.7.19-log

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
-- Table structure for table `members`
--

DROP TABLE IF EXISTS `members`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `members` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `password` varchar(10) COLLATE utf8mb4_unicode_ci NOT NULL,
  `useremail` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `usergender` varchar(30) COLLATE utf8mb4_unicode_ci NOT NULL,
  `userbirth` date NOT NULL,
  `useraddress` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `userphone` varchar(30) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `members`
--

LOCK TABLES `members` WRITE;
/*!40000 ALTER TABLE `members` DISABLE KEYS */;
INSERT INTO `members` VALUES (13,'Ann','ann','Ann@gmail.com','Female','2018-06-01','台北市中正區','0910-000-000'),(14,'Betty','betty','Betty@gmail.com','Female','2018-06-02','台北市中山區','0910-111-111'),(15,'Cindy','cindy','Cindy@gmail.com','Female','2018-06-03','台北市大同區','0910-222-222'),(16,'Hank','hank','Hank@gmail.com','Male','2018-06-04','台北市信義區','0910-333-333'),(17,'Tom','tom','Tom@gmail.com','Male','2018-06-05','新北市中和區','0910-444-444'),(18,'John','john','John@gmail.com','Male','2018-06-06','新北市永和區','0910-555-555'),(24,'linkin','111111','linkin@yahoo.com','Male','2018-05-02','usa','0923333333'),(25,'私房料理家','11111','cook@msn.com','Female','2018-05-10','tokyo','0922222444'),(26,'小當家','12345','xiaodj@qq.com','Male','2018-04-05','北京','0911222333'),(27,'阿基師','12345','ajishi@iii.com','Male','2016-02-13','復興南路一段','0922111111'),(28,'詹姆士','12345','james@iii.com','Male','2011-10-06','型難大煮廚','0912345678');
/*!40000 ALTER TABLE `members` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-06-06 17:09:01
