#include <pthread.h>
#include <stdio.h>
#include <unistd.h>
#include <string.h>

// Mutexes para os trilhos compartilhados
pthread_mutex_t trilho_L3 = PTHREAD_MUTEX_INITIALIZER;
pthread_mutex_t trilho_L5 = PTHREAD_MUTEX_INITIALIZER;

// Mutex para proteger a tabela de estado
pthread_mutex_t estado_mutex = PTHREAD_MUTEX_INITIALIZER;

// Estados dos trens e mutexes
typedef struct {
    char trem1[20];
    char trem2[20];
    char trem3[20];
    char mutex_L3[10];
    char mutex_L5[10];
} Estado;

Estado estado = {
    .trem1 = "Iniciando",
    .trem2 = "Iniciando",
    .trem3 = "Iniciando",
    .mutex_L3 = "Livre",
    .mutex_L5 = "Livre"
};

// Função auxiliar para imprimir a tabela de estados
void imprimir_tabela() {
    pthread_mutex_lock(&estado_mutex);
    printf("\n");
    printf("| Trem      | Seção Atual | Mutex L3 | Mutex L5 |\n");
    printf("|-----------|-------------|----------|----------|\n");
    printf("| Verde     | %-11s | %-8s | %-8s |\n", estado.trem1, estado.mutex_L3, estado.mutex_L5);
    printf("| Roxo      | %-11s | %-8s | %-8s |\n", estado.trem2, estado.mutex_L3, estado.mutex_L5);
    printf("| Vermelho  | %-11s | %-8s | %-8s |\n", estado.trem3, estado.mutex_L3, estado.mutex_L5);
    pthread_mutex_unlock(&estado_mutex);
}

// Função do trem 1
void* trem1(void* arg) {
    while (1) {
        pthread_mutex_lock(&estado_mutex);
        strcpy(estado.trem1, "L1 -> L2");
        pthread_mutex_unlock(&estado_mutex);
        imprimir_tabela();
        sleep(1);

        pthread_mutex_lock(&trilho_L3);
        pthread_mutex_lock(&estado_mutex);
        strcpy(estado.trem1, "L3");
        strcpy(estado.mutex_L3, "Ocupado");
        pthread_mutex_unlock(&estado_mutex);
        imprimir_tabela();
        sleep(1);

        pthread_mutex_lock(&estado_mutex);
        strcpy(estado.trem1, "Saindo L3");
        strcpy(estado.mutex_L3, "Livre");
        pthread_mutex_unlock(&estado_mutex);
        pthread_mutex_unlock(&trilho_L3);
        imprimir_tabela();

        pthread_mutex_lock(&estado_mutex);
        strcpy(estado.trem1, "L4");
        pthread_mutex_unlock(&estado_mutex);
        imprimir_tabela();
        sleep(1);
    }
    return NULL;
}

// Função do trem 2
void* trem2(void* arg) {
    while (1) {
        pthread_mutex_lock(&estado_mutex);
        strcpy(estado.trem2, "L6");
        pthread_mutex_unlock(&estado_mutex);
        imprimir_tabela();
        sleep(1);

        pthread_mutex_lock(&trilho_L3);
        pthread_mutex_lock(&estado_mutex);
        strcpy(estado.trem2, "L3");
        strcpy(estado.mutex_L3, "Ocupado");
        pthread_mutex_unlock(&estado_mutex);
        imprimir_tabela();
        sleep(1);

        pthread_mutex_lock(&estado_mutex);
        strcpy(estado.trem2, "Saindo L3");
        strcpy(estado.mutex_L3, "Livre");
        pthread_mutex_unlock(&estado_mutex);
        pthread_mutex_unlock(&trilho_L3);
        imprimir_tabela();

        pthread_mutex_lock(&estado_mutex);
        strcpy(estado.trem2, "L7");
        pthread_mutex_unlock(&estado_mutex);
        imprimir_tabela();
        sleep(1);
    }
    return NULL;
}

// Função do trem 3
void* trem3(void* arg) {
    while (1) {
        pthread_mutex_lock(&estado_mutex);
        strcpy(estado.trem3, "L8");
        pthread_mutex_unlock(&estado_mutex);
        imprimir_tabela();
        sleep(1);

        pthread_mutex_lock(&trilho_L5);
        pthread_mutex_lock(&estado_mutex);
        strcpy(estado.trem3, "L5");
        strcpy(estado.mutex_L5, "Ocupado");
        pthread_mutex_unlock(&estado_mutex);
        imprimir_tabela();
        sleep(1);

        pthread_mutex_lock(&estado_mutex);
        strcpy(estado.trem3, "Saindo L5");
        strcpy(estado.mutex_L5, "Livre");
        pthread_mutex_unlock(&estado_mutex);
        pthread_mutex_unlock(&trilho_L5);
        imprimir_tabela();

        pthread_mutex_lock(&estado_mutex);
        strcpy(estado.trem3, "L9");
        pthread_mutex_unlock(&estado_mutex);
        imprimir_tabela();
        sleep(1);
    }
    return NULL;
}

int main() {
    pthread_t t1, t2, t3;

    // Cabeçalho inicial
    printf("\n");
    printf("Simulacao do Problema dos Trens\n");

    // Criação das threads
    pthread_create(&t1, NULL, trem1, NULL);
    pthread_create(&t2, NULL, trem2, NULL);
    pthread_create(&t3, NULL, trem3, NULL);

    // Junta as threads
    pthread_join(t1, NULL);
    pthread_join(t2, NULL);
    pthread_join(t3, NULL);

    return 0;
}