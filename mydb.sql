-- phpMyAdmin SQL Dump
-- version 4.6.6deb5
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Jul 15, 2018 at 05:38 PM
-- Server version: 5.7.22-0ubuntu18.04.1
-- PHP Version: 7.2.7-0ubuntu0.18.04.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `mydb`
--

-- --------------------------------------------------------

--
-- Table structure for table `commands`
--

CREATE TABLE `commands` (
  `Id` int(11) NOT NULL,
  `Set_S5_BoilerStatus` int(1) NOT NULL,
  `Set_S6_PumpStatus` int(1) NOT NULL,
  `Set_K5_BoilerStatus` int(1) NOT NULL,
  `Set_K6_PumpStatus` int(1) NOT NULL,
  `Datetime` varchar(19) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `commands`
--

INSERT INTO `commands` (`Id`, `Set_S5_BoilerStatus`, `Set_S6_PumpStatus`, `Set_K5_BoilerStatus`, `Set_K6_PumpStatus`, `Datetime`) VALUES
(1, 0, 1, 1, 0, '2018-06-18 20:20:27'),
(2, 0, 2, 0, 0, '2018-07-15 17:21:41');

-- --------------------------------------------------------

--
-- Table structure for table `settings`
--

CREATE TABLE `settings` (
  `Id` int(11) NOT NULL,
  `temp1` int(2) NOT NULL,
  `StartTime` int(5) NOT NULL,
  `EndTime` int(5) NOT NULL,
  `temp2` int(2) NOT NULL,
  `Time3` int(5) NOT NULL,
  `Time4` int(5) NOT NULL,
  `temp3` int(2) NOT NULL,
  `temp4` int(2) NOT NULL,
  `temp5` int(2) NOT NULL,
  `Time5` int(5) NOT NULL,
  `temp6` int(2) NOT NULL,
  `temp7` int(2) NOT NULL,
  `Time6` int(5) NOT NULL,
  `Time7` int(5) NOT NULL,
  `temp8` int(2) NOT NULL,
  `Time8` int(5) NOT NULL,
  `Time9` int(5) NOT NULL,
  `temp9` int(2) NOT NULL,
  `Time10` int(5) NOT NULL,
  `Datetime` varchar(19) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `settings`
--

INSERT INTO `settings` (`Id`, `temp1`, `StartTime`, `EndTime`, `temp2`, `Time3`, `Time4`, `temp3`, `temp4`, `temp5`, `Time5`, `temp6`, `temp7`, `Time6`, `Time7`, `temp8`, `Time8`, `Time9`, `temp9`, `Time10`, `Datetime`) VALUES
(1, 40, 700, 2200, 57, 700, 1600, 40, 5, 57, 1600, 45, 2, 700, 2200, 40, 700, 2200, 40, 700, '2018-06-18 20:20:27'),
(2, 40, 700, 2300, 57, 700, 1600, 40, 5, 57, 1600, 45, 2, 700, 2300, 40, 700, 2300, 42, 700, '2018-07-15 17:19:11'),
(3, 40, 700, 2300, 57, 700, 1800, 40, 5, 57, 1800, 45, 2, 700, 2300, 40, 700, 2300, 42, 700, '2018-07-15 17:19:50'),
(4, 40, 700, 2300, 57, 700, 1800, 40, 5, 57, 1800, 45, 2, 700, 2300, 40, 700, 2300, 42, 700, '2018-07-15 17:21:24');

-- --------------------------------------------------------

--
-- Table structure for table `set_valves`
--

CREATE TABLE `set_valves` (
  `Id` int(11) NOT NULL,
  `Set_Valve1` int(1) NOT NULL,
  `Set_Valve2` int(1) NOT NULL,
  `Set_Valve3` int(1) NOT NULL,
  `Set_Valve4` int(1) NOT NULL,
  `Datetime` varchar(19) NOT NULL,
  `starttime_v1` int(5) NOT NULL,
  `histeresis` int(3) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `set_valves`
--

INSERT INTO `set_valves` (`Id`, `Set_Valve1`, `Set_Valve2`, `Set_Valve3`, `Set_Valve4`, `Datetime`, `starttime_v1`, `histeresis`) VALUES
(1, 2, 2, 2, 2, '2018-06-18 20:20:27', 600, 0),
(2, 2, 2, 2, 2, '2018-07-15 17:21:49', 600, 0);

-- --------------------------------------------------------

--
-- Table structure for table `temp`
--

CREATE TABLE `temp` (
  `id` int(11) NOT NULL,
  `Datetime` varchar(19) NOT NULL,
  `S1_BoilerInput` varchar(5) NOT NULL,
  `S2_BoilerOutput` varchar(5) NOT NULL,
  `S3_BoilerTop` varchar(5) NOT NULL,
  `S4_BoilerBottom` varchar(5) NOT NULL,
  `S5_BoilerStatus` int(1) NOT NULL,
  `S6_PumpStatus` int(1) NOT NULL,
  `S0_PumpStatus` int(5) NOT NULL,
  `SolarRadiation` int(4) DEFAULT NULL,
  `OutdoorTemp` int(5) DEFAULT NULL,
  `K1_KotelOutput` varchar(5) NOT NULL,
  `K2_BoilerInput` varchar(5) NOT NULL,
  `K3_BoilerTop` varchar(5) NOT NULL,
  `K4_BoilerBottom` varchar(5) NOT NULL,
  `K5_BoilerStatus` int(1) NOT NULL,
  `K6_PumpStatus` int(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `temp`
--

INSERT INTO `temp` (`id`, `Datetime`, `S1_BoilerInput`, `S2_BoilerOutput`, `S3_BoilerTop`, `S4_BoilerBottom`, `S5_BoilerStatus`, `S6_PumpStatus`, `S0_PumpStatus`, `SolarRadiation`, `OutdoorTemp`, `K1_KotelOutput`, `K2_BoilerInput`, `K3_BoilerTop`, `K4_BoilerBottom`, `K5_BoilerStatus`, `K6_PumpStatus`) VALUES
(1, '2018-06-18 20:20:27', '0', '0', '0', '0', 0, 0, 0, 0, 0, '0', '0', '0', '0', 0, 0),
(2, '2018-07-15 17:16:37', '67.3', '55.7', '62.2', '48.2', 0, 1, 5, NULL, NULL, '23.6', '44.8', '51.9', '52.0', 0, 0),
(3, '2018-07-15 17:19:40', '67.0', '55.4', '62.3', '47.6', 0, 1, 5, NULL, NULL, '23.7', '45.0', '52.2', '52.2', 0, 0),
(4, '2018-07-15 17:22:43', '66.8', '54.4', '62.4', '44.1', 0, 1, 5, NULL, NULL, '23.6', '45.1', '52.5', '53.3', 0, 0),
(5, '2018-07-15 17:25:45', '65.1', '51.6', '62.4', '34.6', 0, 1, 0, NULL, NULL, '23.6', '45.4', '53.1', '54.2', 0, 0);

-- --------------------------------------------------------

--
-- Table structure for table `valves`
--

CREATE TABLE `valves` (
  `id` int(10) NOT NULL,
  `Datetime` varchar(19) NOT NULL,
  `Valve1_Status` varchar(3) NOT NULL,
  `Valve2_Status` varchar(3) NOT NULL,
  `Valve3_Status` varchar(3) NOT NULL,
  `Valve4_Status` varchar(3) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `valves`
--

INSERT INTO `valves` (`id`, `Datetime`, `Valve1_Status`, `Valve2_Status`, `Valve3_Status`, `Valve4_Status`) VALUES
(1, '2018-06-18 20:20:27', '0', '0', '0', '0');

-- --------------------------------------------------------

--
-- Table structure for table `water`
--

CREATE TABLE `water` (
  `id` int(11) NOT NULL,
  `Datetime` varchar(19) NOT NULL,
  `water_data` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `water`
--

INSERT INTO `water` (`id`, `Datetime`, `water_data`) VALUES
(1, '2018-07-15 15:55:57', 45.41),
(2, '2018-07-15 17:01:03', 45.42);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `commands`
--
ALTER TABLE `commands`
  ADD PRIMARY KEY (`Id`);

--
-- Indexes for table `settings`
--
ALTER TABLE `settings`
  ADD PRIMARY KEY (`Id`);

--
-- Indexes for table `set_valves`
--
ALTER TABLE `set_valves`
  ADD PRIMARY KEY (`Id`);

--
-- Indexes for table `temp`
--
ALTER TABLE `temp`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `valves`
--
ALTER TABLE `valves`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `water`
--
ALTER TABLE `water`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `commands`
--
ALTER TABLE `commands`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
--
-- AUTO_INCREMENT for table `settings`
--
ALTER TABLE `settings`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
--
-- AUTO_INCREMENT for table `set_valves`
--
ALTER TABLE `set_valves`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
--
-- AUTO_INCREMENT for table `temp`
--
ALTER TABLE `temp`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
--
-- AUTO_INCREMENT for table `valves`
--
ALTER TABLE `valves`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
--
-- AUTO_INCREMENT for table `water`
--
ALTER TABLE `water`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
