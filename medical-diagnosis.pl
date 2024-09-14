% Define diseases and their corresponding symptoms
disease(cold) :-
    has_symptom(cough),
    has_symptom(sneezing),
    has_symptom(fever).

disease(flu) :-
    has_symptom(fever),
    has_symptom(headache),
    has_symptom(body_ache).

disease(covid19) :-
    has_symptom(fever),
    has_symptom(cough),
    has_symptom(loss_of_taste_or_smell),
    has_symptom(difficulty_breathing).

disease(allergy) :-
    has_symptom(sneezing),
    has_symptom(runny_nose),
    has_symptom(itchy_eyes).

disease(malaria) :-
    has_symptom(fever),
    has_symptom(shivering),
    has_symptom(sweating),
    has_symptom(fatigue).

% Interact with user to ask for symptoms
ask_symptom(Symptom) :-
    format('Do you have ~w? (yes/no) ', [Symptom]),
    read(Reply),
    (Reply == yes -> assert(has_symptom(Symptom)) ; true).

% Start the diagnosis process
diagnose :-
    retractall(has_symptom(_)),  % Clear any previous symptoms
    write('Let\'s diagnose your illness!'), nl,
    ask_symptom(fever),
    ask_symptom(cough),
    ask_symptom(sneezing),
    ask_symptom(headache),
    ask_symptom(body_ache),
    ask_symptom(loss_of_taste_or_smell),
    ask_symptom(difficulty_breathing),
    ask_symptom(runny_nose),
    ask_symptom(itchy_eyes),
    ask_symptom(shivering),
    ask_symptom(sweating),
    ask_symptom(fatigue),
    (disease(Disease) -> format('You may have ~w.', [Disease]), nl;
     write('Sorry, I could not diagnose your illness.'), nl).

% To start the diagnosis, query:
% ?- diagnose.

