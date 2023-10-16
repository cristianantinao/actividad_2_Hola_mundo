# 1. TAREA: imprime "Hola, mundo"
Hola = 'Hola'
mundo = 'mundo'
print( 'Hola', 'mundo')
# 2. imprime "Hola, Noelle" con el nombre en una variable
name = "Noelle"
print( 'Hola', 'Noelle')	# con una coma
print( 'Hola' + 'Noelle' )	# con un +
# 3. imprimir "Hola 42!" con el número en una variable
name = 42
print( 'Hola', 42,'!' )	# con una coma
print( 'Hola' + str(42) +'!' )	# con una +	-- este debería arrojar un error!
# 4. imprimir "Amo comer sushi y pizza" con las comidas en variables
fave_food1 = "sushi"
fave_food2 = "pizza"
comer = "Amo comer {} y {}".format(fave_food1, fave_food2)
print(comer) # con .format()
print(f"Amo comer {fave_food1} y {fave_food2}") # con una cadena f

