# -*- coding: utf-8 -*-
"""
@author: lucia
"""
import pandas as panda
#import os

#data = panda.read_csv(r"C:\Users\lucia\OneDrive\Escritorio\mental_health2.csv", encoding='iso-8859-1')
#data = panda.read_csv(r"C:\Users\lcalzado\Desktop\survey_2016.csv", encoding='iso-8859-1')
data = panda.read_csv(r"C:\Users\Lucía Calzado\Desktop\survey_2016.csv", encoding='iso-8859-1')

print(data)

data2 = data[data["Are you self-employed?"] == 0]

data2 = data2.drop(["Are you self-employed?",
                    "Is your employer primarily a tech company/organization?",
                    "Is your primary role within your company related to tech/IT?",
                    "Do you have medical coverage (private insurance or state-provided) which includes treatment of Â mental health issues?",
                    "Do you know local or online resources to seek help for a mental health disorder?",
                    "If you have been diagnosed or treated for a mental health disorder, do you ever reveal this to clients or business contacts?",
                    "If you have revealed a mental health issue to a client or business contact, do you believe this has impacted you negatively?",
                    "If you have been diagnosed or treated for a mental health disorder, do you ever reveal this to coworkers or employees?",
                    "If you have revealed a mental health issue to a coworker or employee, do you believe this has impacted you negatively?",
                    "Do you believe your productivity is ever affected by a mental health issue?",
                    "If yes, what percentage of your work time (time performing primary or secondary job functions) is affected by a mental health issue?",
                    "Do you have previous employers?",
                    "Have your previous employers provided mental health benefits?",
                    "Were you aware of the options for mental health care provided by your previous employers?",
                    "Did your previous employers ever formally discuss mental health (as part of a wellness campaign or other official communication)?",
                    "Did your previous employers provide resources to learn more about mental health issues and how to seek help?",
                    "Was your anonymity protected if you chose to take advantage of mental health or substance abuse treatment resources with previous employers?",
                    "Do you think that discussing a mental health disorder with previous employers would have negative consequences?",
                    "Do you think that discussing a physical health issue with previous employers would have negative consequences?",
                    "Would you have been willing to discuss a mental health issue with your previous co-workers?",
                    "Would you have been willing to discuss a mental health issue with your direct supervisor(s)?",
                    "Did you feel that your previous employers took mental health as seriously as physical health?",
                    "Did you hear of or observe negative consequences for co-workers with mental health issues in your previous workplaces?",
                    "Why or why not?",
                    "Why or why not?.1",
                    "How willing would you be to share with friends and family that you have a mental illness?",
                    "Do you have a family history of mental illness?",
                    "Have you had a mental health disorder in the past?",
                    "Do you currently have a mental health disorder?",
                    "Have you been diagnosed with a mental health condition by a medical professional?",
                    "If so, what condition(s) were you diagnosed with?",
                    "Have you ever sought treatment for a mental health issue from a mental health professional?",
                    "What country do you live in?",
                    "What US state or territory do you live in?",
                    "What country do you work in?",
                    "What US state or territory do you work in?",
                    "Which of the following best describes your work position?"
                    ], axis=1)
print(data2)


#data2.to_csv(r"C:\Users\lucia\OneDrive\Escritorio\resultado_2ej.csv", index=False)
#data2.to_csv(r"C:\Users\lcalzado\Desktop\resultado_2ej.csv", index=False)
data2.to_csv(r"C:\Users\Lucía Calzado\Desktop\resultado_2ej.csv", index=False)



