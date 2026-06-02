class Libro
    def __init__(self, titulo, autor, editorial, año):
        self.titolo = titolo
        self.autore = autore
        self.pagine = pagine
        self.anno = anno
        
 def get_titolo(self):
        return self.titolo

    def set_titolo(self, titolo):
        if titolo:
            self.titolo = titolo

    def get_autore(self):
        return self.autore

    def set_autore(self, autore):
        if autore:
            self.autore = autore

    def get_pagine(self):
        return self.pagine

    def set_pagine(self, pagine):
        if pagine > 0:
            self.pagine = pagine

    def get_anno(self):
        return self.anno

    def set_anno(self, anno):
        if anno > 0:
            self.anno = anno
            
Libro1 = Libro("CasaLi neL 1980", "J.R.R. Tolkien", 1200, 1954)
  print(libro1.get_titolo())  
  print(libro1.get_autore())  
  print(libro1.get_pagine())  
  print(libro1.get_anno())     
  
         