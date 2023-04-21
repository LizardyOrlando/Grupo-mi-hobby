f = open ('./pps2023/mihobby.md', 'r')
hobby = f.read()
respuestas= []
diccionario = {}
for i in range(2,7):
    respuestas.append(hobby.splitlines()[i])
for i in range(5):
    respuestas[i] =  respuestas[i].replace("*","") 
    diccionario[respuestas[i].split(":")[0]] = respuestas[i].split(":")[1]
print(diccionario)
for i in diccionario:
    print(i)
for z in diccionario:
    print(diccionario[z])