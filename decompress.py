import pyzipper as pz 

dictionary = open('listado-general.txt', 'r')
outcome = open('pass.txt', 'w')
compressed = pz.AESZipFile('respaldo.zip', 'r' , compression=pz.ZIP_LZMA, encryption=pz.WZ_AES)

for line in dictionary:
    try:
        password = line.strip('\n')
        pl = line
        password = password.encode("utf-8")
        data = compressed.extract('respaldo.txt', pwd=password)
        outcome.write(pl)
        outcome.close()
        break
    except: 
        pass





