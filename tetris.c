#include <stdlib.h>
#include <stdio.h>
#include <string.h>
typedef enum {
    T=1,S1,S2,I,L1,L2,Q
}peca_tipo;

typedef struct{
    int peso;
    int tamanho;
    char cor[8];
    char borda[2];
    peca_tipo tipo;
}peca;

int comparar_tipo(const void *a,const void *b){

    peca *peca_a = (peca*)a;
    peca *peca_b = (peca*)b;
    
    // Comparando os tipos
    return peca_a->tipo - peca_b->tipo;
}





void limpar_buffer(){
    while (getchar() != '\n');
}


const char* tipo_string(peca_tipo tipo) {
    switch (tipo) {
        case T: return "T";
        case S1: return "S1";
        case S2: return "S2";
        case I: return "I";
        case L1: return "L1";
        case L2: return "L2";
        case Q: return "Q";
        default: return "Digite um valor correto";
    }
}


int main(){
    peca *pecas;
    int resposta;
    int qtd_pecas;
    int i;
    
    

    while(1){
    
    
    printf("\n[1] Cadastrar peca\n[2]Ver pecas\n[3]Organizar pecas\n[4]Sair\n");
    scanf("%d",&resposta);
    
    switch (resposta){
    case 1:
        printf("Quantas pecas deseja cadastrar: ");
        scanf("%d",&qtd_pecas);
        pecas=malloc(sizeof(*pecas)*qtd_pecas);
        if(pecas==NULL){
            printf("Erro na alocacao de memoria");
            exit(1);
        }

            for(i=0;i<qtd_pecas;i++){
            printf("selecione o tipo:\n[1] T\n[2] S1\n[3] S2\n[4] I\n[5] L1\n[6] L2\n[7] Q\n");
            scanf("%d",(int*)&pecas[i].tipo);
            
        
            printf("Digite a cor: ");
            scanf("%7s",pecas[i].cor);

            printf("Digite o tamanho: ");
            scanf("%d",&pecas[i].tamanho);
            limpar_buffer();

            printf("Digite o peso: ");
            scanf("%d",&pecas[i].peso);
            limpar_buffer();
            
            printf("Possui borda: ");
            scanf("%2s",pecas[i].borda);
        
            }
            break;
            
        
        
        
        case 2:
            printf("\nPecas cadastradas: ");
            
            for(i=0;i<qtd_pecas;i++){
                printf("\nPeca %d",i);
                printf("\nTipo: %s",tipo_string(pecas[i].tipo));
                printf("\nCor: %s",(pecas+i)->cor);
                printf("\nTamanho:%d",(pecas+i)->tamanho);
                printf("\nPeso: %d",(pecas+i)->peso);
                printf("\nBorda: %s\n",(pecas+i)->borda);
            }
            
            break;

        case 3:
            printf("Pecas organizadas: ");
            qsort(pecas,qtd_pecas,sizeof(peca),comparar_tipo);
            for(i=0;i<qtd_pecas;i++){
                printf("\nPeca %d",i);
                printf("\nTipo: %s",tipo_string(pecas[i].tipo));
                printf("\nCor: %s",(pecas+i)->cor);
                printf("\nTamanho:%d",(pecas+i)->tamanho);
                printf("\nPeso: %d",(pecas+i)->peso);
                printf("\nBorda: %s\n",(pecas+i)->borda);
                
                }
                
            
        case 4:
            printf("Ate logo");
            exit(1);
            
        default:
            break;
            
            
            }
               
    

    }

    free(pecas);
}


