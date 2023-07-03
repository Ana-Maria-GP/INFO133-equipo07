-- MariaDB dump 10.19  Distrib 10.6.12-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: COLOMBIA
-- ------------------------------------------------------
-- Server version	10.6.12-MariaDB-0ubuntu0.22.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `CATEGORIA`
--

DROP TABLE IF EXISTS `CATEGORIA`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `CATEGORIA` (
  `ID_CATEGORIA` int(11) NOT NULL,
  `NOMBRE_CATEGORIA` varchar(100) DEFAULT NULL,
  `NOMBRE_MEDIO` varchar(100) DEFAULT NULL,
  `URL_CATEGORIA` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`ID_CATEGORIA`),
  KEY `NOMBRE_MEDIO` (`NOMBRE_MEDIO`),
  CONSTRAINT `CATEGORIA_ibfk_1` FOREIGN KEY (`NOMBRE_MEDIO`) REFERENCES `MEDIO_PRENSA` (`NOMBRE_MEDIO`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `CATEGORIA`
--

LOCK TABLES `CATEGORIA` WRITE;
/*!40000 ALTER TABLE `CATEGORIA` DISABLE KEYS */;
/*!40000 ALTER TABLE `CATEGORIA` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `FUNDADORES`
--

DROP TABLE IF EXISTS `FUNDADORES`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `FUNDADORES` (
  `ID_FUNDADOR` int(11) NOT NULL,
  `NOMBRE_FUNDADOR` varchar(100) DEFAULT NULL,
  `APELLIDO_FUNDADOR` varchar(100) DEFAULT NULL,
  `NOMBRE_MEDIO` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`ID_FUNDADOR`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `FUNDADORES`
--

LOCK TABLES `FUNDADORES` WRITE;
/*!40000 ALTER TABLE `FUNDADORES` DISABLE KEYS */;
/*!40000 ALTER TABLE `FUNDADORES` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `FUNDADO_POR`
--

DROP TABLE IF EXISTS `FUNDADO_POR`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `FUNDADO_POR` (
  `NOMBRE_MEDIO` varchar(100) DEFAULT NULL,
  `ID_FUNDADOR` int(11) DEFAULT NULL,
  KEY `NOMBRE_MEDIO` (`NOMBRE_MEDIO`),
  KEY `ID_FUNDADOR` (`ID_FUNDADOR`),
  CONSTRAINT `FUNDADO_POR_ibfk_1` FOREIGN KEY (`NOMBRE_MEDIO`) REFERENCES `MEDIO_PRENSA` (`NOMBRE_MEDIO`),
  CONSTRAINT `FUNDADO_POR_ibfk_2` FOREIGN KEY (`ID_FUNDADOR`) REFERENCES `FUNDADORES` (`ID_FUNDADOR`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `FUNDADO_POR`
--

LOCK TABLES `FUNDADO_POR` WRITE;
/*!40000 ALTER TABLE `FUNDADO_POR` DISABLE KEYS */;
/*!40000 ALTER TABLE `FUNDADO_POR` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `MEDIO_PRENSA`
--

DROP TABLE IF EXISTS `MEDIO_PRENSA`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `MEDIO_PRENSA` (
  `NOMBRE_MEDIO` varchar(100) NOT NULL,
  `URL_MEDIO` varchar(100) DEFAULT NULL,
  `AÑO_FUNDACION` int(11) DEFAULT NULL,
  `COBERTURA` varchar(100) DEFAULT NULL,
  `CONTINENTE` varchar(100) DEFAULT NULL,
  `PAIS` varchar(100) DEFAULT NULL,
  `REGION` varchar(100) DEFAULT NULL,
  `CIUDAD` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`NOMBRE_MEDIO`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `MEDIO_PRENSA`
--

LOCK TABLES `MEDIO_PRENSA` WRITE;
/*!40000 ALTER TABLE `MEDIO_PRENSA` DISABLE KEYS */;
INSERT INTO `MEDIO_PRENSA` VALUES ('A La Luz Pública','https://www.alaluzpublica.com/',2012,'Nacional','América','Colombia','Tolima','Ibagué;'),('ADN','http://www.diarioadn.co/',2008,'Local','América','Colombia','Cundinamarca','Bogotá;'),('Cambio','https://www.cambiocolombia.com/',1993,'Nacional','América','Colombia','Cundinamarca','Bogotá;'),('Diario del Cauca','https://diariodelcauca.com.co/',1983,'Local','América','Colombia','Cauca','Popayán;'),('Diario del Huila','http://www.diariodelhuila.com/',1966,'Internacional','América','Colombia','Huila','Neiva;'),('Diario del Sur','http://www.diariodelsur.com.co/',1983,'Local','América','Colombia','Nariño','San Juan de Pasto;'),('El Bolivarense','https://bolivarense.com/',0,'Nacional','América','Colombia','Bolívar','Cartagena De Indias;'),('El Colombiano','https://www.elcolombiano.com/',1912,'Local','América','Colombia','Antioquia','Medellín;'),('El Deportivo','https://www.eldeportivo.com.co/',0,'Internacional','América','Colombia','Cundinamarca','Bogotá;'),('El Diario','https://www.eldiario.com.co/',1982,'Nacional','América','Colombia','Risaralda','Pereira;'),('El Espectador','https://www.elespectador.com/',1887,'Nacional','América','Colombia','Cundinamarca','Bogotá;'),('El Expreso','https://www.elexpreso.co/',0,'Nacional','América','Colombia','Risaralda','Pereira;'),('El Heraldo','https://www.elheraldo.co/',1933,'Nacional','América','Colombia','Atlántico','Barranquilla;'),('El Informador','https://www.elinformador.com.co/',1958,'Internacional','América','Colombia','Magdalena','Santa Marta;'),('El Meridiano','https://elmeridiano.co/',1995,'Internacional','América','Colombia','Córdoba','Montería;'),('El Nuevo Día','http://www.elnuevodia.com.co/',1992,'Nacional','América','Colombia','Tolima','Ibagué;'),('El Nuevo Siglo','https://www.elnuevosiglo.com.co/',1936,'Nacional','América','Colombia','Cundinamarca','Bogotá;'),('El Olfato','https://www.elolfato.com/',2016,'Nacional','América','Colombia','Tolima','Ibagué;'),('El País','https://www.elpais.com.co/',1950,'Local','América','Colombia','Valle del Cauca','Cali;'),('El País Vallenato','https://www.elpaisvallenato.com/',2005,'Nacional','América','Colombia','Cesar','Valledupar;'),('El Palpitar','http://www.elpalpitar.com/',2014,'Nacional','América','Colombia','Antioquia','Medellín;'),('El Periódico Deportivo','https://elperiodicodeportivo.com.co/',2009,'Internacional','América','Colombia','Cundinamarca','Bogotá;'),('El Pilón','https://elpilon.com.co/',1994,'Nacional','América','Colombia','Cesar','Valledupar;'),('El Quindiano','https://www.elquindiano.com/',0,'Local','América','Colombia','Quindío','Armenia;'),('El Universal','https://www.eluniversal.com.co/',1948,'Internacional','América','Colombia','Bolívar','Cartagena De Indias;'),('Extra','https://extra.com.co/',0,'Nacional','América','Colombia','Cundinamarca','Bogotá;'),('Hoy Diario del Magdalena','https://www.hoydiariodelmagdalena.com.co/',1993,'Internacional','América','Colombia','Magdalena','Santa Marta;'),('La Crónica del Quindío','https://www.cronicadelquindio.com/',1991,'Local','América','Colombia','Quindío','Armenia;'),('La Nación','https://www.lanacion.com.co/',1994,'Nacional','América','Colombia','Huila','Neiva;'),('La Opinion','https://www.laopinion.com.co/',1960,'Local','América','Colombia','Norte de Santander','San José de Cúcuta;'),('La Patria','https://www.lapatria.com/',1921,'Nacional','América','Colombia','Caldas','Manizales;'),('La Piragua','https://www.lapiragua.co/',0,'Internacional','América','Colombia','Córdoba','Montería;'),('La Razon','https://larazon.co/',2014,'Nacional','América','Colombia','Córdoba','Montería;'),('La República','http://www.larepublica.co/',1954,'Nacional','América','Colombia','Cundinamarca','Bogotá;'),('Las 2 orillas','https://www.las2orillas.co/',2013,'Nacional','América','Colombia','Cundinamarca','Bogotá;'),('Mi Diario','https://www.midiario.co/',0,'Nacional','América','Colombia','Cesar','Valledupar;'),('Minuto 30','https://www.minuto30.com/',2013,'Nacional','América','Colombia','Antioquia','Medellín;'),('Mundo Noticias','https://mundonoticias.com.co/',0,'Nacional','América','Colombia','Bolívar','Cartagena De Indias;'),('Nariño Hoy','https://nariñohoy.com',0,'Nacional','América','Colombia','Nariño','San Juan de Pasto;'),('Opanoticias','https://www.opanoticias.com/',0,'Internacional','América','Colombia','Huila','Neiva;'),('Periódico del Meta','https://www.periodicodelmeta.com/',2012,'Nacional','América','Colombia','Meta','Villavicencio;'),('Periodico Virtual','https://periodicovirtual.com/',2010,'Nacional','América','Colombia','Cauca','Popayan;'),('Periodismo Público','https://www.periodismopublico.com/',0,'Nacional','América','Colombia','Cundinamarca','Soacha;'),('Portafolio','http://www.portafolio.co/',1993,'Nacional','América','Colombia','Cundinamarca','Bogotá;'),('Proclama Cauca y Valle','https://www.proclamadelcauca.com/',1983,'Local','América','Colombia','Cauca','Santander de Quilichao;'),('Publimetro','https://www.publimetro.co/',1995,'Local','América','Colombia','Cundinamarca','Bogotá;'),('Pulzo','https://www.pulzo.com/',2013,'Nacional','América','Colombia','Cundinamarca','Bogotá;'),('Q\'Hubo Cali','https://www.qhubocali.com/',2008,'Local','América','Colombia','Valle del Cauca','Cali;'),('Q\'Hubo Medellín','https://qhubomedellin.com/',2008,'Local','América','Colombia','Antioquia','Medellín;'),('Santa Marta Al Día','https://santamartaaldia.co/',2018,'Nacional','América','Colombia','Magdalena','Santa Marta;'),('Seguimiento','https://www.seguimiento.co/',2016,'Nacional','América','Colombia','Magdalena','Santa Marta;'),('Semana','https://www.semana.com/',1982,'Nacional','América','Colombia','Cundinamarca','Bogotá;'),('Vanguardia Liberal','http://www.vanguardia.com/',1919,'Nacional','América','Colombia','Santander','Bucaramanga;'),('Zona Cero','http://www.zonacero.com/',2009,'Nacional','América','Colombia','Atlántico','Barranquilla;');
/*!40000 ALTER TABLE `MEDIO_PRENSA` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `NOTICIA`
--

DROP TABLE IF EXISTS `NOTICIA`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `NOTICIA` (
  `ID_NOTICIA` int(11) NOT NULL,
  `XPATH_TITULO` varchar(100) DEFAULT NULL,
  `XPATH_FECHA` varchar(100) DEFAULT NULL,
  `XPATH_CONTENIDO` varchar(100) DEFAULT NULL,
  `URL_NOTICIA` varchar(100) DEFAULT NULL,
  `NOMBRE_MEDIO` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`ID_NOTICIA`),
  KEY `NOMBRE_MEDIO` (`NOMBRE_MEDIO`),
  CONSTRAINT `NOTICIA_ibfk_1` FOREIGN KEY (`NOMBRE_MEDIO`) REFERENCES `MEDIO_PRENSA` (`NOMBRE_MEDIO`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `NOTICIA`
--

LOCK TABLES `NOTICIA` WRITE;
/*!40000 ALTER TABLE `NOTICIA` DISABLE KEYS */;
/*!40000 ALTER TABLE `NOTICIA` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `RRSS`
--

DROP TABLE IF EXISTS `RRSS`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `RRSS` (
  `ID_RRSS` int(11) NOT NULL,
  `USUARIO` varchar(100) DEFAULT NULL,
  `ACTUALIZACION` date DEFAULT NULL,
  `SEGUIDORES` int(11) DEFAULT NULL,
  `NOMBRE_RED` varchar(100) DEFAULT NULL,
  `NOMBRE_MEDIO` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`ID_RRSS`),
  KEY `NOMBRE_MEDIO` (`NOMBRE_MEDIO`),
  CONSTRAINT `RRSS_ibfk_1` FOREIGN KEY (`NOMBRE_MEDIO`) REFERENCES `MEDIO_PRENSA` (`NOMBRE_MEDIO`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `RRSS`
--

LOCK TABLES `RRSS` WRITE;
/*!40000 ALTER TABLE `RRSS` DISABLE KEYS */;
/*!40000 ALTER TABLE `RRSS` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-07-02 13:47:24
