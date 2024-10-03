# Variables
nombre = "Luis Vejarano"
dias = int(input("Ingrese los dias: "))
salario = int(input("Ingrese el salario: "))
interesesCesantias = float(12/100)

# Calculos
prima = salario * dias / 360
cesantias = salario * dias / 360
intereses = cesantias * interesesCesantias / dias
vacaciones = salario * dias / 720
liquidacion = prima + cesantias + intereses + vacaciones

# Impresion
print(f"Señor Luis Vejarano para los {dias} dias laborados y salario {salario}, su liquidacion se compone asi:")
print(f"Prima: {prima}")
print(f"Cesantia: {cesantias}")
print(f"Intereses cesantias: {intereses}")
print(f"Vacaciones: {vacaciones}")
print(f"Liquidacion: {liquidacion}")