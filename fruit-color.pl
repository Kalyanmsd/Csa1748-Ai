% Define facts: fruit(Fruit, Color)
fruit(apple, red).
fruit(banana, yellow).
fruit(grape, purple).
fruit(orange, orange).
fruit(strawberry, red).
fruit(blueberry, blue).
fruit(lemon, yellow).
fruit(watermelon, green).

% Rule to find the color of a given fruit
find_color(Fruit, Color) :-
    fruit(Fruit, Color).

% Rule to find all fruits of a given color
find_fruits_by_color(Color, Fruit) :-
    fruit(Fruit, Color).

% Example Queries:

% To find the color of a specific fruit
% ?- find_color(apple, Color).
% Color = red.

% To find all fruits of a specific color
% ?- find_fruits_by_color(yellow, Fruit).
% Fruit = banana ;
% Fruit = lemon.
