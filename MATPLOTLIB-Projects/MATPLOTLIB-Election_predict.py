import numpy as np
from matplotlib import pyplot as plt

survey_responses = ['Moon-Democratic Party', 'Lee-National Party', 'Moon-Democratic Party', 'Moon-Democratic Party', 'Moon-Democratic Party','Lee-National Party', 'Lee-National Party', 'Moon-Democratic Party','Moon-Democratic Party','Moon-Democratic Party','Moon-Democratic Party','Moon-Democratic Party','Moon-Democratic Party','Moon-Democratic Party','Moon-Democratic Party','Moon-Democratic Party','Moon-Democratic Party',
'Moon-Democratic Party', 'Moon-Democratic Party', 'Moon-Democratic Party', 'Lee-National Party', 'Moon-Democratic Party', 'Moon-Democratic Party', 'Moon-Democratic Party', 
'Lee-National Party', 'Lee-National Party', 'Moon-Democratic Party', 'Moon-Democratic Party', 'Lee-National Party', 'Moon-Democratic Party', 'Moon-Democratic Party',
'Moon-Democratic Party', 'Moon-Democratic Party', 'Lee-National Party', 'Moon-Democratic Party', 'Moon-Democratic Party', 'Moon-Democratic Party', 'Moon-Democratic Party', 
'Moon-Democratic Party', 'Moon-Democratic Party', 'Moon-Democratic Party', 'Lee-National Party', 'Moon-Democratic Party', 'Moon-Democratic Party', 'Lee-National Party', 
'Lee-National Party', 'Lee-National Party', 'Moon-Democratic Party', 'Lee-National Party', 'Lee-National Party', 'Lee-National Party', 'Lee-National Party', 'Lee-National Party', 
'Moon-Democratic Party', 'Lee-National Party', 'Moon-Democratic Party', 'Lee-National Party', 'Moon-Democratic Party', 'Lee-National Party', 'Moon-Democratic Party', 'Moon-Democratic Party', 
'Lee-National Party', 'Moon-Democratic Party', 'Lee-National Party', 'Lee-National Party', 'Lee-National Party', 'Lee-National Party', 'Lee-National Party', 'Moon-Democratic Party', 
'Moon-Democratic Party', 'Lee-National Party', 'Moon-Democratic Party', 'Lee-National Party', 'Moon-Democratic Party', 'Lee-National Party', 'Moon-Democratic Party', 'Lee-National Party', 
'Lee-National Party', 'Moon-Democratic Party', 'Lee-National Party']

total_Moon = sum([1 for n in survey_responses if n== 'Moon-Democratic Party'])
lensurvey=float(len(survey_responses))
percentage_Moon = total_Moon/lensurvey

#print(percentage_Moon)

possible_surveys = np.random.binomial(lensurvey, 0.54, size=10000)/lensurvey

plt.hist(possible_surveys, range=(0,1),bins=20)

possible_surveys_len = float(len(possible_surveys))
incorrect_predictions = len(possible_surveys[tuple([possible_surveys< .5])])

Moon_loss_surveys = incorrect_predictions/possible_surveys_len

large_survey_length = float(7000)
large_survey = np.random.binomial(large_survey_length, .54 , size = 1000)/large_survey_length

plt.close()
plt.hist(possible_surveys, range=(0,1), bins=20)
plt.hist(large_survey, alpha=0.5, range=(0,1), bins=20)
plt.show()

