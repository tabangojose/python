import os
import pandas as pd

# Lee el archivo de Excel
df = pd.read_excel('listado.xlsx')

# Nombre de la tabla
table_name = 'inv_ventas'

# Borra el archivo de salida si
if os.path.exists('sentences.sql'):
    os.remove('sentences.sql')

# Abre el archivo de salida
with open('sentences.sql', 'w') as f:
    # Genera la sentences INSERT para cada fila del archivo
    for index, row in df.iterrows():
        columns = "', '".join([col for col in df.columns])
        values = "', '".join([str(val) if isinstance(val, (int, float)) else f"'{val}'" for val in row.values])
        f.write(f"INSERT INTO {table_name} ('{columns}') VALUES ('{values}');\n")