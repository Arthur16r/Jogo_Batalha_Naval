
#  Batalha Naval em Python

## Descrição

Este projeto é uma recriação do clássico jogo **Batalha Naval**, totalmente implementado em **Python**.  
O jogador enfrenta o **computador**, posicionando embarcações em um tabuleiro 10x10 e tentando afundar todas as do adversário antes que ele afunde as suas.

O código foi dividido em dois arquivos principais para melhor organização:
- `BATALHA NAVAL.py`: contém o fluxo principal do jogo e as interações com o usuário.
- `funcoes_batalha_naval.py`: contém todas as funções auxiliares responsáveis pela lógica de posicionamento, exibição e execução das jogadas.

---

## ⚙️ Estrutura dos Arquivos

```
 Batalha_Naval/
├── BATALHA NAVAL.py
└── funcoes_batalha_naval.py
```

---

##  Funcionalidades Principais

- **Posicionamento manual das embarcações**.
- **Posicionamento automático do computador**.
- **Modo de jogo interativo com ataques por coordenadas**.
- **Sistema de pontuação** com vitória ao atingir 16 acertos.
- **Modo de teste (debug)** que revela o tabuleiro inimigo.

---

##  Como Jogar

1. Execute o arquivo principal:
   ```bash
   python "BATALHA NAVAL.py"
   ```

2. Siga as instruções no terminal:
   - Posicione suas embarcações no tabuleiro digitando as coordenadas `x` e `y`.
   - Escolha a direção do navio (cima, baixo, direita ou esquerda).
   - Após todos os barcos serem posicionados, a partida começa.

3. Durante a partida:
   - Digite as coordenadas do ataque (de 0 a 9).
   - “X” indica acerto e “~” indica erro.
   - O computador realiza ataques automaticamente.

4. O jogo termina quando:
   - Você ou o computador atingir **16 pontos** (todas as embarcações do oponente destruídas).

---

##  Tipos de Embarcações

| Tipo de barco | Tamanho | Quantidade |
|----------------|----------|------------|
| Porta-aviões   | 5 casas  | 1          |
| Navio-tanque   | 4 casas  | 1          |
| Cruzador       | 3 casas  | 1          |
| Submarino      | 2 casas  | 2          |

---

##  Regras do Jogo

- Cada acerto dá direito a **jogar novamente**.
- Caso ataque uma posição já escolhida, **perde a vez**.
- Os símbolos do tabuleiro:
  - `^` → Embarcação do jogador  
  - `*` → Embarcação do computador (oculto durante o jogo normal)  
  - `X` → Acerto  
  - `~` → Erro  

---

##  Lógica e Implementação

O jogo utiliza:
- **Listas bidimensionais (matrizes)** para representar os tabuleiros.
- **Loops e condicionais** para controle de jogadas e limites.
- **Módulo `random`** para ataques e posicionamentos automáticos.
- **Funções modulares** para clareza e reutilização de código.

---

##  Funções Principais

| Função | Descrição |
|--------|------------|
| `colocar_embarcacao()` | Permite ao jogador escolher a posição e direção dos barcos. |
| `colocar_embarcacao_aleatoria()` | Posiciona os barcos do computador aleatoriamente. |
| `mostra_tabuleiro()` | Exibe o tabuleiro no console com coordenadas. |
| `comecar_partidada()` | Controla o fluxo principal da partida e verifica o vencedor. |

---

##  Desenvolvido por

**Arthur Ribeiro Gonçalves**  
Estudante de **Engenharia da Computação**
