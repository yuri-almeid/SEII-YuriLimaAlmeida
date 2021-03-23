 #include <iostream>
using namespace std;

void hanoi(int n,char origem,char destino,char auxiliar){
	/*Se sobrar apenas o disco 1, mova fazer o movimento e retornar*/
	if(n==1){ 

        cout << "\nMova o disco 1 da base " << origem  << " para a base " << destino;
		return;
	}
	/*Mover o n-1 disco de A para B, usando C de auxiliar*/
	hanoi(n-1,origem,auxiliar,destino);
	/* Mover os discos restantes de A para C*/
    cout << "\nMova o disco " << n << " da base " << origem << " para a base " << destino;

	/*Mover os n-1 discos de B para C usando A como auxiliar*/
	hanoi(n-1,auxiliar,destino,origem);
}

int main() {
    int n;
    cout << "Digite o numero de discos : ";
    cin >> n;
    cout << "Para resolver a torre de Hanois faça :";
    hanoi(n,'A','C','B');
    cout << "\n";
    return 0;
} 