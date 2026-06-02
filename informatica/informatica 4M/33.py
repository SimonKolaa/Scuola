import os
class Utente:
    def __init__(self, nomeUtente, password, email):
        self.nome = nomeUtente
        self.email = email
        self.password = password
        self.videoVisti = []
        self.playlistCreate = []

    def guardaVideo(self, video):
        self.videoVisti.append(video)
    
    def creaPlaylist(self, playlist):
        self.playlist.append(playlist)

    def aggiungiVideoPlaylist(self, playlist, video):
        playlist.video.append(video)

    def rimuoviVideoPlaylist(self, playlist, video):
        playlist.video.remove(video)

    def cancellaPlaylist(self, playlist):
        self.playlist.remove(playlist)

    def commentaVideo(self, video, commento):
        video.commenti.append(commento)


class Video:
    def __init__(self, titolo, descrizione, url, durata):
        self.titolo = titolo
        self.descrizione = descrizione
        self.url = url
        self.durata = durata
        self.commenti = []

    def aggiungiCommento(self, commento):
        self.commenti.append(commento)  

class Playlist:
    def __init__(self, nome, creatore):
        self.nome = nome
        self.creatore = creatore
        self.videos = []

    def aggiungiVideo(self, video):
        self.videos.append(video)

    def rimuoviVideo(self, video):
        self.videos.remove(video)

class Abbonamento:
    def __init__(self, tipo, prezzo, dataInizio, dataFine):
        self.tipo = tipo
        self.prezzo = prezzo
        self.dataInizio = dataInizio
        self.dataFine = dataFine

class Commento:
    def __init__(self, testo, dataPubblicazione):
        self.testo = testo
        self.dataPubblicazione = dataPubblicazione


def main():
    utente1 = Utente("Mario", "password", "mariolastreet@mail.com")
    video1 = Video("Pierluigi e i soldi", "il protagonista pierluigi ha una missione importante: deve diventare milionario", "", 10)
    video2 = Video("Angelo e il trading", "Angelo e pierluigi sono i protagonisti, devono fare soldi con il trading, ci riusciranno?", "url2", 15)
    commento1 = Commento("Molto bello, aspetto il sequel", "01/01/2021")
    video1.aggiungiCommento(commento1)
    playlist1 = Playlist("Miei video preferiti", utente1)
    playlist1.aggiungiVideo(video1)
    playlist1.aggiungiVideo(video2)
    
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n1. Aggiungi video")
        print("2. Cerca video")
        print("3. Visualizza video")
        print("4. Esci")
        scelta = input("Cosa vuoi fare? ")
        if scelta == "1":
            titolo = input("Titolo: ")
            descrizione = input("Descrizione: ")
            url = input("URL: ")
            durata = int(input("Durata: "))
            video = Video(titolo, descrizione, url, durata)
            playlist1.aggiungiVideo(video)
            input("\nVideo aggiunto. Premi Invio per continuare...")
        elif scelta == "2":
            chiave = input("Cerca: ")
            risultati = [video for video in playlist1.videos if chiave.lower() in video.titolo.lower()]
            if len(risultati) == 0:
                print("Nessun risultato")
            else:
                for video in risultati:
                    print(video.titolo)
            input("\nPremi Invio per continuare...")
        elif scelta == "3":
            for video in playlist1.videos:
                print(video.titolo)
            input("\nPremi Invio per continuare...")
        elif scelta == "4":
            break
        else:
            print("Scelta non valida")
            input("\nPremi Invio per continuare...")

if __name__ == "__main__":
    main()
