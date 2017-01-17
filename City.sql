-- phpMyAdmin SQL Dump
-- version 4.5.1
-- http://www.phpmyadmin.net
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 17-01-2017 a las 20:24:24
-- Versión del servidor: 10.1.13-MariaDB
-- Versión de PHP: 5.6.21

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `external_cities_example`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `City`
--

CREATE TABLE `city` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `country` varchar(255) NOT NULL,
  `continent` varchar(255) NOT NULL,
  `population` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `City`
--

INSERT INTO `City` (`id`, `name`, `country`, `continent`, `population`) VALUES
(2, 'Tandil', 'Argentina', 'South America', 110627),
(3, 'New York', 'United States', 'North America', 8406000),
(4, 'San Francisco', 'United States', 'North America', 837),
(5, 'Seattle', 'United States', 'North America', 652405),
(6, 'El Calafate', 'Argentina', 'South America', 22000),
(7, 'Barcelona', 'Spain', 'Europe', 1602000),
(8, 'Nice', 'France', 'Europe', 343304),
(9, 'Berlin', 'Germany', 'Europe', 3502000),
(10, 'Istanbul', 'Turkey', 'Europe-Asia', 1403000),
(11, 'Chiang Mai', 'Thailand', 'Asia', 398169),
(12, 'Sydney', 'Australia', 'Oceanina', 4293000),
(13, 'Luxor', 'Egypt', 'Africa', 202232),
(14, 'Johhanesburg', 'South Africa', 'Africa', 752349);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `City`
--
ALTER TABLE `City`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `City`
--
ALTER TABLE `City`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
