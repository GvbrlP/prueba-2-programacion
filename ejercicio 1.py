
VALOR_MEDICAMENTOS_BASE = 60000
VALOR_DESPACHO_BASE = 8000

print("--- EJERCICIO 1: CÁLCULO DE MEDICAMENTOS Y DESPACHO ---")

edad = int(input("Ingrese su edad: "))
tramo = input("Ingrese su tramo (A, B, C o D): ").strip().upper()

descuento_med = 0.0

if edad <= 30:
    if tramo == "A" or tramo == "B":
        descuento_med = 0.18
    elif tramo == "C" or tramo == "D":
        descuento_med = 0.12 
elif 31 <= edad <= 60:
    if tramo == "A" or tramo == "B":
        descuento_med = 0.12
    elif tramo == "C" or tramo == "D":
        descuento_med = 0.08  
else:
    descuento_med = 0.0

descuento_despacho = 0.0

if tramo == "A" or tramo == "B":
    descuento_despacho += 0.10
    if edad >= 55:
        descuento_despacho += 0.05

valor_medicamentos_final = int(VALOR_MEDICAMENTOS_BASE * (1 - descuento_med))
valor_despacho_final = int(VALOR_DESPACHO_BASE * (1 - descuento_despacho))

print(f"El valor de medicamentos es: {valor_medicamentos_final}")
print(f"El valor del despacho es: {valor_despacho_final}")
