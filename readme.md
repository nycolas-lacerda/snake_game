# 🐍 Snake Game

Um clássico **Jogo da Cobrinha (Snake)** desenvolvido em **Python** utilizando a biblioteca **Pygame**.  
O projeto foi criado para fins acadêmicos, mas também como prática de programação orientada a objetos, organização de pastas e boas práticas em jogos 2D.

---

## 🎮 Funcionalidades

- Movimento da cobrinha em todas as direções.  
- Sistema de pontuação com **HighScore salvo em arquivos** (separados por dificuldade).  
- Duas dificuldades de jogo:
  - **Normal:** colisão apenas com o corpo da cobra (bordas têm teletransporte).  
  - **Difícil:** colisão com corpo **e com as bordas** (game over ao bater).  
- Comida gerada aleatoriamente no campo de jogo.  
- Crescimento da cobra a cada comida ingerida.  
- **Música de fundo** + efeitos sonoros (comer, movimento e game over).  
- Menu inicial com seleção de dificuldade e opção de sair.  

---

## 🖥️ Tecnologias Utilizadas

- [Python 3.x](https://www.python.org/)  
- [Pygame](https://www.pygame.org/news)  

---

## 📂 Estrutura de Pastas
```
project/
│
├── assets/ # Arquivos de mídia (músicas e sons)
│ ├── background.mp3
│ ├── eat.wav
│ ├── gameover.wav
│ └── move.wav
│
├── scores/ # Highscores separados por dificuldade
│ ├── normal.txt
│ └── hard.txt
│
├── classes/ # Classes do jogo
│ ├── food.py
│ ├── game.py
│ ├── highscore.py
│ ├── menu.py
│ ├── scoreboard.py
│ ├── snake.py
│ └── sound_manager.py
│
├── main.py # Ponto de entrada (menu principal)
├── README.md
└── settings.py # Configurações globais
```

---

## 🚀 Como Rodar o Jogo

### 1. Clone o repositório
```bash
git clone https://github.com/seu-usuario/snake-game.git
cd snake-game
```

### 2. Crie um ambiente virtual (opcional, mas recomendado) 
```bash 
python -m venv venv
```

Ative o ambiente:

- Windows: venv\\Scripts\\activate
- Linux/Mac: source venv/bin/activate

### 3. Instale as depêndencias
```bash 
pip install pygame
```

### 4. Rode o jogo
```bash
python main.py
```

🕹️ Controles

Setas do Teclado (↑ ↓ ← →): movimentar a cobrinha

Enter: selecionar opção no menu

Esc: voltar ao menu / sair

## 📊 Dificuldades

- ### Normal:
    - A cobra pode atravessar as bordas (teletransporte).
    - Game over apenas ao colidir com o próprio corpo.

- ### Difícil:
    - A cobra morre ao colidir com o próprio corpo ou com as bordas.
    - Jogo mais desafiador 🔥.

## 📜 Licença

Este projeto é de uso acadêmico e livre para estudo.