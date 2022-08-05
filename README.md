# Game-Of-Life
A pygame visualisation of the Game of Life by John Conway

Conway's Game of Life is a 0 player game consisting of a grid of cells and a set of rules that governs the cells.
Rules:
- Any live cell with fewer than two live neighbours dies, as if by underpopulation.
- Any live cell with two or three live neighbours lives on to the next generation.
- Any live cell with more than three live neighbours dies, as if by overpopulation.
- Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

These rules can then be condensed into the following:
- Any live cell with two or three live neighbours survives.
- Any dead cell with three live neighbours becomes a live cell.
- All other live cells die in the next generation. Similarly, all other dead cells stay dead.

Lastly, after establishing the rules, you can choose a starting generation of live cells in a particular pattern
then observe the changes over generations caused by the rules.
