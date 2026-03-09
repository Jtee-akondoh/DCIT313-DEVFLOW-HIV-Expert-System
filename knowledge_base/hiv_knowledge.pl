% HIV/AIDS Expert System Knowledge Base
% Facts and Rules for HIV/AIDS information and risk assessment

% ============================================
% BASIC FACTS ABOUT HIV/AIDS
% ============================================

% Transmission methods
transmission_method(unprotected_sex).
transmission_method(shared_needles).
transmission_method(blood_transfusion).
transmission_method(mother_to_child).
transmission_method(contact_with_infected_blood).

% Prevention methods
prevention_method(use_condoms).
prevention_method(use_sterile_needles).
prevention_method(testing_blood_products).
prevention_method(prep_medication).
prevention_method(pep_after_exposure).

% Symptoms (early stage)
early_symptom(fever).
early_symptom(headache).
early_symptom(fatigue).
early_symptom(swollen_lymph_nodes).
early_symptom(sore_throat).
early_symptom(rash).

% Symptoms (late stage)
late_symptom(rapid_weight_loss).
late_symptom(recurring_fever).
late_symptom(night_sweats).
late_symptom(extreme_fatigue).
late_symptom(prolonged_swelling_lymph_nodes).
late_symptom(diarrhea_more_than_week).
late_symptom(sores_mouth_anus_genitals).
late_symptom(pneumonia).
late_symptom(memory_loss).

% ============================================
% RISK ASSESSMENT RULES
% ============================================

% Rule: High risk if engaged in unprotected sex with multiple partners
risk_level(high) :-
    has_risk_factor(unprotected_sex),
    has_risk_factor(multiple_partners).

% Rule: High risk if shared needles
risk_level(high) :-
    has_risk_factor(shared_needles).

% Rule: Medium risk if unprotected sex with one partner whose status unknown
risk_level(medium) :-
    has_risk_factor(unprotected_sex),
    not(has_risk_factor(multiple_partners)),
    not(has_risk_factor(knows_partner_status)).

% Rule: Medium risk if had blood transfusion before 1985
risk_level(medium) :-
    has_risk_factor(blood_transfusion_before_1985).

% Rule: Low risk if always uses protection and no other risk factors
risk_level(low) :-
    has_risk_factor(uses_protection),
    not(has_risk_factor(shared_needles)),
    not(has_risk_factor(blood_transfusion_before_1985)).

% Default risk level if no specific rules apply
risk_level(unknown) :-
    not(has_risk_factor(_)).

% ============================================
% SYMPTOM-BASED ADVICE RULES
% ============================================

% Rule: Suggest testing if multiple early symptoms present
suggest_testing :-
    count_early_symptoms(Count),
    Count >= 3.

% Rule: Suggest immediate medical attention if late symptoms present
suggest_medical_attention :-
    has_late_symptom(_).

% Rule: Provide general information based on user query
provide_information(transmission, Info) :-
    Info = 'HIV can be transmitted through: 
    - Unprotected sexual contact
    - Sharing needles or syringes
    - From mother to child during pregnancy, birth, or breastfeeding
    - Blood transfusions with infected blood (rare now due to screening)'.

provide_information(prevention, Info) :-
    Info = 'Ways to prevent HIV:
    - Use condoms correctly every time you have sex
    - Don\'t share needles or syringes
    - Take PrEP if you\'re at high risk
    - Get tested regularly
    - If exposed, get PEP within 72 hours'.

provide_information(symptoms, Info) :-
    Info = 'Early symptoms (2-4 weeks after exposure):
    - Fever, headache, fatigue
    - Swollen lymph nodes, sore throat
    - Rash
    
    Later symptoms (years after infection):
    - Rapid weight loss, recurring fever
    - Night sweats, extreme fatigue
    - Prolonged swelling of lymph nodes
    - Diarrhea, pneumonia, memory loss'.

provide_information(treatment, Info) :-
    Info = 'HIV treatment (ART - Antiretroviral Therapy):
    - Helps people with HIV live long, healthy lives
    - Reduces viral load to undetectable levels
    - Prevents transmission to others (U=U: Undetectable = Untransmittable)
    - Requires daily medication as prescribed'.

provide_information(Testing, Info) :-
    Info = 'HIV testing options:
    - Rapid tests (results in 20-30 minutes)
    - Laboratory tests (results in few days)
    - Home testing kits
    - Anonymous testing available at many clinics
    - Window period: 2-4 weeks to 3 months'.

% ============================================
% HELPER PREDICATES
% ============================================

% Count early symptoms
count_early_symptoms(Count) :-
    findall(S, early_symptom(S), Symptoms),
    count_matching_symptoms(Symptoms, Count).

% Count matching symptoms
count_matching_symptoms([], 0).
count_matching_symptoms([S|Rest], Count) :-
    (has_symptom(S) ->
        count_matching_symptoms(Rest, RestCount),
        Count is RestCount + 1
    ;
        count_matching_symptoms(Rest, Count)
    ).

% Check if user has late symptoms
has_late_symptom(Symptom) :-
    late_symptom(Symptom),
    user_symptom(Symptom).

% Dynamic predicates for user inputs
:- dynamic has_risk_factor/1.
:- dynamic user_symptom/1.
:- dynamic knows_partner_status/0.
:- dynamic uses_protection/0.