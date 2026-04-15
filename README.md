# AI-PATH-PLANNING
Path planning is a crucial component of autonomous systems, enabling agents to navigate
from a starting point to a target while avoiding collisions. This project gamifies the
concept by creating a pet simulation game where a player controls movement. Although
controlled manually, the framework reflects how AI systems handle navigation
challenges such as:
● Obstacle detection.
● Safe path traversal.
● Multi-goal achievement.
● Level progression with increasing complexity.
The game allows players to understand AI’s role in path planning through an engaging,
visual medium.
Implementation:
● Obstacle spawning ensures no overlap with each other or player’s start area.
● Goals placement avoids overlap with obstacles.
● The movement system is grid-free, giving smooth real-time control.
● Collision handling uses Pygame’s Rect class.
● Difficulty scaling: Each level spawns more obstacles and goals.
 Workflow of given project:
➢ Initialization: Create window, load fonts, set variables.
➢ Spawning: Randomly place obstacles and goals on the map without overlaps
➢ Player Movement: Control pet 🐶 with arrow keys.
➢ Collision Detection:
1. With goals 🍖 → Increase score.
2. With obstacles → End game.
➢ Level Progression: Once all goals are collected, spawn new obstacles and goals
with higher difficulty.
➢ Display: Score, level, and messages (Game Over, Level Complete).
Tools and Technologies used:
● Programming Language: Python 3
● Library: Pygame (for graphics, event handling, and game mechanics)
● IDE/Editor: Any Python-supported IDE (e.g., PyCharm, VS Code, IDLE)
● Platform: Desktop (Windows/Linux/Mac)
Conclusion:
The Pet Path Planner demonstrates essential AI principles of navigation, obstacle
avoidance, and progressive difficulty. It serves as both an educational and recreational
project, helping learners visualize how autonomous systems manage dynamic
environments. The simplicity of design also makes it an excellent foundation for future
enhancements such as automated movement, smarter enemies, or pathfinding algorithms
like BFS, DFS, or A*.
DEMO:
<img width="563" height="407" alt="image" src="https://github.com/user-attachments/assets/8cbd6267-e2ce-4383-ad55-42ca3cf57523" />
