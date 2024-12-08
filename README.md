# Data Warehouse para Ventas Totales Detalladas

Este proyecto consiste en la construcción de un Data Warehouse basado en los datos de ventas.

El propósito es organizar, limpiar, y transformar los datos para facilitar su análisis mediante consultas SQL.

### Estructura del Proyecto

1. Archivos Principales
   • Ventas-Totales-Detalladas.xlsx: Archivo de entrada que contiene los datos en bruto.
   • procesar_datos.py: Script Python para limpiar y transformar los datos en tablas.
   • Archivos CSV Generados:
   • DimCliente.csv: Dimensión de clientes.
   • DimProducto.csv: Dimensión de productos.
   • DimTiempo.csv: Dimensión temporal (fechas, años, meses, días).
   • FactVentas.csv: Tabla de hechos con las transacciones de ventas.

2. Tablas del Data Warehouse

## El Data Warehouse está diseñado con las siguientes tablas:

### Tablas de Dimensiones

• DimCliente: Contiene datos de los clientes.
• Columnas: CODCLI, Cliente, Pais, Departamento, Zona.
• DimProducto: Contiene información de los productos vendidos.
• Columnas: CODART, Artículo, Serie.
• DimTiempo: Define las fechas de las transacciones.
• Columnas: Fecha, Año, Mes, Día.

### Tabla de Hechos

• FactVentas: Contiene las transacciones de ventas realizadas.
• Columnas: Nfactura, CODCLI, CODART, Fecha, Unidades, Precio, Costo.

### Instalación y Configuración

1. Requisitos Previos
   • Python 3.8 o superior.
   • MySQL para almacenar el Data Warehouse.
   • Bibliotecas de Python:
   • pandas
   • openpyxl

2. Instalar Dependencias

### Ejecuta el siguiente comando para instalar las dependencias necesarias:

```bash
pip install pandas openpyxl
```

Uso

1. Preparar los Datos

Coloca el archivo ventas-votales-detalladas.xlsx en la misma carpeta que el script

procesar_datos.py.

2. Ejecutar el Script

Ejecuta el siguiente comando para procesar los datos y generar los archivos CSV:

```bash
python procesar_datos.py
```

3. Archivos Generados

Los archivos CSV se crearán en la misma carpeta que el script:
• DimCliente.csv
• DimProducto.csv
• DimTiempo.csv
• FactVentas.csv

Configuración de MySQL

1. Crear la Base de Datos

Ejecuta este comando en tu herramienta de MySQL:

```bash
CREATE DATABASE DataWarehouseVentas;
```

2. Crear Tablas

Ejecuta los scripts de creación de tablas en MySQL:

```bash
-- Tabla DimCliente
CREATE TABLE DimCliente (
CODCLI INT PRIMARY KEY,
Cliente VARCHAR(100),
Pais VARCHAR(50),
Departamento VARCHAR(50),
Zona VARCHAR(50)
);
```

```bash
-- Tabla DimProducto
CREATE TABLE DimProducto (
CODART INT PRIMARY KEY,
Articulo VARCHAR(100),
Serie VARCHAR(50)
);
```

```bash
-- Tabla DimTiempo
CREATE TABLE DimTiempo (
Fecha DATE PRIMARY KEY,
Año INT,
Mes INT,
Día INT
);
```

```bash
-- Tabla FactVentas
CREATE TABLE FactVentas (
Nfactura INT PRIMARY KEY,
CODCLI INT REFERENCES DimCliente(CODCLI),
CODART INT REFERENCES DimProducto(CODART),
Fecha DATE REFERENCES DimTiempo(Fecha),
Unidades INT,
Precio DECIMAL(10, 2),
Costo DECIMAL(10, 2)
);
```

3. Cargar los Datos en MySQL

Carga los archivos CSV generados en las tablas con los siguientes comandos:

COPY DimCliente(CODCLI, Cliente, Pais, Departamento, Zona)
FROM '/ruta/a/DimCliente.csv'
DELIMITER ','
CSV HEADER;

COPY DimProducto(CODART, Articulo, Serie)
FROM '/ruta/a/DimProducto.csv'
DELIMITER ','
CSV HEADER;

COPY DimTiempo(Fecha, Año, Mes, Día)
FROM '/ruta/a/DimTiempo.csv'
DELIMITER ','
CSV HEADER;

COPY FactVentas(Nfactura, CODCLI, CODART, Fecha, Unidades, Precio, Costo)
FROM '/ruta/a/FactVentas.csv'
DELIMITER ','
CSV HEADER;

Resultados Esperados

Con el Data Warehouse configurado, puedes realizar consultas como:
1.Total de Ventas por Cliente:

SELECT Cliente, SUM(Unidades \* Precio) AS TotalVentas
FROM FactVentas
JOIN DimCliente ON FactVentas.CODCLI = DimCliente.CODCLI
GROUP BY Cliente;

2.Productos Más Vendidos:

SELECT Articulo, SUM(Unidades) AS TotalUnidades
FROM FactVentas
JOIN DimProducto ON FactVentas.CODART = DimProducto.CODART
GROUP BY Articulo
ORDER BY TotalUnidades DESC;

Contribuciones

Si deseas contribuir al proyecto o necesitas ayuda, abre un Issue o realiza un Pull Request en el repositorio.

Licencia

Este proyecto es de uso académico y está bajo una licencia de uso libre.

Autor

Creado por Darvcode
