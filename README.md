# tttAI
building a TicTacToe AI, then morphing it into a Connect4 AI

### Running
Run `python ttt.py` at the command line. This is tested on Python 3.7.2.

### Basics and Input
This will create a Command Line tic-tac-toe game. THe human plays 'X' and inputs moves as coordinates, i.e. `0, 0` or `1, 2`. The board is a grid (0, 2) x (0, 2). When entering moves, spaces can be added between the coordinates and the comma, but they need to be comma separated.

### Future plans
Allow the user to select if the AI is 'X' or 'O', and then whoever is 'X' goes first.

Since TicTacToe is a pretty simple game, there is no AB pruning. When I build this into a Connect4 AI, I'll implement AB Pruning to increase the AI speed.
