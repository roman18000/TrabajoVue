
-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 16-10-2021 a las 16:42:32
-- Versión del servidor: 10.3.31-MariaDB
-- Versión de PHP: 8.0.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `proyecto`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `categories`
--

 CREATE DATABASE /*!32312 IF NOT EXISTS*/ `proyecto` /*!40100 DEFAULT CHARACTER SET latin1 */;

 USE `proyecto`;

CREATE TABLE `categories` (
  `id` int(11) NOT NULL,
  `name` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `categories`
--

INSERT INTO `categories` (`id`, `name`) VALUES
(1, 'Bug'),
(2, 'Question');


-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `role`
--

CREATE TABLE `roles` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `configurations`
--

CREATE TABLE `configurations` (
  `id` int(10) UNSIGNED NOT NULL,
  `background` varchar(50) NOT NULL,
  `items_per_page` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `issues`
--

CREATE TABLE `issues` (
  `id` int(11) UNSIGNED NOT NULL,
  `email` varchar(30) DEFAULT NULL,
  `description` text DEFAULT NULL,
  `category_id` int(10) NOT NULL,
  `status_id` int(10) NOT NULL,
  `created_at` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;




-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `statuses`
--

CREATE TABLE `statuses` (
  `id` int(11) NOT NULL,
  `name` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `statuses`
--

INSERT INTO `statuses` (`id`, `name`) VALUES
(1, 'New'),
(2, 'Todo'),
(3, 'In progress');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `users`
--

CREATE TABLE `users` (
  `id` int(10) UNSIGNED NOT NULL,
  `email` varchar(30) NOT NULL,
  `username` varchar(30) NOT NULL,
  `password` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `configuration_id` int(10) UNSIGNED NOT NULL,
  `active` tinyint(1) UNSIGNED NOT NULL,
  `created_at` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--


-- --------------------------------------------------------
-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `points`
--
CREATE TABLE `points` (
  `id` int(10) UNSIGNED NOT NULL,
  `name` varchar(30) NOT NULL,
  `address` varchar(30) NOT NULL,
  `coordinates_latitude` varchar(50) NOT NULL,
  `coordinates_longitude` varchar(50) NOT NULL,
  `status` varchar(30) NOT NULL,
  `phone` varchar(30) NOT NULL,
  `email` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


-- --------------------------------------------------------
-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `points`
--
CREATE TABLE `route_of_evacuation` (
  `id` int(10) UNSIGNED NOT NULL,
  `name` varchar(50) NOT NULL,
  `description` varchar(50) NOT NULL,
  `publicado` tinyint(1) UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


--
-- Estructura de tabla para la tabla `view de usuarios`
--

CREATE TABLE `view` (
  `id` varchar(100) NOT NULL,
  `sorted_by_column` varchar(30) NOT NULL,
  `sort_type` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;



CREATE TABLE `report` (
  `id` int(10) UNSIGNED NOT NULL,
  `title` varchar(50) NOT NULL,
  `status` varchar(50) NOT NULL,
  `category` varchar(50) NOT NULL,
  `creation_date` varchar(50) NOT NULL,
  `closing_date` varchar(50),
  `description` varchar(255) NOT NULL,
  `coordinates_latitude` varchar(30) NOT NULL,
  `coordinates_longitude` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `phone` varchar(30) NOT NULL,
  `email` varchar(30) NOT NULL,
  `user_assing_id` int(10) UNSIGNED

) ENGINE=InnoDB DEFAULT CHARSET=latin1;



-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `permission`
--

CREATE TABLE `permissions` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------
-- --------------------------------------------------------
--
-- Estructura de tabla para la tabla `seguimiento`
--

CREATE TABLE `monitoring` (
  `id` int(11) NOT NULL,
  `description` varchar(255) NOT NULL,
  `creation_date` varchar(255) NOT NULL,
  `author_id` int(10) UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



--
-- Estructura de tabla para la tabla `role_has_permission`
--

CREATE TABLE `role_has_permission` (
  `role_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Estructura de tabla para la tabla `role_has_permission`
--

CREATE TABLE `report_has_monitoring` (
  `report_id` int(11) NOT NULL,
  `monitoring_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
--


-- Índices para tablas volcadas
--
-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `user_has_role`
--

CREATE TABLE `user_has_role` (
  `user_id` int(11) NOT NULL,
  `role_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `flood_zones`
--

CREATE TABLE `flood_zones` (
  `id` int(10) UNSIGNED NOT NULL,
  `cod_zone` varchar(50) NOT NULL,
  `name` varchar(30) NOT NULL,
  `state` tinyint(1) UNSIGNED NOT NULL,
  `colour` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `coordinates`
--

CREATE TABLE `coordinates` (
  `id` int(10) UNSIGNED NOT NULL,
  `latitude` float(50) NOT NULL,
  `longitude` float(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------


--
-- Estructura de tabla para la tabla `floodZone_has_coordinate`
--

CREATE TABLE `floodZone_has_coordinate` (
  `floodZone_id` int(10) NOT NULL,
  `coordinate_id` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `route_of_evacuation_has_coordinate`
--

CREATE TABLE `route_of_evacuation_has_coordinate` (
  `route_of_evacuation_id` int(10) NOT NULL,
  `coordinate_id` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Indices de la tabla `coordinates`
--
ALTER TABLE `coordinates`
  ADD PRIMARY KEY (`id`);


--
-- Indices de la tabla `flood_zones`
--
ALTER TABLE `flood_zones`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `categories`
--
ALTER TABLE `categories`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `configurations`
--
ALTER TABLE `configurations`
  ADD PRIMARY KEY (`id`);

--
--
-- Indices de la tabla `route_of_evacuation`
--
ALTER TABLE `route_of_evacuation`
  ADD PRIMARY KEY (`id`);

--

-- Indices de la tabla `issues`
--
ALTER TABLE `issues`
  ADD PRIMARY KEY (`id`),
  ADD KEY `category_id` (`category_id`),
  ADD KEY `status_id` (`status_id`);

--
-- Indices de la tabla `statuses`
--
ALTER TABLE `statuses`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`),
  ADD UNIQUE KEY `username` (`username`),
  ADD KEY `last_name` (`last_name`),
  ADD KEY `password` (`password`),
  ADD KEY `first_name` (`first_name`),
  ADD KEY `active` (`active`),
  ADD KEY `created_at` (`created_at`),
  ADD KEY `configuration_id` (`configuration_id`);


  --
  -- Indices de la tabla `points`
  --
  ALTER TABLE `points`
    ADD PRIMARY KEY (`id`),
    ADD UNIQUE KEY `name` (`name`),
    ADD UNIQUE KEY `address` (`address`),
    ADD KEY `coordinates_latitude` (`coordinates_latitude`),
    ADD KEY `coordinates_longitude` (`coordinates_longitude`),
    ADD KEY `status` (`status`),
    ADD KEY `phone` (`phone`),
    ADD KEY `email` (`email`);


--
-- Indice de la tabla de report_id
--

  ALTER TABLE `report`
    ADD PRIMARY KEY (`id`),
    ADD UNIQUE KEY `coordinates_latitude` (`coordinates_latitude`),
    ADD UNIQUE KEY `coordinates_longitude` (`coordinates_longitude`),
    ADD KEY `user_assing_id` (`user_assing_id`);
--
-- Indices de la tabla `role`
--
ALTER TABLE `roles`
  ADD PRIMARY KEY (`id`);


  -- Indices de la tabla `seguimiento`
  --
  ALTER TABLE `monitoring`
    ADD PRIMARY KEY (`id`);
--
-- Indices de la tabla `permission`
--
ALTER TABLE `permissions`
  ADD PRIMARY KEY (`id`);



--
-- Indices de la tabla `view_issues`
--
ALTER TABLE `view`
  ADD PRIMARY KEY (`id`);




  --
  -- AUTO_INCREMENT de la tabla `report`
  --
  ALTER TABLE `report`
    MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

  --
  -- AUTO_INCREMENT de la tabla `route_of_evacuation`
  --
  ALTER TABLE `route_of_evacuation`
    MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;




--
-- AUTO_INCREMENT de la tabla `coordinates`
--
ALTER TABLE `coordinates`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `flood_zones`
--
ALTER TABLE `flood_zones`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT;


--
-- AUTO_INCREMENT de la tabla `categories`
--
ALTER TABLE `categories`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `configurations`
--
ALTER TABLE `configurations`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `issues`
--
ALTER TABLE `issues`
  MODIFY `id` int(11) UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `statuses`
--
ALTER TABLE `statuses`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;


--
-- AUTO_INCREMENT de la tabla `users`
--
ALTER TABLE `users`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `points`
--
ALTER TABLE `points`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT;

  --
  -- AUTO_INCREMENT de la tabla `roles`
  --
  ALTER TABLE `roles`
    MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT;



--
-- AUTO_INCREMENT de la tabla `monitoring`
--
ALTER TABLE `monitoring`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT;


--
-- AUTO_INCREMENT de la tabla `permission`
--
ALTER TABLE `permissions`
  MODIFY `id` int(11) UNSIGNED NOT NULL AUTO_INCREMENT;



-- ALTER TABLE `issues`
--   ADD CONSTRAINT `issues_ibfk_1` FOREIGN KEY (`category_id`) REFERENCES `catego>
--   ADD CONSTRAINT `issues_ibfk_2` FOREIGN KEY (`status_id`) REFERENCES `statuses>
-- COMMIT;




/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
