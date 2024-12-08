import pandas as pd

# Archivo Excel de Ventas Totales Detalladas
file_path = 'ventas-totales-detalladas.xlsx'
data = pd.read_excel(file_path, sheet_name='Facturas ventas')

# ---- 1. LIMPIEZA Y TRANSFORMACIÓN DE LOS DATOS ----

# Eliminar duplicados para evitar datos redundantes
data = data.drop_duplicates()

# Convertir la columna "Fecha" (que está en formato Excel) a un formato de fecha legible
data['Fecha'] = pd.to_datetime(data['Fecha'], origin='1899-12-30', unit='D')

# Crear nuevas columnas para la Dimensión de Tiempo
data['Año'] = data['Fecha'].dt.year
data['Mes'] = data['Fecha'].dt.month
data['Día'] = data['Fecha'].dt.day

# ---- 2. CREACIÓN DE LAS TABLAS DIMENSIONALES ----

# Crear la tabla DimCliente eliminando duplicados de las columnas relevantes
dim_cliente = data[['CODCLI', 'Cliente', 'Pais', 'Departamento', 'Zona']].drop_duplicates()

# Crear la tabla DimProducto eliminando duplicados de las columnas relevantes
dim_producto = data[['CODART', 'Artículo', 'Serie']].drop_duplicates()

# Crear la tabla DimTiempo eliminando duplicados de las columnas de fecha desglosadas
dim_tiempo = data[['Fecha', 'Año', 'Mes', 'Día']].drop_duplicates()

# ---- 3. CREACIÓN DE LA TABLA DE HECHOS ----

# Crear la tabla FactVentas con las columnas necesarias
fact_ventas = data[['Nfactura', 'CODCLI', 'CODART', 'Fecha', 'Unidades', 'Precio', 'Costo']]

# ---- 4. EXPORTAR LAS TABLAS A ARCHIVOS CSV ----

# Guardar cada tabla en un archivo CSV
dim_cliente.to_csv('DimCliente.csv', index=False)
dim_producto.to_csv('DimProducto.csv', index=False)
dim_tiempo.to_csv('DimTiempo.csv', index=False)
fact_ventas.to_csv('FactVentas.csv', index=False)

# ---- 5. RESUMEN PARA EL USUARIO ----

print("Los datos han sido procesados y exportados a los siguientes archivos:")
print("- DimCliente.csv: Información de clientes.")
print("- DimProducto.csv: Información de productos.")
print("- DimTiempo.csv: Información de tiempo (años, meses, días).")
print("- FactVentas.csv: Tabla de hechos con datos de ventas.")
