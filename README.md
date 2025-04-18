🐍 Snake Game with Shivam
A classic Snake Game built using Pygame — enriched with colorful graphics, fun backgrounds, sound effects, and a scoring system with high score tracking!

🎮 Gameplay Overview
You control the snake using arrow keys.

Eat the red square (food) to grow your snake and earn points.

Avoid running into the walls or yourself — or it's game over!

Background music plays during the game, and a beep plays on game over.

High score is saved and displayed.

🕹️ Controls

Key	Action
→	Move Right
←	Move Left
↑	Move Up
↓	Move Down
M	Cheat: Add +10 Score
G	Cheat: Subtract -10
Enter	Restart after Game Over
Space	Start the game from welcome screen

🧠 Features

🎨 Backgrounds for game, welcome screen, and game over screen

🎵 Sound effects and background music

🏆 Score and High Score display (saved to a text file)

💡 Cheat codes for testing or fun

🐍 Smooth movement and growth logic

🗂️ Folder Structure
bash
Copy
Edit
snake_game/
├── snake_game.py
├── snake7.jpg            # Welcome background
├── snake8.jpg            # Game background
├── 10.JPG                # Game over background
├── back.mp3              # Background music
├── beep.mp3              # Game over sound
└── high_score.txt        # Auto-created to store high score
🚀 How to Run
Install Pygame (if you haven’t):

bash
Copy
Edit
pip install pygame
Run the game:

python snake_game.py
Make sure all images and sound files are in the same directory as the Python file.

🧩 Future Ideas
Add main menu and pause functionality

Implement difficulty levels (increase speed over time)

Multiplayer support

Track and display total playtime

GUI high score board

📄 License
This project is created for fun and learning purposes. You’re free to modify, enhance, and share it! Credit is appreciated but not required.
