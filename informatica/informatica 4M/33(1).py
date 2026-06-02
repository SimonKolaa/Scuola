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
    video2 = Video("Angelo", "Descrizione video 2", "url2", 15)
    commento1 = Commento("Molto bello, aspetto il sequel", "01/01/2021")