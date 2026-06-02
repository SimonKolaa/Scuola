import json
def read_file_json (worked_hours: str) -> list:
    with open('worked_hours.json', 'r') as f:
        links = json.load(f)
    return list
def update_file_json(filename: str, worked_hours: list) -> None:
      with open(worked_hours, "w") as file_json:
        json.dump(obj=list, fp=file_json, indent=4)



def add_new_user_data (old_list:list, name: str, surname: str, worked_hours: int, hourly_pay: float) -> None:
    
    user_item = {"name" : "<nome_utente>",
"surname" : "<cognome_utente>",
"worked_hours" : "<ore_lavorate>",
"hourly_pay" : "<paga_oraria>",
"total" : "<totale>"}
def aggiungi_lista(dict_da_aggiungere: dict, lista: str) -> list:
    lista.append(dict_da_aggiungere)
    return lista

def print_list(worked_hours: list) -> None:
    print(worked_hours)

def get_item_by_name(filename: str, name: str, surname: str) -> list:
 with open('worked_hours.json', 'r') as f:
        links = json.load(f)
        return list








def CLIApplication():
    nome = input("come ti chiami?")
    cognome = input("come fai di cognome?")
    worked_hours = input("quante ore hai lavorato?")
    hourly_pay = input("quanti soldi all'ora?")
    total = input("totale?")
    lista = read_file_json("worked_hours.json")
def aggiungi_lista(dict_da_aggiungere: dict, lista: str) -> list:
    lista.append(dict_da_aggiungere)
    return lista
    print()

    if __name__ == "__main__":
        CLIApplication()
