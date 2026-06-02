/******************************************************************************
Autori:              Kola Simon
Classe:              1M
Data:                15/04/2021
Descrizione:         Calcolo Area e Perimetro di un Reattangolo
*******************************************************************************/
#include <iostream>
using namespace std;

int main()
{
    int skLato1;
    int skLato2;
    int skPerimetro;
    int skArea;
    
    cout << "Calcolo Area e Perimetro di un Reattangolo " <<endl <<endl;
    
    cout <<"inserisci dimensione lato: ";
    cin >> skLato1;
    cout <<"inserisci dimensione lato: ";
    cin >> skLato2;
    
    //Elaboro
    skPerimetro = skLato1 * 2 + skLato2 * 2;
    skArea = skLato1 * skLato2;
    
    //Visualizza risultati
    
    cout <<endl;
    cout << "Area    " <<skArea;
    cout << "Perimetro " <<skPerimetro;
   

    return 0;
}
/******************************************************************************
Autore:        Kola Simon
classe:         1M
Data:          09/04/2021
Descrizione:  Es pag298
*******************************************************************************/
#include <iostream>

using namespace std;

int main()
{
    int skx,sky;
    float skLato1, skLato2, skAltezza, skVolume;
    
    cout << "Dammi il numero che vuoi che assegni a agx";
    cin >> sky;
    skx=sky;
    cout << "Il numero che mi hai dato è:      "
    <<agx<<endl<<endl;
    
    cout << "Dammi un numero e io ti dirò il suo successivo";
    cin >> skx;
    skx=skx+1;
    cout << "Il successivo è:     " <<skx 
    <<endl <<endl;
    
    cout << "Dammi il primo lato della base della piramide";
    cin >> skLato1;
    cout << "Dammi il secondo lato della base della peramide";
    cin >> skLato2;
    cout << "Dammi l'altezza della piramide";
    cin >> skAltezza;
    skVolume=skLato1*skLato2*skAltezza/3;
    cout <<"Il volume della piramide é:     "
    << skVolume <<endl;
    

    return 0;
}