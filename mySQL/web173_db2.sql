-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Erstellungszeit: 14. Jun 2021 um 18:19
-- Server-Version: 8.0.22
-- PHP-Version: 7.3.28-1+0~20210503.84+debian10~1.gbp6819da

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Datenbank: `web173_db2`
--

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `gruppen`
--

CREATE TABLE `gruppen` (
  `id` int NOT NULL,
  `name` varchar(45) NOT NULL,
  `max_teilnehmer` int DEFAULT NULL,
  `teilnehmerzahl` int NOT NULL,
  `teilnehmerListe` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `lerntypen`
--

CREATE TABLE `lerntypen` (
  `id` int NOT NULL,
  `lerntyp` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `lernvorlieben`
--

CREATE TABLE `lernvorlieben` (
  `id` int NOT NULL,
  `internet verbindung` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `pole der persönlichkeit` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `frequenz` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `nachrichten`
--

CREATE TABLE `nachrichten` (
  `id` int NOT NULL,
  `inhalt` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `timestamp` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `profil_id` int NOT NULL,
  `gruppe_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `profile`
--

CREATE TABLE `profile` (
  `id` int NOT NULL,
  `name` varchar(45) NOT NULL,
  `faecher` varchar(255) NOT NULL,
  `lebensalter` int NOT NULL,
  `studiengang` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `wohnort` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `semester` int NOT NULL,
  `Vorwissen` varchar(45) NOT NULL,
  `about_me` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `sprachen` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `student_id` int NOT NULL,
  `lernvorlieben_id` int NOT NULL,
  `lerntyp_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `studenten`
--

CREATE TABLE `studenten` (
  `id` int NOT NULL,
  `name` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `google_user_id` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `email` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Daten für Tabelle `studenten`
--

INSERT INTO `studenten` (`id`, `name`, `google_user_id`, `email`) VALUES
(1, 'Dummy', 'token', 'token@gmail.com'),
(2, 'Daniel', 'token', 'danielweinert34@gmail.com');

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `teilnahmen`
--

CREATE TABLE `teilnahmen` (
  `gruppe_id` int NOT NULL,
  `profil_id` int NOT NULL,
  `id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Indizes der exportierten Tabellen
--

--
-- Indizes für die Tabelle `gruppen`
--
ALTER TABLE `gruppen`
  ADD PRIMARY KEY (`id`);

--
-- Indizes für die Tabelle `lerntypen`
--
ALTER TABLE `lerntypen`
  ADD PRIMARY KEY (`id`);

--
-- Indizes für die Tabelle `lernvorlieben`
--
ALTER TABLE `lernvorlieben`
  ADD PRIMARY KEY (`id`);

--
-- Indizes für die Tabelle `nachrichten`
--
ALTER TABLE `nachrichten`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_Nachricht/Konversation_Profil1_idx` (`profil_id`),
  ADD KEY `fk_Nachricht/Konversation_Gruppe1_idx` (`gruppe_id`);

--
-- Indizes für die Tabelle `profile`
--
ALTER TABLE `profile`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_Profil_Student_idx` (`student_id`),
  ADD KEY `fk_Profil_Lernvorlieben1_idx` (`lernvorlieben_id`),
  ADD KEY `fk_Profil_Lerntyp1_idx` (`lerntyp_id`);

--
-- Indizes für die Tabelle `studenten`
--
ALTER TABLE `studenten`
  ADD PRIMARY KEY (`id`);

--
-- Indizes für die Tabelle `teilnahmen`
--
ALTER TABLE `teilnahmen`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_Teilnahme_Profil1_idx` (`profil_id`),
  ADD KEY `fk_Teilnahme_Gruppe1` (`gruppe_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
