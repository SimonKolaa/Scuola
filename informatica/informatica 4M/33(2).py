class Utente:
    def __init__(self, nome, cognome, email):
        self.nome = nome
        self.cognome = cognome
        self.email = email

    def guardaVideo(self, video):
        self.videoVisti.append(video)
    
    def creaPlaylist(self, playlist):
        self.playlist.append(playlist)

    def aggiungiVideoPlaylist(self, playlist, video):
        playlist.videos.append(video)

    def rimuoviVideoPlaylist(self, playlist, video):
        playlist.videos.remove(video)

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

