% Facts: parent(Parent, Child), male(Person), female(Person)
parent(john, mary).
parent(john, michael).
parent(susan, mary).
parent(susan, michael).
parent(mary, james).
parent(mary, lisa).
parent(michael, andrew).
parent(michael, sophia).

male(john).
male(michael).
male(james).
male(andrew).

female(susan).
female(mary).
female(lisa).
female(sophia).

% Rule: child(Child, Parent)
child(X, Y) :-
    parent(Y, X),
    format('~w is a child of ~w.~n', [X, Y]).

% Rule: sibling(X, Y) - X and Y are siblings if they share at least one parent
sibling(X, Y) :-
    parent(Z, X),
    parent(Z, Y),
    X \= Y,
    format('~w and ~w are siblings.~n', [X, Y]).

% Rule: father(Father, Child) - A father is a male parent
father(Father, Child) :-
    parent(Father, Child),
    male(Father),
    format('~w is the father of ~w.~n', [Father, Child]).

% Rule: mother(Mother, Child) - A mother is a female parent
mother(Mother, Child) :-
    parent(Mother, Child),
    female(Mother),
    format('~w is the mother of ~w.~n', [Mother, Child]).

% Rule: grandparent(Grandparent, Grandchild)
grandparent(Grandparent, Grandchild) :-
    parent(Grandparent, Parent),
    parent(Parent, Grandchild),
    format('~w is the grandparent of ~w.~n', [Grandparent, Grandchild]).

% Rule: grandfather(Grandfather, Grandchild) - A grandfather is a male grandparent
grandfather(Grandfather, Grandchild) :-
    grandparent(Grandfather, Grandchild),
    male(Grandfather),
    format('~w is the grandfather of ~w.~n', [Grandfather, Grandchild]).

% Rule: grandmother(Grandmother, Grandchild) - A grandmother is a female grandparent
grandmother(Grandmother, Grandchild) :-
    grandparent(Grandmother, Grandchild),
    female(Grandmother),
    format('~w is the grandmother of ~w.~n', [Grandmother, Grandchild]).

% Rule: aunt(Aunt, NieceOrNephew) - An aunt is a female sibling of a parent
aunt(Aunt, NieceOrNephew) :-
    sibling(Aunt, Parent),
    parent(Parent, NieceOrNephew),
    female(Aunt),
    format('~w is the aunt of ~w.~n', [Aunt, NieceOrNephew]).

% Rule: uncle(Uncle, NieceOrNephew) - An uncle is a male sibling of a parent
uncle(Uncle, NieceOrNephew) :-
    sibling(Uncle, Parent),
    parent(Parent, NieceOrNephew),
    male(Uncle),
    format('~w is the uncle of ~w.~n', [Uncle, NieceOrNephew]).

% Rule: cousin(X, Y) - X and Y are cousins if their parents are siblings
cousin(X, Y) :-
    parent(A, X),
    parent(B, Y),
    sibling(A, B),
    format('~w and ~w are cousins.~n', [X, Y]).

% Rule: ancestor(Ancestor, Descendant)
ancestor(Ancestor, Descendant) :-
    parent(Ancestor, Descendant),
    format('~w is an ancestor of ~w.~n', [Ancestor, Descendant]).

ancestor(Ancestor, Descendant) :-
    parent(Ancestor, Intermediate),
    ancestor(Intermediate, Descendant),
    format('~w is an ancestor of ~w.~n', [Ancestor, Descendant]).

% Rule: descendant(Descendant, Ancestor)
descendant(Descendant, Ancestor) :-
    ancestor(Ancestor, Descendant),
    format('~w is a descendant of ~w.~n', [Descendant, Ancestor]).
