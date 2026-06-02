class Pagamento:
    def __init__(self, processa_pagamento):
        self.processa_pagamento = processa_pagamento

    def processa_pagamento(self):
        self.processa_pagamento()

class CartaCredito(Pagamento):
    def __init__(self, nome, numero, scadenza, cvv):
        self.nome = nome
        self.numero = numero
        self.scadenza = scadenza
        self.cvv = cvv

    def processa_pagamento(self):
        print("pagamento con carta di credito")

class PayPal(Pagamento):
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def processa_pagamento(self):
        print("pagamento con PayPal")

def effettua_pagamento(metodo_di_pagamento: Pagamento):
    metodo_di_pagamento.processa_pagamento()

# Esempio di utilizzo
pagamento_carta = CartaCredito("Mario Monticelli", "5105 0800 1413 5391", "09/29", "123")
pagamento_paypal = PayPal("cardonelavrai@darkweb.com", "DarioCasali2010")

effettua_pagamento(pagamento_carta)  
effettua_pagamento(pagamento_paypal)