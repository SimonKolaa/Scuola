#include<iostream>

/*
ati tre votisu una materiadire se promuoverlo o bocciarlo
*/
using namespace std;

int main()
{double n1,n2,n3,ris;
cout<<"primo voto";
cin>>n1;
cout<<"secondo voto";
cin>>n2;
cout<<"terzo voto";
cin>>n3;

if ((n1+n2+n3)/3>=6){
	cout<<"PROMOSSO";
}
else {
	cout<<"BOCCIATO";
}
}
