```mermaid
classDiagram
class ElementoMenu {
+List[Primo] primi
+List[Secondo] secondi
+str nome
+str codice
+str tempo_di_preparazione
+str allergeni
+bool disponibile
+int prezzo
+ getNome()
+ getCodice()
+ getTempoDiPreparazione()
+ getAllergeni()
+ getDisponibile()
+ getPrezzo()
+ set_disponibile()
+ to_string() 
}

class Primo {
+ElementoMenu menu
+str tipo_pasta
+bool vegetariano
+ to_string()
}

class Secondo {
+ElementoMenu menu
+str tipo_cottura
+ to_string()
}

class Ordine {
+List[Tavolo] tavoli
+str numero_ordine
+datetime data_ora
+str stato
+str elementi
+ calcola_totale()
+ aggiungi_elemento()
+ rimuovi_elemento()
+ stato(in_attesa, in_preparazione, pronto, servito)
+ to_string()
}
class Tavolo {
+Ordine ordini
+str numero
+str posti
+str stato
+ stato(libero, occupato)
+ is_libero() : str
+ aggiungi_ordine()
+ get_ordini_attivi()
+ to_string()
}

ElementoMenu "1" -- "*" Primo : contiene
ElementoMenu "1" -- "*" Secondo : contiene
Ordine "1" -- "*" ElementoMenu : contiene
Ordine "1" -- "*" Tavolo : associato