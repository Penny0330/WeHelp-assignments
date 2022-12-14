-- MySQL dump 10.13  Distrib 8.0.30, for Win64 (x86_64)
--
-- Host: localhost    Database: website
-- ------------------------------------------------------
-- Server version	8.0.30

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `like_member`
--

DROP TABLE IF EXISTS `like_member`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `like_member` (
  `message_id` bigint NOT NULL,
  `member_id` bigint NOT NULL,
  PRIMARY KEY (`message_id`,`member_id`),
  KEY `member_id` (`member_id`),
  CONSTRAINT `like_member_ibfk_1` FOREIGN KEY (`message_id`) REFERENCES `message` (`id`) ON DELETE CASCADE,
  CONSTRAINT `like_member_ibfk_2` FOREIGN KEY (`member_id`) REFERENCES `member` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `like_member`
--

LOCK TABLES `like_member` WRITE;
/*!40000 ALTER TABLE `like_member` DISABLE KEYS */;
INSERT INTO `like_member` VALUES (2,1),(6,1),(2,2),(3,2),(2,3),(2,4),(3,4),(2,5),(7,5),(2,6),(3,6),(2,7),(3,7),(5,7);
/*!40000 ALTER TABLE `like_member` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `member`
--

DROP TABLE IF EXISTS `member`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `member` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `follower_count` int unsigned NOT NULL DEFAULT '0',
  `time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `member`
--

LOCK TABLES `member` WRITE;
/*!40000 ALTER TABLE `member` DISABLE KEYS */;
INSERT INTO `member` VALUES (1,'test2','test','test',0,'2022-10-17 15:58:17'),(2,'??????','????????????','cat',1000000,'2022-10-17 15:59:21'),(3,'??????','???????????????','dog',500,'2022-10-17 16:00:07'),(4,'??????','???????????????','human',0,'2022-10-17 16:00:24'),(5,'??????','?????????????????? ??????~','tiger',8000,'2022-10-17 16:01:26'),(6,'??????','???????????????','HP+1',5000,'2022-10-17 16:01:47'),(7,'??????','???????????????','toy',3500,'2022-10-17 16:01:55'),(8,'test1','test1','test1',20,'2022-10-24 19:07:10'),(10,'test3','test3','test3',0,'2022-10-24 19:19:50'),(11,'test4','test4','test4',0,'2022-10-24 19:22:28');
/*!40000 ALTER TABLE `member` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `message`
--

DROP TABLE IF EXISTS `message`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `message` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `member_id` bigint NOT NULL,
  `content` varchar(255) NOT NULL,
  `like_count` int unsigned NOT NULL DEFAULT '0',
  `time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `member_id` (`member_id`),
  CONSTRAINT `message_ibfk_1` FOREIGN KEY (`member_id`) REFERENCES `member` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `message`
--

LOCK TABLES `message` WRITE;
/*!40000 ALTER TABLE `message` DISABLE KEYS */;
INSERT INTO `message` VALUES (1,1,'?????????????????????',1,'2022-10-17 16:56:11'),(2,2,'????????????????????????????????????!',5000000,'2022-10-17 17:22:44'),(3,3,'?????????????????????????????? ???!',2000,'2022-10-17 17:24:23'),(4,4,'???~??????????????????~~~',300000,'2022-10-17 17:25:20'),(5,5,'?????????????????????????????????????????????????????????',45000,'2022-10-17 17:27:08'),(6,6,'??????????????? : ????????????',25000,'2022-10-17 17:28:11'),(7,7,'???????????????????????????...',888,'2022-10-17 17:28:58'),(8,10,'hi',0,'2022-10-24 22:51:31'),(9,11,'???????????????4???',0,'2022-10-24 22:52:02'),(10,10,'???????????????3???',0,'2022-10-24 22:54:55'),(11,1,'?????????',0,'2022-10-24 23:00:07'),(12,10,'????????????',0,'2022-10-25 09:23:34'),(13,11,'?????????',0,'2022-10-25 09:44:03'),(15,1,'????????????!',0,'2022-10-25 10:44:01');
/*!40000 ALTER TABLE `message` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-10-25 11:06:17
