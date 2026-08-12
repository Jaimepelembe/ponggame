# 🏓 Jogo Pong

Um jogo clássico de Pong desenvolvido em Python utilizando o módulo Turtle, onde dois jogadores controlam raquetes para rebater uma bola e marcar pontos. O objetivo é conseguir mais pontos que o adversário.

## 📋 Descrição

Este é um jogo simples desenvolvido com o módulo Turtle, uma biblioteca padrão do Python. O jogo simula uma partida de ténis de mesa, onde dois jogadores controlam raquetes posicionadas em lados opostos do ecrã.

A bola movimenta-se automaticamente pelo campo e pode ser rebatida pelas raquetes. Sempre que um jogador falha a bola, o adversário marca um ponto.

O objetivo é obter a maior pontuação possível antes que o adversário consiga superar a sua pontuação.

O jogo termina quando um dos jogadores atinge a pontuação máxima definida. O jogador que alcançar essa pontuação primeiro é declarado vencedor, sendo apresentada uma mensagem de vitória no ecrã.

## ✨ Funcionalidades

- Controlo das duas raquetes através do teclado;
- Movimento automático da bola;
- Deteção de colisão da bola com as raquetes;
- Deteção de colisão da bola com as paredes superior e inferior;
- Sistema de pontuação para os dois jogadores;
- Reinício da bola após cada ponto;
- Definição de uma pontuação máxima para terminar a partida;



## 🛠️ Tecnologias utilizadas

- Python 3.13.12
- Turtle (biblioteca padrão do Python)
- Git version 2.53.0.windows.1
- Github

## 📁 Estrutura do projeto

```text
snackgame/ 
├── main.py          # Arquivo principal do jogo 
├── paddle.py         # Lógica e comportamento das raquetes
├── ball.py          # Lógica e movimento da bola 
├── scoreboard.py    # Sistema de pontuação 
├── sideSeparator.py    # Separador de ecrã 
├── validationFunctions.py    # Funcões de validação
├── LICENSE 
└── README.md

```

## 🚀 Como executar

1. Clone este repositório:
   ```bash
   git clone https://github.com/Jaimepelembe/ponggame.git
   ```
2. Entre na pasta do projeto:
   ```bash
   cd ponggame
   ```
3. Execute o jogo:
   ```bash
   python main.py
   ```

## 🎮 Como jogar

- Execute o jogo.
- O jogador 1 controla a raquete localizada no lado esquerdo.
- O jogador 2 controla a raquete localizada no lado direito.
- A bola começa a movimentar-se automaticamente.
- Utilize as teclas de controlo para mover a sua raquete para cima ou para baixo.
- Tente rebater a bola antes que ela ultrapasse a sua raquete.
- Quando um jogador não consegue rebater a bola, o adversário ganha um ponto.
- A bola é reposicionada e uma nova jogada começa.
- A pontuação dos jogadores é atualizada após cada ponto.

- O jogo termina quando um dos jogadores atinge a pontuação máxima definida.

- O jogador que alcançar essa pontuação primeiro é declarado vencedor e uma mensagem de vitória é apresentada no ecrã.


## Controlos
|Jogador| Tecla | Acção |
|------|-------|-------|
|Jogador 1| W  | Mover para cima   |
|Jogador 1| S  | Mover para baixo  |
|Jogador 2| ↑  | Mover para cima   |
|Jogador 2| ↓  | Mover para baixo  |



## 👤 Autor

Desenvolvido por **Jaime Fernando**

- GitHub: [@jaimepelembe](https://github.com/jaimepelembe)

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE.txt) para mais detalhes.