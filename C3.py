nums = ['uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis', 'siete', 'ocho', 'nueve', 'diez']
colores = ['rojo', 'verde', 'azul', 'amarillo', 'naranja', 'morado', 'rosa', 'blanco', 'negro', 'gris']
#imprimir print
#print(nums)

#agrega mas de un elemento a la lista
#colores.extend(['gris', 'celeste'])

#cambia de posicion primero la posicion despues el objeto a cambiar
#colores.insert(0, 'naranja')

#elimina todo
#colores.clear()

#agrega a la lista al ultimo
#colores.append('violeta')

#elimina el objeto o posicion y te lo enseña
#print(colores.pop(0))

#los datso los ordena de Z-A SI ES TRUE si es False de A-Z
#colores.sort(reverse=True)

#copia superficial
#colores_1=colores.copy()
#print(colores_1)
#print(colores)

"""for num in nums:
    #insertar variable 
    #index marca la posicion de la lista deseada de 0 al infinito 
    output = f"[{num},{colores[nums.index(num)]}]"
    print(output)
"""
#toma posicion de la lista indicada en los corchetes 
#print([nums[0],colores[0]])    
LISTA_NUEVA=[]
nums.reverse()
for num in nums:
   
    output = f"[{num},{colores[nums.index(num)]}]"
    LISTA_NUEVA.append(output)
print(LISTA_NUEVA)
