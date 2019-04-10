musica="O sapo não lava o pé\nNão lava porque não quer\nEle mora na la lagoa\nNão lava o pé porque não quer\nMas que chulé"

vogais=["a","e","i","o","u"]
vogais_maiusculas=["A","E","I","O","U"]
vogais_especiais=["ã","é","í","ó","ú"]

print("\n"+musica)
for letra in musica:
    if letra in vogais_especiais:
        musica = musica.replace(letra, vogais[vogais_especiais.index(letra)])
for vogal in vogais:
    for letra in musica:
        if letra in vogais:
            musica=musica.replace(letra, vogal)
        if letra in vogais_maiusculas:
            musica=musica.replace(letra, vogal.upper())
    print("\n"+musica)