import pyzipper as pz 

diccionario = open('listado-general.txt', 'r')
resultado = open('pass.txt', 'w')
comprimido = pz.AESZipFile('tarea.zip', 'r' , compression=pz.ZIP_LZMA, encryption=pz.WZ_AES)

for linea in diccionario:
    try:
        password = linea.strip('\n')
        pl = linea
        password = password.encode("utf-8")
        datos = comprimido.extract('secreto.txt', pwd=password)
        resultado.write(pl)
        resultado.close()
        break
    except: 
        pass




