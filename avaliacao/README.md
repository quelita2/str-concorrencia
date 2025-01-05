# Gerenciador de Tarefas

Este projeto é um Gerenciador de Tarefas que permite monitorar processos em tempo real no sistema, com funcionalidades similares ao `htop` no Linux. A aplicação fornece informações detalhadas sobre os processos, como:

- PID (Process ID)
- Nome do processo
- Uso de CPU (%)
- Status do processo (Executando, Suspenso, etc.)
- Prioridade do processo
- PPID (Parent Process ID)

Além disso, oferece funcionalidades para gerenciar os processos diretamente pela interface.

## Funcionalidades

1. **Monitoramento de Processos**:
  - Exibe uma lista em tempo real de todos os processos em execução no sistema.
  - Atualiza automaticamente as informações a cada segundo.

2. **Filtragem**:
  - Permite filtrar processos pelo nome para facilitar a visualização.

3. **Controle de Processos**:
  - Matar Processo: Finaliza um processo selecionado.
  - Suspender Processo: Pausa a execução de um processo.
  - Continuar Processo: Retoma a execução de um processo suspenso.

4. **Interface Intuitiva**:
  - Tabela com colunas centralizadas para facilitar a leitura das informações.

## Como Executar

Execute o arquivo principal do projeto:
  ```bash
  python main.py
  ```

---
<div align="center">
  📚 DCA0125 - <strong> SISTEMAS DE TEMPO REAL </strong> - T01 (2024.2 - 24T34) 🎓 <br/>
  Universidade Federal do Rio Grande do Norte - Departamento de Computação e Automação (DCA). 🏛️
</div>