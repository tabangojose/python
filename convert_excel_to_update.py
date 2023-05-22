import pandas as pd

def generate_update_statements(table_name):
    # Lee el archivo de Excel
    df = pd.read_excel('data.xlsx')

    # Genera la sentencia UPDATE
    with open(f"{table_name}.sql", "w") as f:
        for index, row in df.iterrows():
            set_values = "', '".join([f"{col} = {val}" if isinstance(val, (int, float)) else f"{col} = '{val}'" for col, val in zip(df.columns, row.values) if 'PK' not in col])
            where_values = " AND ".join([f"{col.replace('PK', '')} = '{row[col]}'" for col in df.columns if 'PK' in col])
            f.write(f"UPDATE {table_name} SET {set_values} WHERE {where_values};\n")

    # Descarga el archivo .sql
    from google.colab import files
    files.download(f"{table_name}.sql")

generate_update_statements("inv_compras")