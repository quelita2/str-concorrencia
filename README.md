# **Sistemas de Tempo Real (STR) - Programação Concorrente**

Este repositório contém implementações e exemplos relacionados aos conceitos e primitivas de Programação Concorrente aplicados na matéria de Sistemas de Tempo Real (STR). O objetivo deste projeto é explorar como gerenciar múltiplas tarefas concorrentes, garantindo comunicação e sincronização adequadas entre elas, utilizando as principais primitivas de programação concorrente.

O diretório principal foi organizado da seguinte maneira para facilitar a compreensão dos temas abordados na 2ª unidade da matéria de STR:

```
/tarefaX
    /docs         # Materiais disponibilizados para as atividades
    /assets       # Arquivos de recursos estáticos, como imagens
    /src          # Código-fonte da implementação da atividade de programação concorrente
    README.md     # Documentação com explicação da tarefa
```

## **Unidade 2 - Tópicos Abordados**

### 1. **Conceitos de Programação Concorrente**

Programação concorrente refere-se à execução de múltiplas tarefas ou processos ao mesmo tempo, onde a comunicação e sincronização adequadas entre as tarefas são essenciais para evitar condições de corrida e garantir a integridade dos dados. Os principais conceitos envolvidos incluem:

- **Tarefas**: Unidades independentes de execução que podem ser executadas concorrentemente.
- **Concorrência**: A execução simultânea de várias tarefas, que podem ou não ser executadas de forma paralela, dependendo do hardware disponível.
- **Comunicação**: Mecanismos que permitem que as tarefas troquem informações entre si.
- **Sincronização**: Garantia de que as tarefas sejam executadas de maneira coordenada, sem conflitos.

### 2. **Primitivas de Programação Concorrente**

As primitivas básicas de programação concorrente que serão exploradas neste projeto incluem:

- **Tarefas**: A criação e o gerenciamento de múltiplas tarefas.
- **Mutex**: Uma ferramenta para garantir que apenas uma tarefa acesse um recurso compartilhado de cada vez.
- **Semáforos**: Mecanismo de controle para permitir a sincronização entre tarefas, controlando o acesso a recursos compartilhados.

### 3. **Problema da Exclusão-Mútua e Região Crítica**

A **exclusão mútua** é um problema que ocorre quando duas ou mais tarefas tentam acessar um recurso compartilhado simultaneamente, causando inconsistência nos dados. Para resolver isso, usamos mecanismos de **sincronização** (como mutexes ou semáforos) para garantir que apenas uma tarefa acesse a região crítica de cada vez.

### 4. **Problema de Dead-lock e Starvation**

**Dead-lock** ocorre quando duas ou mais tarefas ficam bloqueadas esperando por recursos que nunca estarão disponíveis, criando um ciclo de espera infinita. Já o **starvation** ocorre quando uma tarefa nunca recebe a oportunidade de ser executada porque outras tarefas monopolizam o recurso.

Esses problemas são comuns em sistemas concorrentes e serão abordados com exemplos de soluções que evitam ou resolvem esses problemas, garantindo que o sistema continue funcionando de maneira eficiente.

---
<div align="center">
  📚 DCA0125 - <strong> SISTEMAS DE TEMPO REAL </strong> - T01 (2024.2 - 24T34) 🎓 <br/>
  Universidade Federal do Rio Grande do Norte - Departamento de Computação e Automação (DCA). 🏛️
</div>