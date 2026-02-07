import pandas as pd
import matplotlib.pyplot as plt

# 1. Cargar y limpiar
df = pd.read_csv('historial_conversiones.csv')
df['fecha'] = pd.to_datetime(df['fecha'])

# 2. Análisis: ¿Qué moneda sumó más monto?
resultado = df.groupby('moneda_origen')['monto_origen'].sum().sort_values(ascending=False)

# 3. Mostrar resultados en consola
print("Suma de montos por moneda:")
print(resultado)

# 4. Crear el gráfico
resultado.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Total Convertido por Moneda de Origen')
plt.xlabel('Moneda')
plt.ylabel('Suma de Montos')
plt.xticks(rotation=0) # Para que las letras no salgan inclinadas
plt.tight_layout()     # Ajusta el gráfico
