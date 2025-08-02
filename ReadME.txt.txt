Rubik’s Cube Solver 
===================
Author: [S PRAVEEN KUMAR SWAMY]

-------------------------------------------------
Overview
-------------------------------------------------
This project is a visual Rubik's Cube solver built using Python.
It scrambles a standard 3x3 cube, solves it using a depth-limited DFS algorithm, 
and animates the solving process using a GUI built with Tkinter.

-------------------------------------------------
Requirements
-------------------------------------------------
• Python 3.8 or higher (Tested on Python 3.13)
• Tkinter (usually included with Python installations)

To check if Tkinter is installed:
Run this command in your terminal or command prompt:
    python -m tkinter

If a small window opens with “Click Me” and “Quit” buttons, Tkinter is available.

-------------------------------------------------
How to Run
-------------------------------------------------
1. Open a terminal in the project directory.
2. Run the Python script:

    python rubiks_solver_gui.py

3. A window will open:
    • It will scramble the cube using 4 moves.
    • The GUI will animate each move in the solution.

You can modify the number of scramble moves or solving depth (optional, see below).

-------------------------------------------------
Optional Customizations
-------------------------------------------------
Inside the code (`rubiks_solver_gui.py`):

1. Adjust Scramble Difficulty:
   - Line: `scramble_seq = scramble(cube, moves=4)`
   - Increase `moves` to scramble more deeply.

2. Adjust Solving Power (search depth):
   - Line: `MAX_DEPTH = 8`
   - Increase to 10+ to allow solving more complex scrambles.

NOTE: Increasing both `moves` and `MAX_DEPTH` will increase runtime.

-------------------------------------------------
Files Included in this Submission
-------------------------------------------------
• rubiks_solver_gui.py        → The main Python script
• Design_Dexterity_Slides.pptx → Filled template describing the approach
• README.txt                  → This instruction file
• screenshots/                → (Optional) Images of GUI and outputs

-------------------------------------------------
Key Skills Demonstrated
-------------------------------------------------
✓ Algorithm design (DFS + pruning)
✓ OOP in Python
✓ GUI animation using Tkinter
✓ State modeling of a complex system
✓ Clean and modular code

