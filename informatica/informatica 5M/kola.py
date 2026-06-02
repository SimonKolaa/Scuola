import requests

# URL base - CONTROLLA LA PORTA nel messaggio del server!
BASE_URL = "http://localhost:3000"




try:
    response = requests.get(f"{BASE_URL}/projects?dev_id=1")
    response.raise_for_status()
    projects = response.json()
    
    print(projects)
    for p in projects:
        print(f"  - {p['name']} ({p['budget']})")
    
 
    

except requests.exceptions.RequestException as e:
    print(f"Errore nella richiesta: {e}")    

#2. Calcolo Carico di Lavoro
active_projects = []
for p in projects:
    if p["status"] == "active":
        active_projects.append(p)
        
    print("progetti attivi")
    for p in active_projects:
        print(f"  - {p['name']}")
   
#Per ogni progetto attivo, recupera la lista dei suoi task.     
    print("task")
    for p in active_projects:
        task_response = requests.get(f"{BASE_URL}/tasks?project_id=(p['id'])")
        task_response.raise_for_status()
        task = task_response.json()

        ore_totali = 0
        for i in task:
            ore_totali += i['pages']
    
#3. Assegnazione Nuovo Task
#Scegli (tramite codice) il primo progetto attivo trovato.
if len(active_projects) > 0:
    primo_progetto = active_projects[0]
#Utilizzando una richiesta POST, crea un nuovo task per questo progetto con i seguenti dati:
nuovo_task = {
    "project_id": 'primo_progetto["id"]',
    "description": "Code Review Finale",
    "is_done": False,
    "hours_estimated": "3"  
}
    
post_response = requests.put(f"{BASE_URL}/tasks" , json=nuovo_task)
post_response.raise_for_status()
creato = post_response.json()

print("nuovo task creato")

#Pulizia
#Trova il primo task completato (is_done: true).
task_completato = []
#Simula la sua eliminazione tramite una richiesta DELETE.

try:
    # DELETE richiesta
    task = requests.delete(f"{BASE_URL}/tasks/{id}")
    task_response.raise_for_status()   
    #Stampa l'ID del task eliminato.
    print(f"Eliminato elemento ID: {id}")
except requests.exceptions.RequestException as e:
    print(f"Errore: {e}")
# if __name__ == "__main__":
#     main()