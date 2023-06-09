from random import choice, randrange
from datetime import datetime
# Operadores posibles
operators = ["+", "-", "*", "/"]
# Cantidad de cuentas a resolver
times = 5
# Contador inicial de tiempo.
# Esto toma la fecha y hora actual.
init_time = datetime.now()
print(f"¡Veremos cuanto tardas en responder estas {times} operaciones!")
resultados_correctos = 0
resultados_incorrectos = 0
for i in range(0, times):
    # Se eligen números y operador al azar
    number_1 = randrange(10)
    number_2 = randrange(10) 
    operator = choice(operators)
    #   Se hace un loop hasta que numero 2 sea distinto de 0, ya que no se puede dividir por 0
    while number_2 == 0:
        number_2 = randrange(10)  
    # Se imprime la cuenta.
    print(f"{i+1}- ¿Cuánto es {number_1} {operator} {number_2}?")
    # Le pedimos al usuario el resultado
    result = float(input("resultado: "))
    # Evaluamos que operador es,tambien se podria usar un case
    if operator == "*":
        resultado_maquina = number_1 * number_2
    elif operator == "/" :
        resultado_maquina = number_1 / number_2
    elif operator == "+" :
        resultado_maquina = number_1 + number_2
    else :
        resultado_maquina = number_1 - number_2
    # Evaluamos si el resultado ingresado por el usuario es correcto o no
    if result == resultado_maquina :
        print( " Resultado correcto :) ")
        resultados_correctos += 1
    else :
        print( " Resultado incorrecto :( ")
        resultados_incorrectos += 1
# Al terminar toda la cantidad de cuentas por resolver.
# # Se vuelve a tomar la fecha y la hora.
end_time = datetime.now()
# Restando las fechas obtenemos el tiempo transcurrido.
total_time = end_time - init_time
# Mostramos ese tiempo en segundos.
print(f"\n Tardaste {total_time.seconds} segundos.")
print(f"\n Tu cantidad de respuestas correctas fue : {resultados_correctos}")
print(f"\n Tu cantidad de respuestas incorrectas fue : {resultados_incorrectos}")

