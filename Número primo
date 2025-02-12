#include <stdlib.h>
#include <stdio.h>
#include <math.h>


void primo(long long int numero){
    long long int raiz;
    long long int divisor;
    raiz=sqrt(numero);
    if (numero==2 || numero==3 || numero==1){
        printf("Numero Primo");
    }
    else{
    
    for(divisor=2;divisor<=raiz;divisor++){
        
        
        if(numero%divisor==0){
            printf("Divisor de %lld : %lld",numero,divisor);
            break;
        }
        if(raiz==divisor){
            printf("Numero primo");
        }
    }
    

    }
}

int main(){
    while(1){
    long long int numero;
    printf("\nDigite um numero: ");
    scanf(" %lld",&numero);
    
    primo(numero);
    }
    
}
