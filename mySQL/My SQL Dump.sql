-- MySQL dump 10.13  Distrib 8.0.22, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: lerngruppen_app
-- ------------------------------------------------------
-- Server version	8.0.22

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `gruppe`
--

DROP TABLE IF EXISTS `gruppe`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `gruppe` (
  `id` int NOT NULL,
  `name` varchar(45) NOT NULL,
  `Max_Teilnehmer` int DEFAULT NULL,
  `Teilnehmerzahl` int NOT NULL,
  `TeilnehmerListe` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gruppe`
--

LOCK TABLES `gruppe` WRITE;
/*!40000 ALTER TABLE `gruppe` DISABLE KEYS */;
/*!40000 ALTER TABLE `gruppe` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lerntyp`
--

DROP TABLE IF EXISTS `lerntyp`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `lerntyp` (
  `id` int NOT NULL,
  `lerntyp` varchar(45) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lerntyp`
--

LOCK TABLES `lerntyp` WRITE;
/*!40000 ALTER TABLE `lerntyp` DISABLE KEYS */;
/*!40000 ALTER TABLE `lerntyp` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lernvorlieben`
--

DROP TABLE IF EXISTS `lernvorlieben`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `lernvorlieben` (
  `id` int NOT NULL,
  `name` varchar(45) NOT NULL,
  `Internet Verbindung` varchar(45) NOT NULL,
  `Pole der Persönlichkeit` varchar(45) NOT NULL,
  `Lernvorliebencol` varchar(45) NOT NULL,
  `Frequenz` varchar(45) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lernvorlieben`
--

LOCK TABLES `lernvorlieben` WRITE;
/*!40000 ALTER TABLE `lernvorlieben` DISABLE KEYS */;
/*!40000 ALTER TABLE `lernvorlieben` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `nachricht/konversation`
--

DROP TABLE IF EXISTS `nachricht/konversation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `nachricht/konversation` (
  `id` int NOT NULL,
  `Inhalt` varchar(255) NOT NULL,
  `timestamp` datetime NOT NULL,
  `Profil_id` int NOT NULL,
  `Gruppe_id` int NOT NULL,
  PRIMARY KEY (`id`,`Profil_id`),
  KEY `fk_Nachricht/Konversation_Profil1_idx` (`Profil_id`),
  KEY `fk_Nachricht/Konversation_Gruppe1_idx` (`Gruppe_id`),
  CONSTRAINT `fk_Nachricht/Konversation_Gruppe1` FOREIGN KEY (`Gruppe_id`) REFERENCES `gruppe` (`id`),
  CONSTRAINT `fk_Nachricht/Konversation_Profil1` FOREIGN KEY (`Profil_id`) REFERENCES `profil` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `nachricht/konversation`
--

LOCK TABLES `nachricht/konversation` WRITE;
/*!40000 ALTER TABLE `nachricht/konversation` DISABLE KEYS */;
/*!40000 ALTER TABLE `nachricht/konversation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `profil`
--

DROP TABLE IF EXISTS `profil`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `profil` (
  `id` int NOT NULL,
  `name` varchar(45) NOT NULL,
  `faecher` varchar(255) NOT NULL,
  `alter` int NOT NULL,
  `Studiengang` varchar(45) NOT NULL,
  `Wohnort` varchar(45) NOT NULL,
  `Semester` int NOT NULL,
  `Vorwissen` varchar(45) NOT NULL,
  `About_Me` varchar(255) NOT NULL,
  `Sprachen` varchar(45) NOT NULL,
  `Student_id` int NOT NULL,
  `Lernvorlieben_id` int NOT NULL,
  `Lerntyp_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_Profil_Student_idx` (`Student_id`),
  KEY `fk_Profil_Lernvorlieben1_idx` (`Lernvorlieben_id`),
  KEY `fk_Profil_Lerntyp1_idx` (`Lerntyp_id`),
  CONSTRAINT `fk_Profil_Lerntyp1` FOREIGN KEY (`Lerntyp_id`) REFERENCES `lerntyp` (`id`),
  CONSTRAINT `fk_Profil_Lernvorlieben1` FOREIGN KEY (`Lernvorlieben_id`) REFERENCES `lernvorlieben` (`id`),
  CONSTRAINT `fk_Profil_Student` FOREIGN KEY (`Student_id`) REFERENCES `student` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `profil`
--

LOCK TABLES `profil` WRITE;
/*!40000 ALTER TABLE `profil` DISABLE KEYS */;
/*!40000 ALTER TABLE `profil` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `student`
--

DROP TABLE IF EXISTS `student`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `student` (
  `id` int NOT NULL,
  `Name` varchar(45) NOT NULL,
  `Google User id` varchar(45) NOT NULL,
  `email` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student`
--

LOCK TABLES `student` WRITE;
/*!40000 ALTER TABLE `student` DISABLE KEYS */;
/*!40000 ALTER TABLE `student` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `teilnahme`
--

DROP TABLE IF EXISTS `teilnahme`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `teilnahme` (
  `Gruppe_id` int NOT NULL,
  `Profil_id` int NOT NULL,
  `id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_Teilnahme_Profil1_idx` (`Profil_id`),
  KEY `fk_Teilnahme_Gruppe1` (`Gruppe_id`),
  CONSTRAINT `fk_Teilnahme_Gruppe1` FOREIGN KEY (`Gruppe_id`) REFERENCES `gruppe` (`id`),
  CONSTRAINT `fk_Teilnahme_Profil1` FOREIGN KEY (`Profil_id`) REFERENCES `profil` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `teilnahme`
--

LOCK TABLES `teilnahme` WRITE;
/*!40000 ALTER TABLE `teilnahme` DISABLE KEYS */;
/*!40000 ALTER TABLE `teilnahme` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-05-29 14:00:39
