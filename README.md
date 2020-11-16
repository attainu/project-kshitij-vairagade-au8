Snake & Ladder Application using Python:

Rules:-
1. The board will have 100 cells numbered from 1 to 100.
2. The game will have a six sided dice numbered from 1 to 6 and will always give a random number on rolling it.
3. Each player has a piece which is initially kept outside the board (i.e., at position 0).
4. Each player rolls the dice when their turn comes.
5. Based on the dice value, the player moves their piece forward that number of cells. Ex: If the dice value is 5 and the piece is at position 21, the player will put their piece at position 26 now (21+5).
6. A player wins if it exactly reaches the position 100 and the game ends there.
7. After the dice roll, if a piece is supposed to move outside position 100, it does not move.
8. The board also contains some snakes and ladders.
9. Each snake will have its head at some number and its tail at a smaller number.
10. Whenever a piece ends up at a position with the head of the snake, the piece should go down to the position of the tail of that snake.
11. Each ladder will have its start position at some number and end position at a larger number.
12. Whenever a piece ends up at a position with the start of the ladder, the piece should go up to the position of the end of that ladder.
13. There could be another snake/ladder at the tail of the snake or the end position of the ladder and the piece should go up/down accordingly.


Entities used:
1. Players
2. Snake
3. Ladder
4. Snake And LadderBoard

Working of Application:
1. Welcome Message Display
2. Input the player names
3. Collect their names
4. Working of app until one player is winning do the following steps :-
     a. Roll the dice
     b. Move the player forward as the the dice roll has diplayed the value
     c. If the player is stopping on any snake's head on the board it will go down directly to snale's tail on whichever number it's tail is present.
     d. If the player is stopping on any ladder's bottom on the board it will directly go up to it's top. 
     e. If no such dice roll comes continue to play the game till it's over.
  5. Thank you message

The project is solely created using Python programming language