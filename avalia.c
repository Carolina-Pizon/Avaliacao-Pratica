#include <stdio.h>
#include <stdbool.h>
int main()
{
    // FUNÇÃO 1
void servicoSpaPes(float preco)
{
    printf("O valor do servico Spa dos Pes custa R$ %.2f\n", preco);
}

// FUNÇÃO 2
void servicoSpaMaos(float preco)
{
    printf("O valor do servico Spa das Maos custa R$ %.2f\n", preco);
}

// FUNÇÃO 3
void servicoManicure(float preco)
{
    printf("O valor do servico Manicure custa R$ %.2f\n", preco);
}
    // Tipos de Dados Utilizados (char, float e int)
    char nome[61];
    float spa_pes = 150.00;
    float spa_maos = 160.00;
    float manicure = 50.00;
    float pedicure = 50.00;
    float massagem = 100.00;
    int opcao;



    // Paradigma Imperativo :
    // Pilares - Imutabilidade de estado e comandos sequenciais
    printf("===============SEJA BEM-VINDO AO SPA DELUXE===============\n");
    printf("1 - SPA DOS PES\n");
    printf("2 - SPA DAS MAOS\n");
    printf("3 - MANICURE\n");
    printf("4 - PEDICURE\n");
    printf("5 - MASSAGEM\n");
   
    printf("Escolha somente um dos pacotes promocionais:", opcao);
    scanf("%d", & opcao);

    //Utiliza estruturas de controle - condicionais (if/else)
    if (opcao == 1){
        printf("O valor do servico custa R$ %.2f\n",  spa_pes);
    }
    else if (opcao == 2){
        printf("O valor do servico custa R$ %.2f\n",  spa_maos);
    }
    else if(opcao == 3){
        printf("O valor do servico custa R$ %.2f\n",  manicure);
    }
    else if(opcao == 4){
        printf("O valor do servico custa R$ %.2f\n",  pedicure);
    }
    else if(opcao == 5){
        printf("O valor do servico custa R$ %.2f\n",  massagem);
    }
    else{
        printf("Opção Inválida\n");
    }

    printf("Qual o seu nome?\n", nome);
    scanf("%s", nome);

    printf("Promoção Relâmpago - Você ganhou mais 10 por cento de desconto");

return 0;

}
