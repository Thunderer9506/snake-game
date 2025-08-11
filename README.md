# Snake Game

A classic Snake game implemented in Python using the `turtle` graphics library.  
The game features smooth movement, randomized food placement, and a persistent high score saved between sessions.

---

## How It Works

### **Game Setup**
- The game runs from `main.py`.
- A `turtle.Screen` is set to a 600×600 black background.
- The snake (`Snake` class), food (`Food` class), and scoreboard (`scoreboard` class) are initialized.
- The game listens for arrow key presses to control the snake’s direction.

---

### **Snake (`snake.py`)**
- The snake is made up of square segments starting at fixed positions.
- Movement works by each segment moving to the position of the one in front, while the head moves forward.
- The snake grows by adding a new segment at its tail position.
- The snake can be reset (for collisions) by moving all segments off-screen and recreating it.

---

### **Food (`Food.py`)**
- Food is represented as a small blue circle placed randomly within the game area.
- When eaten by the snake, the `refresh()` method generates a new random location for the next piece of food.

---

### **Scoreboard (`score_board.py`)**
- Displays the current score and the highest score achieved (high score is stored in `data.txt`).
- Each time the snake eats food, the score increases by 1.
- On game reset, if the current score beats the high score, the new high score is saved.

---

### **Main Game Loop**
1. The screen updates every 0.1 seconds to simulate movement.
2. The snake moves in the set direction.
3. If the snake’s head collides with food:
   - The snake grows longer.
   - The score increases.
   - New food is placed randomly.
4. If the snake’s head collides with:
   - A wall → game resets.
   - Its own body → game resets.
5. High scores are preserved between games.

---

## **Project Structure**
```
snake-game/
│
├── main.py          # Main game loop and controls
├── snake.py         # Snake creation, movement, and growth
├── Food.py          # Food generation and placement
├── score_board.py   # Score tracking and display
├── data.txt         # Stores persistent high score
└── README.md        # Project overview and explanation
```

---

## **Controls**
- **Arrow Keys**: Move the snake **Up**, **Down**, **Left**, or **Right**
