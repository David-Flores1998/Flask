week = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo']   
out = []
for i,day in enumerate(week):
    if day == 'Sabado' or day == 'Domingo':
        out.append(i)
print(out)
