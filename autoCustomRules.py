import skfuzzy.control as ctrl
import skfuzzy as fuzzy
import numpy as np


universe_features = np.arange(0,1,0.001)
universe_result = np.arange(0,1,0.01)

title_word = ctrl.Antecedent(universe_features, 'title_word')
sentence_length = ctrl.Antecedent(universe_features, 'sentence_length')
sentence_location = ctrl.Antecedent(universe_features, 'sentence_location')
numerical_data = ctrl.Antecedent(universe_features, 'numerical_data')
thematic_keyword = ctrl.Antecedent(universe_features, 'thematic_keyword')
proper_noun = ctrl.Antecedent(universe_features, 'proper_noun')
sentence_similarity = ctrl.Antecedent(universe_features, 'sentence_similarity')
term_weight = ctrl.Antecedent(universe_features, 'term_weight')


result = ctrl.Consequent(universe_result, 'result')


# Auto-membership function population is possible with .automf(3, 5, or 7)
title_word.automf(3)
sentence_length.automf(3)
sentence_location.automf(3)
numerical_data.automf(3)
thematic_keyword.automf(3)
proper_noun.automf(3)
sentence_similarity.automf(3)
term_weight.automf(3)

# Custom membership functions can be built interactively with a familiar,
# Pythonic API
result['low'] = fuzzy.trimf(result.universe, [0.000,0.30,0.500])
result['medium'] = fuzzy.trimf(result.universe, [0.300,0.500,0.700])
result['high'] = fuzzy.trimf(result.universe, [0.500,1.0,1.0])

def test():
    return "ok"

def customRule():

    
    rule1  = ctrl.Rule(title_word["poor"] & sentence_length["poor"] & sentence_location["poor"] & numerical_data["poor"] & thematic_keyword["poor"] & proper_noun["poor"] & sentence_similarity["poor"] & term_weight["poor"], result['low'])
    rule2  = ctrl.Rule(title_word["poor"] & sentence_length["poor"] & sentence_location["poor"] & numerical_data["poor"] & thematic_keyword["poor"] & proper_noun["poor"] & sentence_similarity["poor"] & term_weight["average"], result['low'])
    rule3  = ctrl.Rule(title_word["poor"] & sentence_length["poor"] & sentence_location["poor"] & numerical_data["poor"] & thematic_keyword["poor"] & proper_noun["poor"] & sentence_similarity["poor"] & term_weight["good"], result['low'])
    rule4  = ctrl.Rule(title_word["poor"] & sentence_length["poor"] & sentence_location["poor"] & numerical_data["poor"] & thematic_keyword["poor"] & proper_noun["poor"] & sentence_similarity["average"] & term_weight["poor"], result['low'])
    rule5  = ctrl.Rule(title_word["poor"] & sentence_length["poor"] & sentence_location["poor"] & numerical_data["poor"] & thematic_keyword["poor"] & proper_noun["poor"] & sentence_similarity["average"] & term_weight["average"], result['low'])
    rule6  = ctrl.Rule(title_word["poor"] & sentence_length["poor"] & sentence_location["poor"] & numerical_data["poor"] & thematic_keyword["poor"] & proper_noun["poor"] & sentence_similarity["average"] & term_weight["good"], result['low'])
    rule7  = ctrl.Rule(title_word["poor"] & sentence_length["poor"] & sentence_location["poor"] & numerical_data["poor"] & thematic_keyword["poor"] & proper_noun["poor"] & sentence_similarity["good"] & term_weight["poor"], result['low'])
    rule8  = ctrl.Rule(title_word["poor"] & sentence_length["poor"] & sentence_location["poor"] & numerical_data["poor"] & thematic_keyword["poor"] & proper_noun["poor"] & sentence_similarity["good"] & term_weight["average"], result['low'])
    rule9  = ctrl.Rule(title_word["poor"] & sentence_length["poor"] & sentence_location["poor"] & numerical_data["poor"] & thematic_keyword["poor"] & proper_noun["poor"] & sentence_similarity["good"] & term_weight["good"], result['low'])
    rule10  = ctrl.Rule(title_word["poor"] & sentence_length["poor"] & sentence_location["poor"] & numerical_data["poor"] & thematic_keyword["poor"] & proper_noun["average"] & sentence_similarity["poor"] & term_weight["poor"], result['low'])
    rule11  = ctrl.Rule(title_word["poor"] & sentence_length["poor"] & sentence_location["poor"] & numerical_data["poor"] & thematic_keyword["poor"] & proper_noun["average"] & sentence_similarity["poor"] & term_weight["average"], result['low'])
    rule12  = ctrl.Rule(title_word["poor"] & sentence_length["poor"] & sentence_location["poor"] & numerical_data["poor"] & thematic_keyword["poor"] & proper_noun["average"] & sentence_similarity["poor"] & term_weight["good"], result['low'])
    rule13  = ctrl.Rule(title_word["poor"] & sentence_length["poor"] & sentence_location["poor"] & numerical_data["poor"] & thematic_keyword["poor"] & proper_noun["average"] & sentence_similarity["average"] & term_weight["poor"], result['low'])
    rule14  = ctrl.Rule(title_word["poor"] & sentence_length["poor"] & sentence_location["poor"] & numerical_data["poor"] & thematic_keyword["poor"] & proper_noun["average"] & sentence_similarity["average"] & term_weight["average"], result['low'])
    rule15  = ctrl.Rule(title_word["poor"] & sentence_length["poor"] & sentence_location["poor"] & numerical_data["poor"] & thematic_keyword["poor"] & proper_noun["average"] & sentence_similarity["average"] & term_weight["good"], result['low'])
    rule16  = ctrl.Rule(title_word["poor"] & sentence_length["poor"] & sentence_location["poor"] & numerical_data["poor"] & thematic_keyword["poor"] & proper_noun["average"] & sentence_similarity["good"] & term_weight["poor"], result['low'])
    rule17  = ctrl.Rule(title_word["poor"] & sentence_length["poor"] & sentence_location["poor"] & numerical_data["poor"] & thematic_keyword["poor"] & proper_noun["average"] & sentence_similarity["good"] & term_weight["average"], result['low'])
    rule18  = ctrl.Rule(title_word["poor"] & sentence_length["poor"] & sentence_location["poor"] & numerical_data["poor"] & thematic_keyword["poor"] & proper_noun["average"] & sentence_similarity["good"] & term_weight["good"], result['low'])
    rule19  = ctrl.Rule(title_word["poor"] & sentence_length["poor"] & sentence_location["poor"] & numerical_data["poor"] & thematic_keyword["poor"] & proper_noun["good"] & sentence_similarity["poor"] & term_weight["poor"], result['low'])
    rule20  = ctrl.Rule(title_word["poor"] & sentence_length["poor"] & sentence_location["poor"] & numerical_data["poor"] & thematic_keyword["poor"] & proper_noun["good"] & sentence_similarity["poor"] & term_weight["average"], result['low'])
    rule21  = ctrl.Rule(title_word["poor"] & sentence_length["poor"] & sentence_location["poor"] & numerical_data["poor"] & thematic_keyword["poor"] & proper_noun["good"] & sentence_similarity["poor"] & term_weight["good"], result['low'])
    rule22  = ctrl.Rule(title_word["poor"] & sentence_length["poor"] & sentence_location["poor"] & numerical_data["poor"] & thematic_keyword["poor"] & proper_noun["good"] & sentence_similarity["average"] & term_weight["poor"], result['low'])
    rule23  = ctrl.Rule(title_word["poor"] & sentence_length["poor"] & sentence_location["poor"] & numerical_data["poor"] & thematic_keyword["poor"] & proper_noun["good"] & sentence_similarity["average"] & term_weight["average"], result['low'])
    rule24  = ctrl.Rule(title_word["poor"] & sentence_length["poor"] & sentence_location["poor"] & numerical_data["poor"] & thematic_keyword["poor"] & proper_noun["good"] & sentence_similarity["average"] & term_weight["good"], result['low'])
    rule25  = ctrl.Rule(title_word["poor"] & sentence_length["poor"] & sentence_location["poor"] & numerical_data["poor"] & thematic_keyword["poor"] & proper_noun["good"] & sentence_similarity["good"] & term_weight["poor"], result['low'])
    rule26  = ctrl.Rule(title_word["poor"] & sentence_length["poor"] & sentence_location["poor"] & numerical_data["poor"] & thematic_keyword["poor"] & proper_noun["good"] & sentence_similarity["good"] & term_weight["average"], result['low'])
    rule27  = ctrl.Rule(title_word["poor"] & sentence_length["poor"] & sentence_location["poor"] & numerical_data["poor"] & thematic_keyword["poor"] & proper_noun["good"] & sentence_similarity["good"] & term_weight["good"], result['low'])
    rule28  = ctrl.Rule(title_word["poor"] & sentence_length["poor"] & sentence_location["poor"] & numerical_data["poor"] & thematic_keyword["average"] & proper_noun["poor"] & sentence_similarity["poor"] & term_weight["poor"], result['low'])
    rule29  = ctrl.Rule(title_word["poor"] & sentence_length["poor"] & sentence_location["poor"] & numerical_data["poor"] & thematic_keyword["average"] & proper_noun["poor"] & sentence_similarity["poor"] & term_weight["average"], result['low'])
    rule30  = ctrl.Rule(title_word["poor"] & sentence_length["poor"] & sentence_location["poor"] & numerical_data["poor"] & thematic_keyword["average"] & proper_noun["poor"] & sentence_similarity["poor"] & term_weight["good"], result['low'])
    rule31  = ctrl.Rule(title_word["poor"] & sentence_length["poor"] & sentence_location["poor"] & numerical_data["poor"] & thematic_keyword["average"] & proper_noun["poor"] & sentence_similarity["average"] & term_weight["poor"], result['low'])
    rule32  = ctrl.Rule(title_word["poor"] & sentence_length["poor"] & sentence_location["poor"] & numerical_data["poor"] & thematic_keyword["average"] & proper_noun["poor"] & sentence_similarity["average"] & term_weight["average"], result['low'])
    rule33  = ctrl.Rule(title_word["poor"] & sentence_length["poor"] & sentence_location["poor"] & numerical_data["poor"] & thematic_keyword["average"] & proper_noun["poor"] & sentence_similarity["average"] & term_weight["good"], result['low'])
    rule34  = ctrl.Rule(title_word["poor"] & sentence_length["poor"] & sentence_location["poor"] & numerical_data["poor"] & thematic_keyword["average"] & proper_noun["poor"] & sentence_similarity["good"] & term_weight["poor"], result['low'])
    rule35  = ctrl.Rule(title_word["poor"] & sentence_length["poor"] & sentence_location["poor"] & numerical_data["poor"] & thematic_keyword["average"] & proper_noun["poor"] & sentence_similarity["good"] & term_weight["average"], result['low'])
    rule36  = ctrl.Rule(title_word["poor"] & sentence_length["poor"] & sentence_location["poor"] & numerical_data["poor"] & thematic_keyword["average"] & proper_noun["poor"] & sentence_similarity["good"] & term_weight["good"], result['low'])
    rule37  = ctrl.Rule(title_word["poor"] & sentence_length["poor"] & sentence_location["poor"] & numerical_data["poor"] & thematic_keyword["average"] & proper_noun["average"] & sentence_similarity["poor"] & term_weight["poor"], result['low'])
    rule38  = ctrl.Rule(title_word["poor"] & sentence_length["poor"] & sentence_location["poor"] & numerical_data["poor"] & thematic_keyword["average"] & proper_noun["average"] & sentence_similarity["poor"] & term_weight["average"], result['low'])
    rule39  = ctrl.Rule(title_word["poor"] & sentence_length["poor"] & sentence_location["poor"] & numerical_data["poor"] & thematic_keyword["average"] & proper_noun["average"] & sentence_similarity["poor"] & term_weight["good"], result['low'])
    rule40  = ctrl.Rule(title_word["poor"] & sentence_length["poor"] & sentence_location["poor"] & numerical_data["poor"] & thematic_keyword["average"] & proper_noun["average"] & sentence_similarity["average"] & term_weight["poor"], result['low'])
    rule41  = ctrl.Rule(title_word["poor"] & sentence_length["poor"] & sentence_location["poor"] & numerical_data["poor"] & thematic_keyword["average"] & proper_noun["average"] & sentence_similarity["average"] & term_weight["average"], result['low'])
    rule42  = ctrl.Rule(title_word["poor"] & sentence_length["poor"] & sentence_location["poor"] & numerical_data["poor"] & thematic_keyword["average"] & proper_noun["average"] & sentence_similarity["average"] & term_weight["good"],result['low'])
    rule43  = ctrl.Rule(title_word["poor"] & sentence_length["poor"] & sentence_location["poor"] & numerical_data["poor"] & thematic_keyword["average"] & proper_noun["average"] & sentence_similarity["good"] & term_weight["poor"], result['low'])
    rule44  = ctrl.Rule(title_word["poor"] & sentence_length["poor"] & sentence_location["poor"] & numerical_data["poor"] & thematic_keyword["average"] & proper_noun["average"] & sentence_similarity["good"] & term_weight["average"],result['low'])
    rule45  = ctrl.Rule(title_word["poor"] & sentence_length["poor"] & sentence_location["poor"] & numerical_data["poor"] & thematic_keyword["average"] & proper_noun["average"] & sentence_similarity["good"] & term_weight["good"], result['low'])
    rule46  = ctrl.Rule(title_word["poor"] & sentence_length["poor"] & sentence_location["poor"] & numerical_data["poor"] & thematic_keyword["average"] & proper_noun["good"] & sentence_similarity["poor"] & term_weight["poor"], result['low'])
    rule47  = ctrl.Rule(title_word["poor"] & sentence_length["poor"] & sentence_location["poor"] & numerical_data["poor"] & thematic_keyword["average"] & proper_noun["good"] & sentence_similarity["poor"] & term_weight["average"], result['low'])
    rule48  = ctrl.Rule(title_word["poor"] & sentence_length["poor"] & sentence_location["poor"] & numerical_data["poor"] & thematic_keyword["average"] & proper_noun["good"] & sentence_similarity["poor"] & term_weight["good"], result['low'])
    rule49  = ctrl.Rule(title_word["poor"] & sentence_length["poor"] & sentence_location["poor"] & numerical_data["poor"] & thematic_keyword["average"] & proper_noun["good"] & sentence_similarity["average"] & term_weight["poor"], result['low'])
    rule50  = ctrl.Rule(title_word["poor"] & sentence_length["poor"] & sentence_location["poor"] & numerical_data["poor"] & thematic_keyword["average"] & proper_noun["good"] & sentence_similarity["average"] & term_weight["average"],result['low'])
    rule51  = ctrl.Rule(title_word["poor"] & sentence_length["poor"] & sentence_location["poor"] & numerical_data["poor"] & thematic_keyword["average"] & proper_noun["good"] & sentence_similarity["average"] & term_weight["good"], result['low'])
    rule52  = ctrl.Rule(title_word["poor"] & sentence_length["poor"] & sentence_location["poor"] & numerical_data["poor"] & thematic_keyword["average"] & proper_noun["good"] & sentence_similarity["good"] & term_weight["poor"], result['low'])
    rule53  = ctrl.Rule(title_word["poor"] & sentence_length["poor"] & sentence_location["poor"] & numerical_data["poor"] & thematic_keyword["average"] & proper_noun["good"] & sentence_similarity["good"] & term_weight["average"], result['low'])
    rule54  = ctrl.Rule(title_word["poor"] & sentence_length["poor"] & sentence_location["poor"] & numerical_data["poor"] & thematic_keyword["average"] & proper_noun["good"] & sentence_similarity["good"] & term_weight["good"], result['low'])
    rule55  = ctrl.Rule(title_word["poor"] & sentence_length["poor"] & sentence_location["poor"] & numerical_data["poor"] & thematic_keyword["good"] & proper_noun["poor"] & sentence_similarity["poor"] & term_weight["poor"], result['low'])
    rule56  = ctrl.Rule(title_word["poor"] & sentence_length["poor"] & sentence_location["poor"] & numerical_data["poor"] & thematic_keyword["good"] & proper_noun["poor"] & sentence_similarity["poor"] & term_weight["average"], result['low'])
    rule57  = ctrl.Rule(title_word["poor"] & sentence_length["poor"] & sentence