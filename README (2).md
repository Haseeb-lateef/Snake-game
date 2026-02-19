# 🐍 Snake Game

A classic Snake game built with Python's Turtle graphics library. Control the snake, eat food, and try to achieve the highest score without hitting the walls or yourself!

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Turtle](https://img.shields.io/badge/Library-Turtle-green.svg)

## 📖 About

This is a classic implementation of the Snake game where you control a snake that grows longer as it eats food. The game features:
- Smooth snake movement and controls
- Score tracking with high score persistence
- Auto-reset functionality when colliding with walls or yourself
- Clean, minimal UI with a black background

## ✨ Features

- **Classic Gameplay**: Navigate the snake using arrow keys
- **Dynamic Growth**: Snake expands each time it eats food
- **Collision Detection**: 
  - Wall collision detection
  - Self-collision detection
- **Score System**:
  - Current score display
  - High score tracking across game sessions
- **Auto-Reset**: Game automatically resets on collision while preserving high score

## 🎮 How to Play

1. Use the **arrow keys** to control the snake:
   - ⬆️ **Up Arrow**: Move up
   - ⬇️ **Down Arrow**: Move down
   - ⬅️ **Left Arrow**: Move left
   - ➡️ **Right Arrow**: Move right

2. Eat the food (appears as a dot on screen) to grow and increase your score

3. Avoid:
   - Hitting the walls
   - Colliding with your own body

4. Try to beat your high score!

## 🚀 Installation

### Prerequisites
- Python 3.x installed on your system
- Turtle graphics library (comes pre-installed with Python)

### Setup

1. Clone this repository:
```bash
git clone https://github.com/Haseeb-lateef/Snake-game.git
```

2. Navigate to the project directory:
```bash
cd Snake-game
```

3. Run the game:
```bash
python main.py
```

## 📂 Project Structure

```
Snake-game/
│
├── main.py          # Main game loop and screen setup
├── snake.py         # Snake class with movement and collision logic
├── score.py         # Scoreboard class for score tracking
└── food.py          # Food class for random food placement
```

## 🛠️ Technical Details

### Classes

**Snake** (`snake.py`)
- Manages snake creation, movement, and expansion
- Handles directional controls (up, down, left, right)
- Implements collision detection with self
- Reset functionality to restart the game

**Scoreboard** (`score.py`)
- Displays current score and high score
- Updates score when food is consumed
- Tracks and maintains high score across game resets

**Food** (`food.py`)
- Manages food placement on the screen
- Randomizes food position when consumed

### Game Configuration
- **Screen Size**: 600x600 pixels
- **Background**: Black
- **Snake Color**: White
- **Starting Size**: 3 segments
- **Movement Speed**: 0.1 seconds per update

## 🎯 Game Mechanics

- The snake moves continuously in the current direction
- You cannot reverse direction directly (e.g., can't go left if moving right)
- Food spawns at random locations after being eaten
- Score increases by 1 for each food item consumed
- Game resets when snake hits a wall or itself, but high score is preserved

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/Haseeb-lateef/Snake-game/issues).

## 📝 License

This project is open source and available for personal and educational use.

## 👤 Author

**Haseeb Lateef**
- GitHub: [@Haseeb-lateef](https://github.com/Haseeb-lateef)

## 🎉 Acknowledgments

- Built with Python's Turtle graphics library
- Inspired by the classic Nokia Snake game

---

*Enjoy the game and happy coding!* 🐍✨