import requests
import pickle

data_old=[]
data_new=[]



archivoExterno=open("data","ab+")
archivoExterno.seek(0)


try:
    data_old = pickle.load(archivoExterno)
    print("Se han cargado {} listados anteriores de la base de datos".format(len(data_old)))
except:
    print("Base de datos vacia o inexistente")
finally:
    archivoExterno.close()

#cargando los anuncios de la web
response = requests.get("https://www.kucoin.com/_api/cms/articles?page=1&pageSize=20&category=listing&lang=en_US")

response = response.json()
response = response['items']


for i in range(len(response)):
    title = response[i]['title']
    date = response[i]['summary']
    data_new.append(title+' '+date)
    #print(f"{title} : {date}")


for new_coin in data_new:
    if new_coin not in data_old:
        data_old.append(new_coin)
        print("NUevo anuncio detectado: ",new_coin)


archivoExterno=open("data","wb")
pickle.dump(data_old,archivoExterno)
