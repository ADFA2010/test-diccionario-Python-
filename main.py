meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "ROLF":"Una respuesta a una broma",
            "SHEESH":"Ligera desaprobacion",
            "CREEPY":"Aterrador, siniestro",
            "AGGRO":"Ponerse agresivo o enojado",
            "XD":"Un tipo de risa, como: jajaja"
            }

word = input("escriba una palabra que no entienda").upper()
if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print('no conozco esa palabra')
