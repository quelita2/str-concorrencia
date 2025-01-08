#include <stdio.h>
#include <pthread.h>
#include <unistd.h>

// Mutexes para as seções críticas
pthread_mutex_t L3 = PTHREAD_MUTEX_INITIALIZER;
pthread_mutex_t L4 = PTHREAD_MUTEX_INITIALIZER;
pthread_mutex_t L6 = PTHREAD_MUTEX_INITIALIZER;

// Variáveis globais para estado dos trens
const char* trem_verde_estado = "L1";
const char* trem_roxo_estado = "L5";
const char* trem_vermelho_estado = "L8";

// Função para imprimir o estado em formato de tabela
void imprimir_estado(const char* verde, const char* roxo, const char* vermelho) {
    // Imprimindo o estado dos trens
    printf("\n| Trem      | Seção Atual  | Mutex L3  | Mutex L4  | Mutex L6  |\n");
    printf("|-----------|--------------|-----------|-----------|-----------|\n");

    // Verde
    if (verde == "L1" || verde == "L2") {
        printf("| Verde     | %-12s | %-9s | %-9s | %-9s |\n", verde, 
            pthread_mutex_trylock(&L3) ? "Ocupado" : "Livre",
            pthread_mutex_trylock(&L4) ? "Ocupado" : "Livre",
            pthread_mutex_trylock(&L6) ? "Ocupado" : "Livre");
    } else {
        printf("| Verde     | Saindo %-5s | %-9s | %-9s | %-9s |\n", verde, 
            pthread_mutex_trylock(&L3) ? "Ocupado" : "Livre",
            pthread_mutex_trylock(&L4) ? "Ocupado" : "Livre",
            pthread_mutex_trylock(&L6) ? "Ocupado" : "Livre");
    }

    // Roxo
    printf("| Roxo      | %-12s | %-9s | %-9s | %-9s |\n", roxo,
            pthread_mutex_trylock(&L3) ? "Ocupado" : "Livre",
            pthread_mutex_trylock(&L4) ? "Ocupado" : "Livre",
            pthread_mutex_trylock(&L6) ? "Ocupado" : "Livre");

    // Vermelho
    printf("| Vermelho  | %-12s | %-9s | %-9s | %-9s |\n", vermelho,
            pthread_mutex_trylock(&L3) ? "Ocupado" : "Livre",
            pthread_mutex_trylock(&L4) ? "Ocupado" : "Livre",
            pthread_mutex_trylock(&L6) ? "Ocupado" : "Livre");

    // Liberando os mutexes
    pthread_mutex_unlock(&L3);
    pthread_mutex_unlock(&L4);
    pthread_mutex_unlock(&L6);
}

// Código do Trem Verde
void* trem_verde(void* arg) {
    while (1) {
        trem_verde_estado = "L1";
        sleep(1);
        trem_verde_estado = "L2";
        sleep(1);

        pthread_mutex_lock(&L3);
        trem_verde_estado = "L3";
        imprimir_estado(trem_verde_estado, trem_roxo_estado, trem_vermelho_estado);
        sleep(1);
        pthread_mutex_unlock(&L3);

        pthread_mutex_lock(&L4);
        trem_verde_estado = "L4";
        imprimir_estado(trem_verde_estado, trem_roxo_estado, trem_vermelho_estado);
        sleep(1);
        pthread_mutex_unlock(&L4);
    }
}

// Código do Trem Roxo
void* trem_roxo(void* arg) {
    while (1) {
        trem_roxo_estado = "L5";
        sleep(1);

        pthread_mutex_lock(&L6);
        trem_roxo_estado = "L6";
        imprimir_estado(trem_verde_estado, trem_roxo_estado, trem_vermelho_estado);
        sleep(1);
        pthread_mutex_unlock(&L6);

        pthread_mutex_lock(&L3);
        trem_roxo_estado = "L3";
        imprimir_estado(trem_verde_estado, trem_roxo_estado, trem_vermelho_estado);
        sleep(1);
        pthread_mutex_unlock(&L3);

        trem_roxo_estado = "L7";
        sleep(1);
    }
}

// Código do Trem Vermelho
void* trem_vermelho(void* arg) {
    while (1) {
        trem_vermelho_estado = "L8";
        sleep(1);

        pthread_mutex_lock(&L4);
        trem_vermelho_estado = "L4";
        imprimir_estado(trem_verde_estado, trem_roxo_estado, trem_vermelho_estado);
        sleep(1);
        pthread_mutex_unlock(&L4);

        pthread_mutex_lock(&L6);
        trem_vermelho_estado = "L6";
        imprimir_estado(trem_verde_estado, trem_roxo_estado, trem_vermelho_estado);
        sleep(1);
        pthread_mutex_unlock(&L6);

        trem_vermelho_estado = "L10";
        sleep(1);
    }
}

int main() {
    pthread_t verde, roxo, vermelho;

    // Criação das threads
    pthread_create(&verde, NULL, trem_verde, NULL);
    pthread_create(&roxo, NULL, trem_roxo, NULL);
    pthread_create(&vermelho, NULL, trem_vermelho, NULL);

    // Join threads
    pthread_join(verde, NULL);
    pthread_join(roxo, NULL);
    pthread_join(vermelho, NULL);

    return 0;
}