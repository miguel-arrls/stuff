from pytube import Youtube

link = input("Insira o link do youtube : ")
yt = Youtube(link)
videos = yt.streams.all()  # mostra os formatos disponiveis

video = list(enumerate(videos))  # lista os formatos, começando do zero

for i in video:  # vai printar os formatos na lista
    print(i)

print("Escolha o formato que deseja baixar")
dn_option = int(input("Insira a opção: "))  # opção para escolher o formato
dn_video = videos[dn_option]
dn_video.download()  # baixa o video

print("download concluído !!")
