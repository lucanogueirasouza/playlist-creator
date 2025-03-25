playlist = []
print ("----PlayList----")
while True: 
    selecao = int(input("1 - Adicionar\n2 - Ver PlayList\n3 - Tirar Alguma Musica\n4 - Sair\nDigite: "))
    if selecao == 1: 
        musica = str(input("Digite uma musica: ")).lower()
        if musica in playlist: 
            musicaigual = playlist.index(musica)
            playlist.pop(musicaigual)
            playlist.append(musica)
            print ("voce colocou uma musica igual e ja removemos ela.")
        else:
            playlist.append(musica)
            print ("musica adicionada")
    elif selecao == 3:
        musica_retirar = str(input("Digite o nome da musica para retirar: ")).lower()
        musica_retirar = playlist.index(musica_retirar)
        playlist.pop(musica_retirar)
        print ("Musica retirada com sucesso!")
    if selecao == 2:
        print (playlist)
    if selecao == 4: 
        print ("Saindo...")
        break;
print (f"PlayList feita: {playlist}")