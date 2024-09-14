% Facts representing diseases and their dietary restrictions
% disease(Disease, DietSuggestion)

disease(diabetes, 'Low sugar and carbohydrate diet').
disease(hypertension, 'Low sodium diet').
disease(celiac, 'Gluten-free diet').
disease(allergy, 'Avoid allergens specific to the individual').
disease(heart_disease, 'Low saturated fat and cholesterol diet').

% Rule to suggest a diet based on the disease
suggest_diet(Disease, DietSuggestion) :-
    disease(Disease, DietSuggestion).

% Example queries
% To get diet suggestions based on diseases
% ?- suggest_diet(diabetes, Diet).
% Diet = 'Low sugar and carbohydrate diet'.

% ?- suggest_diet(celiac, Diet).
% Diet = 'Gluten-free diet'.
