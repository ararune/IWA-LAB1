-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 08, 2023 at 12:15 PM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `vjezba6`
--

-- --------------------------------------------------------

--
-- Table structure for table `sessions`
--

CREATE TABLE `sessions` (
  `session_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `subjects`
--

CREATE TABLE `subjects` (
  `id` int(11) NOT NULL,
  `kod` varchar(100) NOT NULL,
  `ime` varchar(100) NOT NULL,
  `bodovi` int(11) NOT NULL,
  `godina` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `subjects`
--

INSERT INTO `subjects` (`id`, `kod`, `ime`, `bodovi`, `godina`) VALUES
(1, 'ip', 'Introduction to programming', 6, 1),
(2, 'c1', 'Calculus 1', 7, 1),
(3, 'cu', 'Computer usage', 5, 1),
(4, 'dmt', 'Digital and microprocessor technology', 6, 1),
(5, 'db', 'Databases', 6, 2),
(6, 'c2', 'Calculus 2', 7, 2),
(7, 'dsa', 'Data structures and algorithms', 5, 2),
(8, 'ca', 'Computer architecture', 6, 2),
(9, 'isd', 'Information systems design', 5, 3),
(10, 'c3', 'Calculus 3', 7, 3),
(11, 'sa', 'Server Architecture', 6, 3),
(12, 'cds', 'Computer and data security', 6, 3);

-- --------------------------------------------------------

--
-- Table structure for table `upisni_list`
--

CREATE TABLE `upisni_list` (
  `id` int(11) NOT NULL,
  `id_studenta` int(11) NOT NULL,
  `id_predmeta` int(11) NOT NULL,
  `status` enum('pass','enr') NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `upisni_list`
--

INSERT INTO `upisni_list` (`id`, `id_studenta`, `id_predmeta`, `status`) VALUES
(37, 17, 2, 'pass'),
(38, 17, 3, 'pass'),
(39, 17, 1, 'enr'),
(40, 17, 4, 'pass'),
(41, 17, 5, 'pass'),
(42, 17, 8, 'pass'),
(43, 17, 7, 'pass'),
(44, 17, 6, 'pass'),
(45, 17, 11, 'pass'),
(46, 17, 10, 'pass'),
(47, 17, 12, 'pass'),
(48, 17, 9, 'pass');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `ime` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` binary(64) NOT NULL,
  `uloga` enum('student','admin') NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `ime`, `email`, `password`, `uloga`) VALUES
(17, 'ante', 'ante@gmail.com', 0x0657e698882cc2d254780e1d68bbbc26458817a5967fb1bb26b33ff80773a36cd9eb635d7e1ceb727b12deb58faebba1d4f89750cef38c495011775e0774ceb5, 'admin'),
(18, 'ana', 'ana@gmail.com', 0xc68a6fe93a8e202b3fafdbb8cc32837e6f8a366434b74752b377462632c9fbb925071364415d96e2543d0cb13c945cbf0ce3ef972bb153c8cfb83d352364c1f3, 'student'),
(19, 'dva', 'dva@gmail.com', 0x4777ce375d8b6401a4dd1898a68d370b3a4377501a72d9653fc730a40ba26f61fb5f3562e3012b1850dab16793dd8cde5b1db00d8c7993223efdbb7be9223bc0, 'student');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `sessions`
--
ALTER TABLE `sessions`
  ADD PRIMARY KEY (`session_id`);

--
-- Indexes for table `subjects`
--
ALTER TABLE `subjects`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `upisni_list`
--
ALTER TABLE `upisni_list`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_studenta` (`id_studenta`),
  ADD KEY `id_predmeta` (`id_predmeta`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `sessions`
--
ALTER TABLE `sessions`
  MODIFY `session_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT for table `subjects`
--
ALTER TABLE `subjects`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `upisni_list`
--
ALTER TABLE `upisni_list`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=49;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `upisni_list`
--
ALTER TABLE `upisni_list`
  ADD CONSTRAINT `upisni_list_ibfk_1` FOREIGN KEY (`id_studenta`) REFERENCES `users` (`id`),
  ADD CONSTRAINT `upisni_list_ibfk_2` FOREIGN KEY (`id_predmeta`) REFERENCES `subjects` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
