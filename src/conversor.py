import requests
import os
from datetime import datetime
import csv

# --- CLASE ---
class ConversorDivisas:
    def __init__(self, moneda_base = "USD"):
        self.moneda_base = moneda_base
        self.principales = ["USD", "EUR", "MXN", "COP", "GBP"]
        self.tasas = {
            "USD": 1.0, 
            "COP": 3679.50, 
            "EUR": 0.86, 
            "MXN": 17.49, 
            "GBP": 0.74
        }
        self.archivo_historial = "historial_conversiones.csv"

    def inicializar_archivo(self):
        if not os.path.exists(self.archivo_historial):
            with open(self.archivo_historial, "w", newline="") as archivo:
                escritor = csv.writer(archivo)
                escritor.writerow(["fecha", "moneda_base", "monto_origen", "moneda_origen", "moneda_destino", "resultado"])

    def guardar_historial(self, lista_de_datos):
        try:
            with open(self.archivo_historial, "a", newline="") as archivo:
                escritor = csv.writer(archivo)
                escritor.writerow(lista_de_datos)
        except Exception as e:
            print(f"⚠️ Error al guardar: {e}")

    def mostrar_resumen(self):
        try:
            with open(self.archivo_historial, "r") as archivo:
                lineas = archivo.readlines()

                if len(lineas) <= 1:
                    return

                print("\n" + "═"*60)
                print("📊  RESUMEN DE ACTIVIDAD RECIENTE")
                print("═"*60)

                datos_a_mostrar = lineas[1:][-5:]

                for linea in datos_a_mostrar:
                    # El .strip() quita espacios en blanco, tabulaciones y saltos de linea
                    # El .split() es para dividir los datos por las comas
                    datos = linea.strip().split(',')

                    if len(datos) >= 6:
                        fecha = datos[0]
                        origen = datos[3]
                        destino = datos[4]

                        try:
                            monto = float(datos[2])
                            resultado = float(datos[5])
                            print(f" {fecha} | {monto:,.2f} {origen} ➡️  {resultado:,.2f} {destino}")
                        except ValueError:
                            print(f" {fecha} | {datos[2]} {origen} ➡️  {datos[5]} {destino}")
                print("="*60)
        except FileNotFoundError:
            pass

    def obtener_tasas_reales(self) -> str:
        url = f"https://open.er-api.com/v6/latest/{self.moneda_base}"
        try:
            respuesta = requests.get(url, timeout = 5)
            datos = respuesta.json()
            if datos["result"] == "success":
                self.tasas = datos["rates"]
                return datos["time_last_update_utc"]
            else:
                return "Fecha no disponible (Error en la API)."
        except requests.exceptions.Timeout:
            return "Tiempo de espera agotado (Falla en el servidor API)."
        except Exception:
            return "Fecha no disponible (Error conexión)."
    
    def convertir_moneda(self, cantidad: float, origen: str, destino: str) -> float:
        monto_base = cantidad / self.tasas[origen]
        return monto_base * self.tasas[destino]
    
    def obtener_moneda(self, mensaje: str) -> str:
        while True:
            moneda = input(f"{mensaje} ({', '.join(self.principales)}): ").upper()
            
            if moneda in self.tasas:
                return moneda
            
            print(f"❌ Error: La moneda '{moneda}' no es válida.")

    def obtener_monto(self) -> float:
        while True:
            try:
                return float(input("💰 Ingrese la cantidad a convertir: $"))
            except ValueError:
                print("❌ Error: El monto debe ser un valor numérico.")


# --- BLOQUE PRINCIPAL ---
print("\n$$$ CONVERSOR DE DIVISAS PROFESIONAL $$$")
print("-" * 40)

# Inicialización
mi_conversor = ConversorDivisas()
mi_conversor.inicializar_archivo()
ultima_actualizacion = mi_conversor.obtener_tasas_reales()

print(f"📅 Tasas del mercado actualizadas: {ultima_actualizacion}")
print("-" * 40)

while True:
    # 1. Obtener datos
    cantidad_monto = mi_conversor.obtener_monto()
    moneda_origen = mi_conversor.obtener_moneda("Ingrese la moneda origen")
    moneda_destino = mi_conversor.obtener_moneda("Ahora, ingrese la moneda destino")

    # 2. Convertir
    result = mi_conversor.convertir_moneda(cantidad_monto, moneda_origen, moneda_destino)

    # 3. Guardar
    fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    linea_historial = [fecha_actual,mi_conversor.moneda_base,cantidad_monto,moneda_origen,moneda_destino,result]
    mi_conversor.guardar_historial(linea_historial)

    # 4. Mostrar resultado
    print("\n" + "·"*40)
    print(f"✅ RESULTADO: {cantidad_monto:,.2f} {moneda_origen} = {result:,.2f} {moneda_destino}")
    print("·"*40 + "\n")

    # 5. Continuar o Salir 
    res = input("¿Desea realizar otra conversión? (S/N): ").upper()
    if res != "S": 
        mi_conversor.mostrar_resumen()
        print("\n👋 ¡Gracias por usar nuestro sistema! Hasta la próxima.") 
        break