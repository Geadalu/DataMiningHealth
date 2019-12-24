"""
@author: lucia
"""

import pandas as panda
import numpy as np

data3 = panda.read_csv(r"C:\Users\lcalzado\Desktop\resultado_2ej.csv", encoding='iso-8859-1')
#data3 = panda.read_csv(r"C:\Users\lucia\OneDrive\Escritorio\resultado_2ej.csv", encoding='iso-8859-1')

data3 = data3.replace(to_replace = {'How many employees does your company or organization have?': '1-5'}, value = 5)
data3 = data3.replace(to_replace = {'How many employees does your company or organization have?': '6-25'}, value = 25)
data3 = data3.replace(to_replace = {'How many employees does your company or organization have?': '26-100'}, value = 100)
data3 = data3.replace(to_replace = {'How many employees does your company or organization have?': '100-500'}, value = 500)
data3 = data3.replace(to_replace = {'How many employees does your company or organization have?': '500-1000'}, value = 1000)
data3 = data3.replace(to_replace = {'How many employees does your company or organization have?': 'More than 1000'}, value = 1500)

data3 = data3.replace(to_replace = {'Does your employer provide mental health benefits as part of healthcare coverage?': 'No'}, value = 0)
data3 = data3.replace(to_replace = {'Does your employer provide mental health benefits as part of healthcare coverage?': 'I don\'t know'}, value = 1)
data3 = data3.replace(to_replace = {'Does your employer provide mental health benefits as part of healthcare coverage?': 'Yes'}, value = 2)
data3 = data3.replace(to_replace = {'Does your employer provide mental health benefits as part of healthcare coverage?': 'Not eligible for coverage / N/A'}, value = 3)

data3 = data3.replace(to_replace = {'Do you know the options for mental health care available under your employer-provided coverage?': 'No'}, value = 0)
data3 = data3.replace(to_replace = {'Do you know the options for mental health care available under your employer-provided coverage?': 'I am not sure'}, value = 1)
data3 = data3.replace(to_replace = {'Do you know the options for mental health care available under your employer-provided coverage?': 'Yes'}, value = 2)
data3['Do you know the options for mental health care available under your employer-provided coverage?'].fillna(1, inplace = True)

data3 = data3.replace(to_replace = {'Has your employer ever formally discussed mental health?': 'No'}, value = 0)
data3 = data3.replace(to_replace = {'Has your employer ever formally discussed mental health?': 'I don\'t know'}, value = 1)
data3 = data3.replace(to_replace = {'Has your employer ever formally discussed mental health?': 'Yes'}, value = 2)

data3 = data3.replace(to_replace = {'Does your employer offer resources to learn more about mental health concerns and options for seeking help?': 'No'}, value = 0)
data3 = data3.replace(to_replace = {'Does your employer offer resources to learn more about mental health concerns and options for seeking help?': 'I don\'t know'}, value = 1)
data3 = data3.replace(to_replace = {'Does your employer offer resources to learn more about mental health concerns and options for seeking help?': 'Yes'}, value = 2)

data3 = data3.replace(to_replace = {'Is your anonymity protected if you choose to take advantage of mental health or substance abuse treatment resources provided by your employer?': 'No'}, value = 0)
data3 = data3.replace(to_replace = {'Is your anonymity protected if you choose to take advantage of mental health or substance abuse treatment resources provided by your employer?': 'I don\'t know'}, value = 1)
data3 = data3.replace(to_replace = {'Is your anonymity protected if you choose to take advantage of mental health or substance abuse treatment resources provided by your employer?': 'Yes'}, value = 2)

data3 = data3.replace(to_replace = {'If a mental health issue prompted you to request a medical leave from work asking for that leave would be:': 'Very easy'}, value = 0)
data3 = data3.replace(to_replace = {'If a mental health issue prompted you to request a medical leave from work asking for that leave would be:': 'Somewhat easy'}, value = 1)
data3 = data3.replace(to_replace = {'If a mental health issue prompted you to request a medical leave from work asking for that leave would be:': 'I don\'t know'}, value = 2)
data3 = data3.replace(to_replace = {'If a mental health issue prompted you to request a medical leave from work asking for that leave would be:': 'Neither easy nor difficult'}, value = 3)
data3 = data3.replace(to_replace = {'If a mental health issue prompted you to request a medical leave from work asking for that leave would be:': 'Somewhat difficult'}, value = 4)
data3 = data3.replace(to_replace = {'If a mental health issue prompted you to request a medical leave from work asking for that leave would be:': 'Very difficult'}, value = 5)

data3 = data3.replace(to_replace = {'Do you think that discussing a mental health disorder with your employer would have negative consequences?': 'No'}, value = 0);
data3 = data3.replace(to_replace = {'Do you think that discussing a mental health disorder with your employer would have negative consequences?': 'Maybe'}, value = 1);
data3 = data3.replace(to_replace = {'Do you think that discussing a mental health disorder with your employer would have negative consequences?': 'Yes'}, value = 2);

data3 = data3.replace(to_replace = {'Do you think that discussing a physical health issue with your employer would have negative consequences?': 'No'}, value = 0);
data3 = data3.replace(to_replace = {'Do you think that discussing a physical health issue with your employer would have negative consequences?': 'Maybe'}, value = 1);
data3 = data3.replace(to_replace = {'Do you think that discussing a physical health issue with your employer would have negative consequences?': 'Yes'}, value = 2);

data3 = data3.replace(to_replace = {'Would you feel comfortable discussing a mental health disorder with your coworkers?': 'No'}, value = 0);
data3 = data3.replace(to_replace = {'Would you feel comfortable discussing a mental health disorder with your coworkers?': 'Maybe'}, value = 1);
data3 = data3.replace(to_replace = {'Would you feel comfortable discussing a mental health disorder with your coworkers?': 'Yes'}, value = 2);

data3 = data3.replace(to_replace = {'Would you feel comfortable discussing a mental health disorder with your direct supervisor(s)?': 'No'}, value = 0);
data3 = data3.replace(to_replace = {'Would you feel comfortable discussing a mental health disorder with your direct supervisor(s)?': 'Maybe'}, value = 1);
data3 = data3.replace(to_replace = {'Would you feel comfortable discussing a mental health disorder with your direct supervisor(s)?': 'Yes'}, value = 2);

data3 = data3.replace(to_replace = {'Do you feel that your employer takes mental health as seriously as physical health?': 'No'}, value = 0)
data3 = data3.replace(to_replace = {'Do you feel that your employer takes mental health as seriously as physical health?': 'I don\'t know'}, value = 1)
data3 = data3.replace(to_replace = {'Do you feel that your employer takes mental health as seriously as physical health?': 'Yes'}, value = 2)

data3 = data3.replace(to_replace = {'Have you heard of or observed negative consequences for co-workers who have been open about mental health issues in your workplace?': 'No'}, value = 0)
data3 = data3.replace(to_replace = {'Have you heard of or observed negative consequences for co-workers who have been open about mental health issues in your workplace?': 'Yes'}, value = 1)

data3 = data3.replace(to_replace = {'Would you be willing to bring up a physical health issue with a potential employer in an interview?': 'No'}, value = 0);
data3 = data3.replace(to_replace = {'Would you be willing to bring up a physical health issue with a potential employer in an interview?': 'Maybe'}, value = 1);
data3 = data3.replace(to_replace = {'Would you be willing to bring up a physical health issue with a potential employer in an interview?': 'Yes'}, value = 2);

data3 = data3.replace(to_replace = {'Would you bring up a mental health issue with a potential employer in an interview?': 'No'}, value = 0);
data3 = data3.replace(to_replace = {'Would you bring up a mental health issue with a potential employer in an interview?': 'Maybe'}, value = 1);
data3 = data3.replace(to_replace = {'Would you bring up a mental health issue with a potential employer in an interview?': 'Yes'}, value = 2);

data3 = data3.replace(to_replace = {'Do you feel that being identified as a person with a mental health issue would hurt your career?': 'No, it has not'}, value = 0);
data3 = data3.replace(to_replace = {'Do you feel that being identified as a person with a mental health issue would hurt your career?': 'No, I don\'t think it would'}, value = 1);
data3 = data3.replace(to_replace = {'Do you feel that being identified as a person with a mental health issue would hurt your career?': 'Maybe'}, value = 2);
data3 = data3.replace(to_replace = {'Do you feel that being identified as a person with a mental health issue would hurt your career?': 'Yes, I think it would'}, value = 3);
data3 = data3.replace(to_replace = {'Do you feel that being identified as a person with a mental health issue would hurt your career?': 'Yes, it has'}, value = 4);

data3 = data3.replace(to_replace = {'Do you think that team members/co-workers would view you more negatively if they knew you suffered from a mental health issue?': 'No, they do not'}, value = 0);
data3 = data3.replace(to_replace = {'Do you think that team members/co-workers would view you more negatively if they knew you suffered from a mental health issue?': 'No, I don\'t think they would'}, value = 1);
data3 = data3.replace(to_replace = {'Do you think that team members/co-workers would view you more negatively if they knew you suffered from a mental health issue?': 'Maybe'}, value = 2);
data3 = data3.replace(to_replace = {'Do you think that team members/co-workers would view you more negatively if they knew you suffered from a mental health issue?': 'Yes, I think they would'}, value = 3);
data3 = data3.replace(to_replace = {'Do you think that team members/co-workers would view you more negatively if they knew you suffered from a mental health issue?': 'Yes, they do'}, value = 4);

data3 = data3.replace(to_replace = {'Have you observed or experienced an unsupportive or badly handled response to a mental health issue in your current or previous workplace?': 'No'}, value = 0);
data3 = data3.replace(to_replace = {'Have you observed or experienced an unsupportive or badly handled response to a mental health issue in your current or previous workplace?': 'Maybe/Not sure'}, value = 1);
data3['Have you observed or experienced an unsupportive or badly handled response to a mental health issue in your current or previous workplace?'].fillna(1, inplace = True)
data3 = data3.replace(to_replace = {'Have you observed or experienced an unsupportive or badly handled response to a mental health issue in your current or previous workplace?': 'Yes'}, value = 2);
data3 = data3.replace(to_replace = {'Have you observed or experienced an unsupportive or badly handled response to a mental health issue in your current or previous workplace?': 'Yes, I observed'}, value = 3);
data3 = data3.replace(to_replace = {'Have you observed or experienced an unsupportive or badly handled response to a mental health issue in your current or previous workplace?': 'Yes, I experienced'}, value = 4);

data3 = data3.replace(to_replace = {'Have your observations of how another individual who discussed a mental health disorder made you less likely to reveal a mental health issue yourself in your current workplace?': 'No'}, value = 0);
data3 = data3.replace(to_replace = {'Have your observations of how another individual who discussed a mental health disorder made you less likely to reveal a mental health issue yourself in your current workplace?': 'Maybe'}, value = 1);
data3 = data3.replace(to_replace = {'Have your observations of how another individual who discussed a mental health disorder made you less likely to reveal a mental health issue yourself in your current workplace?': 'Yes'}, value = 2);
data3['Have your observations of how another individual who discussed a mental health disorder made you less likely to reveal a mental health issue yourself in your current workplace?'].fillna(3, inplace = True) #tratado como "no aplica"

#data3 = data3.replace(to_replace = {'Do you currently have a mental health disorder?': 'No'}, value = 0);
#data3 = data3.replace(to_replace = {'Do you currently have a mental health disorder?': 'Maybe'}, value = 1);
#data3 = data3.replace(to_replace = {'Do you currently have a mental health disorder?': 'Yes'}, value = 1);
#data3 = data3.replace(to_replace = {'label': 'Yes'}, value = 2);

################################################################################################################################
data3 = data3.replace(to_replace = {'If yes what condition(s) have you been diagnosed with?': ['Anxiety Disorder (Generalized, Social, Phobia, etc)',
                                    'Anxiety Disorder (Generalized, Social, Phobia, etc)|Asperges', 
                                    'Anxiety Disorder (Generalized, Social, Phobia, etc)|Attention Deficit Hyperactivity Disorder', 
                                    'Anxiety Disorder (Generalized, Social, Phobia, etc)|Attention Deficit Hyperactivity Disorder|Obsessive-Compulsive Disorder', 
                                    'Anxiety Disorder (Generalized, Social, Phobia, etc)|Attention Deficit Hyperactivity Disorder|Post-traumatic Stress Disorder', 
                                    'Anxiety Disorder (Generalized, Social, Phobia, etc)|Attention Deficit Hyperactivity Disorder|Post-traumatic Stress Disorder|Addictive Disorder', 
                                    'Anxiety Disorder (Generalized, Social, Phobia, etc)|Attention Deficit Hyperactivity Disorder|Stress Response Syndromes', 
                                    'Anxiety Disorder (Generalized, Social, Phobia, etc)|Eating Disorder (Anorexia, Bulimia, etc)|Stress Response Syndromes', 
                                    'Anxiety Disorder (Generalized, Social, Phobia, etc)|Mood Disorder (Depression, Bipolar Disorder, etc)', 
                                    'Anxiety Disorder (Generalized, Social, Phobia, etc)|Mood Disorder (Depression, Bipolar Disorder, etc)|Addictive Disorder', 
                                    'Anxiety Disorder (Generalized, Social, Phobia, etc)|Mood Disorder (Depression, Bipolar Disorder, etc)|Attention Deficit Hyperactivity Disorder', 
                                    'Anxiety Disorder (Generalized, Social, Phobia, etc)|Mood Disorder (Depression, Bipolar Disorder, etc)|Attention Deficit Hyperactivity Disorder|Dissociative Disorder', 
                                    'Anxiety Disorder (Generalized, Social, Phobia, etc)|Mood Disorder (Depression, Bipolar Disorder, etc)|Attention Deficit Hyperactivity Disorder|Obsessive-Compulsive Disorder',  
                                    'Anxiety Disorder (Generalized, Social, Phobia, etc)|Mood Disorder (Depression, Bipolar Disorder, etc)|Attention Deficit Hyperactivity Disorder|Obsessive-Compulsive Disorder|Substance Use Disorder', 
                                    'Anxiety Disorder (Generalized, Social, Phobia, etc)|Mood Disorder (Depression, Bipolar Disorder, etc)|Attention Deficit Hyperactivity Disorder|Personality Disorder (Borderline, Antisocial, Paranoid, etc)', 
                                    'Anxiety Disorder (Generalized, Social, Phobia, etc)|Mood Disorder (Depression, Bipolar Disorder, etc)|Attention Deficit Hyperactivity Disorder|Personality Disorder (Borderline, Antisocial, Paranoid, etc)|Obsessive-Compulsive Disorder|Post-traumatic Stress Disorder', 
                                    'Anxiety Disorder (Generalized, Social, Phobia, etc)|Mood Disorder (Depression, Bipolar Disorder, etc)|Attention Deficit Hyperactivity Disorder|Personality Disorder (Borderline, Antisocial, Paranoid, etc)|Stress Response Syndromes|Addictive Disorder', 
                                    'Anxiety Disorder (Generalized, Social, Phobia, etc)|Mood Disorder (Depression, Bipolar Disorder, etc)|Attention Deficit Hyperactivity Disorder|Post-traumatic Stress Disorder', 
                                    'Anxiety Disorder (Generalized, Social, Phobia, etc)|Mood Disorder (Depression, Bipolar Disorder, etc)|Attention Deficit Hyperactivity Disorder|Post-traumatic Stress Disorder|Substance Use Disorder', 
                                    'Anxiety Disorder (Generalized, Social, Phobia, etc)|Mood Disorder (Depression, Bipolar Disorder, etc)|Attention Deficit Hyperactivity Disorder|Substance Use Disorder', 
                                    'Anxiety Disorder (Generalized, Social, Phobia, etc)|Mood Disorder (Depression, Bipolar Disorder, etc)|Dissociative Disorder', 
                                    'Anxiety Disorder (Generalized, Social, Phobia, etc)|Mood Disorder (Depression, Bipolar Disorder, etc)|Eating Disorder (Anorexia, Bulimia, etc)', 
                                    'Anxiety Disorder (Generalized, Social, Phobia, etc)|Mood Disorder (Depression, Bipolar Disorder, etc)|Eating Disorder (Anorexia, Bulimia, etc)|Obsessive-Compulsive Disorder', 
                                    'Anxiety Disorder (Generalized, Social, Phobia, etc)|Mood Disorder (Depression, Bipolar Disorder, etc)|Eating Disorder (Anorexia, Bulimia, etc)|Personality Disorder (Borderline, Antisocial, Paranoid, etc)|Obsessive-Compulsive Disorder|Stress Response Syndromes|Dissociative Disorder|Substance Use Disorder', 
                                    'Anxiety Disorder (Generalized, Social, Phobia, etc)|Mood Disorder (Depression, Bipolar Disorder, etc)|Eating Disorder (Anorexia, Bulimia, etc)|Post-traumatic Stress Disorder', 
                                    'Anxiety Disorder (Generalized, Social, Phobia, etc)|Mood Disorder (Depression, Bipolar Disorder, etc)|Obsessive-Compulsive Disorder', 
                                    'Anxiety Disorder (Generalized, Social, Phobia, etc)|Mood Disorder (Depression, Bipolar Disorder, etc)|Obsessive-Compulsive Disorder|Post-traumatic Stress Disorder', 
                                    'Anxiety Disorder (Generalized, Social, Phobia, etc)|Mood Disorder (Depression, Bipolar Disorder, etc)|Obsessive-Compulsive Disorder|Post-traumatic Stress Disorder|Stress Response Syndromes', 
                                    'Anxiety Disorder (Generalized, Social, Phobia, etc)|Mood Disorder (Depression, Bipolar Disorder, etc)|Obsessive-Compulsive Disorder|Substance Use Disorder', 
                                    'Anxiety Disorder (Generalized, Social, Phobia, etc)|Mood Disorder (Depression, Bipolar Disorder, etc)|Personality Disorder (Borderline, Antisocial, Paranoid, etc)', 
                                    'Anxiety Disorder (Generalized, Social, Phobia, etc)|Mood Disorder (Depression, Bipolar Disorder, etc)|Personality Disorder (Borderline, Antisocial, Paranoid, etc)|Post-traumatic Stress Disorder|Substance Use Disorder|Addictive Disorder', 
                                    'Anxiety Disorder (Generalized, Social, Phobia, etc)|Mood Disorder (Depression, Bipolar Disorder, etc)|Personality Disorder (Borderline, Antisocial, Paranoid, etc)|Stress Response Syndromes', 
                                    'Anxiety Disorder (Generalized, Social, Phobia, etc)|Mood Disorder (Depression, Bipolar Disorder, etc)|Post-traumatic Stress Disorder', 
                                    'Anxiety Disorder (Generalized, Social, Phobia, etc)|Mood Disorder (Depression, Bipolar Disorder, etc)|Post-traumatic Stress Disorder|Addictive Disorder', 
                                    'Anxiety Disorder (Generalized, Social, Phobia, etc)|Mood Disorder (Depression, Bipolar Disorder, etc)|Post-traumatic Stress Disorder|Addictive Disorder|Autism', 
                                    'Anxiety Disorder (Generalized, Social, Phobia, etc)|Mood Disorder (Depression, Bipolar Disorder, etc)|Post-traumatic Stress Disorder|Stress Response Syndromes', 
                                    'Anxiety Disorder (Generalized, Social, Phobia, etc)|Mood Disorder (Depression, Bipolar Disorder, etc)|Post-traumatic Stress Disorder|Substance Use Disorder', 
                                    'Anxiety Disorder (Generalized, Social, Phobia, etc)|Mood Disorder (Depression, Bipolar Disorder, etc)|Post-traumatic Stress Disorder|Substance Use Disorder|Addictive Disorder', 
                                    'Anxiety Disorder (Generalized, Social, Phobia, etc)|Mood Disorder (Depression, Bipolar Disorder, etc)|Stress Response Syndromes', 
                                    'Anxiety Disorder (Generalized, Social, Phobia, etc)|Mood Disorder (Depression, Bipolar Disorder, etc)|Stress Response Syndromes|Substance Use Disorder', 
                                    'Anxiety Disorder (Generalized, Social, Phobia, etc)|Mood Disorder (Depression, Bipolar Disorder, etc)|Substance Use Disorder', 
                                    'Anxiety Disorder (Generalized, Social, Phobia, etc)|Mood Disorder (Depression, Bipolar Disorder, etc)|Substance Use Disorder|Addictive Disorder', 
                                    'Anxiety Disorder (Generalized, Social, Phobia, etc)|Obsessive-Compulsive Disorder', 
                                    'Anxiety Disorder (Generalized, Social, Phobia, etc)|Obsessive-Compulsive Disorder|Post-traumatic Stress Disorder', 
                                    'Anxiety Disorder (Generalized, Social, Phobia, etc)|Obsessive-Compulsive Disorder|Stress Response Syndromes', 
                                    'Anxiety Disorder (Generalized, Social, Phobia, etc)|Personality Disorder (Borderline, Antisocial, Paranoid, etc)|Obsessive-Compulsive Disorder', 
                                    'Anxiety Disorder (Generalized, Social, Phobia, etc)|Personality Disorder (Borderline, Antisocial, Paranoid, etc)|Substance Use Disorder|Addictive Disorder', 
                                    'Anxiety Disorder (Generalized, Social, Phobia, etc)|Post-traumatic Stress Disorder', 
                                    'Anxiety Disorder (Generalized, Social, Phobia, etc)|Post-traumatic Stress Disorder|Stress Response Syndromes', 
                                    'Anxiety Disorder (Generalized, Social, Phobia, etc)|Post-traumatic Stress Disorder|Stress Response Syndromes|Autism spectrum disorder', 
                                    'Anxiety Disorder (Generalized, Social, Phobia, etc)|Stress Response Syndromes', 
                                    'Anxiety Disorder (Generalized, Social, Phobia, etc)|Stress Response Syndromes|Substance Use Disorder', 
                                    'Anxiety Disorder (Generalized, Social, Phobia, etc)|Substance Use Disorder'], }, value = 0);
data3 = data3.replace(to_replace = {'If yes what condition(s) have you been diagnosed with?': ['Attention Deficit Hyperactivity Disorder', 'Attention Deficit Hyperactivity Disorder|Addictive Disorder',
                                    'Attention Deficit Hyperactivity Disorder|Obsessive-Compulsive Disorder|Stress Response Syndromes', 'Attention Deficit Hyperactivity Disorder|PTSD (undiagnosed)',
                                    'Attention Deficit Hyperactivity Disorder|Pervasive Developmental Disorder (Not Otherwise Specified)']}, value = 1);
data3 = data3.replace(to_replace = {'If yes what condition(s) have you been diagnosed with?': ['Autism Spectrum Disorder', 'Autism (Asperger\'s)']}, value = 2);
data3 = data3.replace(to_replace = {'If yes what condition(s) have you been diagnosed with?': 'Eating Disorder (Anorexia, Bulimia, etc)'}, value = 3);
data3 = data3.replace(to_replace = {'If yes what condition(s) have you been diagnosed with?': ['Eating Disorder (Anorexia, Bulimia, etc)|Mood Disorder (Depression, Bipolar Disorder, etc)',
                                    'Mood Disorder (Depression, Bipolar Disorder, etc)|Addictive Disorder',
                                    'Mood Disorder (Depression, Bipolar Disorder, etc)|Anxiety Disorder (Generalized, Social, Phobia, etc)', 'Mood Disorder (Depression, Bipolar Disorder, etc)|Anxiety Disorder (Generalized, Social, Phobia, etc)',
                                    'Mood Disorder (Depression, Bipolar Disorder, etc)|Attention Deficit Hyperactivity Disorder', 
                                    'Mood Disorder (Depression, Bipolar Disorder, etc)|Attention Deficit Hyperactivity Disorder|Obsessive-Compulsive Disorder|Addictive Disorder',
                                    'Mood Disorder (Depression, Bipolar Disorder, etc)|Attention Deficit Hyperactivity Disorder|Personality Disorder (Borderline, Antisocial, Paranoid, etc)',
                                    'Mood Disorder (Depression, Bipolar Disorder, etc)|Attention Deficit Hyperactivity Disorder|Personality Disorder (Borderline, Antisocial, Paranoid, etc)|Stress Response Syndromes|Addictive Disorder',
                                    'Mood Disorder (Depression, Bipolar Disorder, etc)|Attention Deficit Hyperactivity Disorder|Post-traumatic Stress Disorder',
                                    'Mood Disorder (Depression, Bipolar Disorder, etc)|Eating Disorder (Anorexia, Bulimia, etc)',
                                    'Mood Disorder (Depression, Bipolar Disorder, etc)|Eating Disorder (Anorexia, Bulimia, etc)|Attention Deficit Hyperactivity Disorder|Personality Disorder (Borderline, Antisocial, Paranoid, etc)',
                                    'Mood Disorder (Depression, Bipolar Disorder, etc)|Eating Disorder (Anorexia, Bulimia, etc)|Obsessive-Compulsive Disorder',
                                    'Mood Disorder (Depression, Bipolar Disorder, etc)|Personality Disorder (Borderline, Antisocial, Paranoid, etc)',
                                    'Mood Disorder (Depression, Bipolar Disorder, etc)|Personality Disorder (Borderline, Antisocial, Paranoid, etc)|Addictive Disorder',
                                    'Mood Disorder (Depression, Bipolar Disorder, etc)|Personality Disorder (Borderline, Antisocial, Paranoid, etc)|Post-traumatic Stress Disorder',
                                    'Mood Disorder (Depression, Bipolar Disorder, etc)|Post-traumatic Stress Disorder',
                                    'Mood Disorder (Depression, Bipolar Disorder, etc)|Post-traumatic Stress Disorder|Addictive Disorder',
                                    'Mood Disorder (Depression, Bipolar Disorder, etc)|Post-traumatic Stress Disorder|Dissociative Disorder',
                                    'Mood Disorder (Depression, Bipolar Disorder, etc)|Stress Response Syndromes',
                                    'Mood Disorder (Depression, Bipolar Disorder, etc)|Substance Use Disorder',
                                    'Mood Disorder (Depression, Bipolar Disorder, etc)',
                                    'Mood Disorder (Depression, Bipolar Disorder, etc)|Attention Deficit Hyperactivity Disorder|Post-traumatic Stress Disorder|Substance Use Disorder',
                                    'Mood Disorder (Depression, Bipolar Disorder, etc)|Attention Deficit Hyperactivity Disorder|Substance Use Disorder'
                                    ]}, value = 4)
data3 = data3.replace(to_replace = {'If yes what condition(s) have you been diagnosed with?': ['Obsessive-Compulsive Disorder',
                                    'Obsessive-Compulsive Disorder|Eating Disorder (Anorexia, Bulimia, etc)|Mood Disorder (Depression, Bipolar Disorder, etc)|Anxiety Disorder (Generalized, Social, Phobia, etc)',
                                    'Obsessive-Compulsive Disorder|Substance Use Disorder']}, value = 5)
data3 = data3.replace(to_replace = {'If yes what condition(s) have you been diagnosed with?': 'Personality Disorder (Borderline, Antisocial, Paranoid, etc)'}, value = 6)
data3 = data3.replace(to_replace = {'If yes what condition(s) have you been diagnosed with?': ['Post-traumatic Stress Disorder',
                                    'Post-traumatic Stress Disorder|Dissociative Disorder',
                                    'Post-traumatic Stress Disorder|Stress Response Syndromes',
                                    ]}, value = 7)
data3 = data3.replace(to_replace = {'If yes what condition(s) have you been diagnosed with?': ['Psychotic Disorder (Schizophrenia, Schizoaffective, etc)',
                                    'Psychotic Disorder (Schizophrenia, Schizoaffective, etc)|Obsessive-Compulsive Disorder|ADD (w/o Hyperactivity)']}, value = 8)
data3 = data3.replace(to_replace = {'If yes what condition(s) have you been diagnosed with?': ['Schizotypal Personality Disorder',
                                    'Seasonal Affective Disorder',
                                    'Sexual addiction',
                                    'Stress Response Syndromes',
                                    'Addictive Disorder',
                                    'Stress Response Syndromes|Sleeping Disorder',
                                    'Substance Use Disorder|Addictive Disorder',
                                    'Transgender|Mood Disorder (Depression, Bipolar Disorder, etc)|Anxiety Disorder (Generalized, Social, Phobia, etc)',
                                    'Traumatic Brain Injury']}, value = 9) #otros
data3['If yes what condition(s) have you been diagnosed with?'].fillna(99, inplace = True)
################################################################################################################################

data3 = data3.replace(to_replace = {'If maybe what condition(s) do you believe you have?': ['Anxiety Disorder (Generalized, Social, Phobia, etc)',
                                    'Anxiety Disorder (Generalized, Social, Phobia, etc)|Addictive Disorder',
                                    'Anxiety Disorder (Generalized, Social, Phobia, etc)|Attention Deficit Hyperactivity Disorder',
                                    'Anxiety Disorder (Generalized, Social, Phobia, etc)|Attention Deficit Hyperactivity Disorder|Addictive Disorder',
                                    'Anxiety Disorder (Generalized, Social, Phobia, etc)|Attention Deficit Hyperactivity Disorder|Asperger\'s',
                                    'Anxiety Disorder (Generalized, Social, Phobia, etc)|Attention Deficit Hyperactivity Disorder|Post-traumatic Stress Disorder',
                                    'Anxiety Disorder (Generalized, Social, Phobia, etc)|Attention Deficit Hyperactivity Disorder|Substance Use Disorder',
                                    'Anxiety Disorder (Generalized, Social, Phobia, etc)|Eating Disorder (Anorexia, Bulimia, etc)|Stress Response Syndromes',
                                    'Anxiety Disorder (Generalized, Social, Phobia, etc)|Mood Disorder (Depression, Bipolar Disorder, etc)',
                                    'Anxiety Disorder (Generalized, Social, Phobia, etc)|Mood Disorder (Depression, Bipolar Disorder, etc)|Addictive Disorder',
                                    'Anxiety Disorder (Generalized, Social, Phobia, etc)|Mood Disorder (Depression, Bipolar Disorder, etc)|Attention Deficit Hyperactivity Disorder',
                                    'Anxiety Disorder (Generalized, Social, Phobia, etc)|Mood Disorder (Depression, Bipolar Disorder, etc)|Dissociative Disorder',
                                    'Anxiety Disorder (Generalized, Social, Phobia, etc)|Mood Disorder (Depression, Bipolar Disorder, etc)|Eating Disorder (Anorexia, Bulimia, etc)',
                                    'Anxiety Disorder (Generalized, Social, Phobia, etc)|Mood Disorder (Depression, Bipolar Disorder, etc)|Obsessive-Compulsive Disorder',
                                    'Anxiety Disorder (Generalized, Social, Phobia, etc)|Mood Disorder (Depression, Bipolar Disorder, etc)|Obsessive-Compulsive Disorder|Stress Response Syndromes',
                                    'Anxiety Disorder (Generalized, Social, Phobia, etc)|Mood Disorder (Depression, Bipolar Disorder, etc)|Personality Disorder (Borderline, Antisocial, Paranoid, etc)',
                                    'Anxiety Disorder (Generalized, Social, Phobia, etc)|Mood Disorder (Depression, Bipolar Disorder, etc)|Personality Disorder (Borderline, Antisocial, Paranoid, etc)|Stress Response Syndromes',
                                    'Anxiety Disorder (Generalized, Social, Phobia, etc)|Mood Disorder (Depression, Bipolar Disorder, etc)|Personality Disorder (Borderline, Antisocial, Paranoid, etc)|Stress Response Syndromes|Addictive Disorder',
                                    'Anxiety Disorder (Generalized, Social, Phobia, etc)|Mood Disorder (Depression, Bipolar Disorder, etc)|Personality Disorder (Borderline, Antisocial, Paranoid, etc)|Substance Use Disorder|Addictive Disorder',
                                    'Anxiety Disorder (Generalized, Social, Phobia, etc)|Mood Disorder (Depression, Bipolar Disorder, etc)|Post-traumatic Stress Disorder',
                                    'Anxiety Disorder (Generalized, Social, Phobia, etc)|Mood Disorder (Depression, Bipolar Disorder, etc)|Post-traumatic Stress Disorder|Stress Response Syndromes',
                                    'Anxiety Disorder (Generalized, Social, Phobia, etc)|Mood Disorder (Depression, Bipolar Disorder, etc)|Psychotic Disorder (Schizophrenia, Schizoaffective, etc)',
                                    'Anxiety Disorder (Generalized, Social, Phobia, etc)|Mood Disorder (Depression, Bipolar Disorder, etc)|Psychotic Disorder (Schizophrenia, Schizoaffective, etc)|Eating Disorder (Anorexia, Bulimia, etc)|Attention Deficit Hyperactivity Disorder|Obsessive-Compulsive Disorder|Post-traumatic Stress Disorder|Stress Response Syndromes',
                                    'Anxiety Disorder (Generalized, Social, Phobia, etc)|Mood Disorder (Depression, Bipolar Disorder, etc)|Psychotic Disorder (Schizophrenia, Schizoaffective, etc)|Obsessive-Compulsive Disorder|Post-traumatic Stress Disorder',
                                    'Anxiety Disorder (Generalized, Social, Phobia, etc)|Mood Disorder (Depression, Bipolar Disorder, etc)|Psychotic Disorder (Schizophrenia, Schizoaffective, etc)|Personality Disorder (Borderline, Antisocial, Paranoid, etc)|Stress Response Syndromes',
                                    'Anxiety Disorder (Generalized, Social, Phobia, etc)|Mood Disorder (Depression, Bipolar Disorder, etc)|Stress Response Syndromes',
                                    'Anxiety Disorder (Generalized, Social, Phobia, etc)|Obsessive-Compulsive Disorder',
                                    'Anxiety Disorder (Generalized, Social, Phobia, etc)|Obsessive-Compulsive Disorder|Stress Response Syndromes',
                                    'Anxiety Disorder (Generalized, Social, Phobia, etc)|Personality Disorder (Borderline, Antisocial, Paranoid, etc)',
                                    'Anxiety Disorder (Generalized, Social, Phobia, etc)|Post-traumatic Stress Disorder',
                                    'Anxiety Disorder (Generalized, Social, Phobia, etc)|Post-traumatic Stress Disorder|Stress Response Syndromes',
                                    'Anxiety Disorder (Generalized, Social, Phobia, etc)|Stress Response Syndromes',
                                    'Anxiety Disorder (Generalized, Social, Phobia, etc)|Stress Response Syndromes|Addictive Disorder',
                                    'Anxiety Disorder (Generalized, Social, Phobia, etc)|Mood Disorder (Depression, Bipolar Disorder, etc)|Attention Deficit Hyperactivity Disorder|Obsessive-Compulsive Disorder',
                                    'Anxiety Disorder (Generalized, Social, Phobia, etc)|Mood Disorder (Depression, Bipolar Disorder, etc)|Attention Deficit Hyperactivity Disorder|Personality Disorder (Borderline, Antisocial, Paranoid, etc)',
                                    'Anxiety Disorder (Generalized, Social, Phobia, etc)|Mood Disorder (Depression, Bipolar Disorder, etc)|Attention Deficit Hyperactivity Disorder|Post-traumatic Stress Disorder',
                                    'Anxiety Disorder (Generalized, Social, Phobia, etc)|Mood Disorder (Depression, Bipolar Disorder, etc)|Attention Deficit Hyperactivity Disorder|Stress Response Syndromes',
                                    'Anxiety Disorder (Generalized, Social, Phobia, etc)|Tinnitus']}, value = 0)
data3 = data3.replace(to_replace = {'If maybe what condition(s) do you believe you have?': ['Attention Deficit Hyperactivity Disorder',
                                    'Attention Deficit Hyperactivity Disorder|Mood Disorder (Depression, Bipolar Disorder, etc)',
                                    'Attention Deficit Hyperactivity Disorder|Obsessive-Compulsive Disorder']}, value = 1)  
data3 = data3.replace(to_replace = {'If maybe what condition(s) do you believe you have?': ['Asperger Syndrome',
                                    'Autism']}, value = 2)  
data3 = data3.replace(to_replace = {'If maybe what condition(s) do you believe you have?': 'Eating Disorder (Anorexia, Bulimia, etc)'}, value = 3)                          
data3 = data3.replace(to_replace = {'If maybe what condition(s) do you believe you have?': ['Mood Disorder (Depression, Bipolar Disorder, etc)',
                                    'Mood Disorder (Depression, Bipolar Disorder, etc)|Addictive Disorder',
                                    'Mood Disorder (Depression, Bipolar Disorder, etc)|Anxiety Disorder (Generalized, Social, Phobia, etc)',
                                    'Mood Disorder (Depression, Bipolar Disorder, etc)|Attention Deficit Hyperactivity Disorder',
                                    'Mood Disorder (Depression, Bipolar Disorder, etc)|Attention Deficit Hyperactivity Disorder|Addictive Disorder',
                                    'Mood Disorder (Depression, Bipolar Disorder, etc)|Eating Disorder (Anorexia, Bulimia, etc)',
                                    'Mood Disorder (Depression, Bipolar Disorder, etc)|Eating Disorder (Anorexia, Bulimia, etc)|Attention Deficit Hyperactivity Disorder|Personality Disorder (Borderline, Antisocial, Paranoid, etc)|Stress Response Syndromes',
                                    'Mood Disorder (Depression, Bipolar Disorder, etc)|Obsessive-Compulsive Disorder',
                                    'Mood Disorder (Depression, Bipolar Disorder, etc)|Obsessive-Compulsive Disorder|Stress Response Syndromes|Addictive Disorder',
                                    'Mood Disorder (Depression, Bipolar Disorder, etc)|Personality Disorder (Borderline, Antisocial, Paranoid, etc)',
                                    'Mood Disorder (Depression, Bipolar Disorder, etc)|Personality Disorder (Borderline, Antisocial, Paranoid, etc)|Obsessive-Compulsive Disorder|Substance Use Disorder',
                                    'Mood Disorder (Depression, Bipolar Disorder, etc)|Post-traumatic Stress Disorder|Addictive Disorder',
                                    'Mood Disorder (Depression, Bipolar Disorder, etc)|Psychotic Disorder (Schizophrenia, Schizoaffective, etc)|Attention Deficit Hyperactivity Disorder|Personality Disorder (Borderline, Antisocial, Paranoid, etc)|Post-traumatic Stress Disorder|Dissociative Disorder|Depersonalisation',
                                    'Mood Disorder (Depression, Bipolar Disorder, etc)|Stress Response Syndromes',
                                    ]}, value = 4);
data3 = data3.replace(to_replace = {'If maybe what condition(s) do you believe you have?': ['Obsessive-Compulsive Disorder',
                                    'Obsessive-Compulsive Disorder|Eating Disorder (Anorexia, Bulimia, etc)|Mood Disorder (Depression, Bipolar Disorder, etc)|Anxiety Disorder (Generalized, Social, Phobia, etc)',
                                    'Obsessive-Compulsive Disorder|Substance Use Disorder',
                                    'Obsessive-Compulsive Disorder|Mood Disorder (Depression, Bipolar Disorder, etc)',
                                    'Obsessive-Compulsive Disorder|Personality Disorder (Borderline, Antisocial, Paranoid, etc)|Mood Disorder (Depression, Bipolar Disorder, etc)|Anxiety Disorder (Generalized, Social, Phobia, etc)',
                                    'Obsessive-Compulsive Disorder|Suicidal Ideation']}, value = 5)
data3 = data3.replace(to_replace = {'If maybe what condition(s) do you believe you have?': ['Personality Disorder (Borderline, Antisocial, Paranoid, etc)',
                                    'Personality Disorder (Borderline, Antisocial, Paranoid, etc)|Addictive Disorder'
                                    'Personality Disorder (Borderline, Antisocial, Paranoid, etc)|Mood Disorder (Depression, Bipolar Disorder, etc)',
                                    'Personality Disorder (Borderline, Antisocial, Paranoid, etc)|Mood Disorder (Depression, Bipolar Disorder, etc)|Anxiety Disorder (Generalized, Social, Phobia, etc)',
                                    'Personality Disorder (Borderline, Antisocial, Paranoid, etc)|Substance Use Disorder|Addictive Disorder']}, value = 6)
data3 = data3.replace(to_replace = {'If maybe what condition(s) do you believe you have?': 'Post-traumatic Stress Disorder'}, value = 7)
data3 = data3.replace(to_replace = {'If maybe what condition(s) do you believe you have?': 'Psychotic Disorder (Schizophrenia, Schizoaffective, etc)|Stress Response Syndromes'}, value = 8)
data3 = data3.replace(to_replace = {'If maybe what condition(s) do you believe you have?': ['Addictive Disorder',
                                    'Addictive Disorder|Substance Use Disorder|Obsessive-Compulsive Disorder|Personality Disorder (Borderline, Antisocial, Paranoid, etc)|Mood Disorder (Depression, Bipolar Disorder, etc)',
                                    'Gender Identity Disorder', 
                                    'Personality Disorder (Borderline, Antisocial, Paranoid, etc)|Mood Disorder (Depression, Bipolar Disorder, etc)',
                                    'Personality Disorder (Borderline, Antisocial, Paranoid, etc)|Addictive Disorder',
                                    'Stress Response Syndromes|Substance Use Disorder|Addictive Disorder',
                                    'Substance Use Disorder',
                                    'Substance Use Disorder|Addictive Disorder',
                                    'Substance Use Disorder|Obsessive-Compulsive Disorder',
                                    'depersonalization disorder',
                                    'post-partum / anxiety']}, value = 9)
data3['If maybe what condition(s) do you believe you have?'].fillna(99, inplace = True)
################################################################################################################################

data3 = data3.replace(to_replace = {'If you have a mental health issue do you feel that it interferes with your work when being treated effectively?': 'Never'}, value = 0)
data3 = data3.replace(to_replace = {'If you have a mental health issue do you feel that it interferes with your work when being treated effectively?': 'Rarely'}, value = 1)
data3 = data3.replace(to_replace = {'If you have a mental health issue do you feel that it interferes with your work when being treated effectively?': 'Sometimes'}, value = 2)
data3 = data3.replace(to_replace = {'If you have a mental health issue do you feel that it interferes with your work when being treated effectively?': 'Often'}, value = 3)
data3 = data3.replace(to_replace = {'If you have a mental health issue do you feel that it interferes with your work when being treated effectively?': 'Not applicable to me'}, value = 4)

data3 = data3.replace(to_replace = {'If you have a mental health issue do you feel that it interferes with your work when NOT being treated effectively?': 'Never'}, value = 0)
data3 = data3.replace(to_replace = {'If you have a mental health issue do you feel that it interferes with your work when NOT being treated effectively?': 'Rarely'}, value = 1)
data3 = data3.replace(to_replace = {'If you have a mental health issue do you feel that it interferes with your work when NOT being treated effectively?': 'Sometimes'}, value = 2)
data3 = data3.replace(to_replace = {'If you have a mental health issue do you feel that it interferes with your work when NOT being treated effectively?': 'Often'}, value = 3)
data3 = data3.replace(to_replace = {'If you have a mental health issue do you feel that it interferes with your work when NOT being treated effectively?': 'Not applicable to me'}, value = 4)

data3 = data3.replace(to_replace = {'What is your age?': [17, 18, 19, 20]}, value = 18)
data3 = data3.replace(to_replace = {'What is your age?': [21, 22, 23, 24, 25]}, value = 23)
data3 = data3.replace(to_replace = {'What is your age?': [26, 27, 28, 29, 30]}, value = 28)
data3 = data3.replace(to_replace = {'What is your age?': [31, 32, 33, 34, 35]}, value = 33)
data3 = data3.replace(to_replace = {'What is your age?': [36, 37, 38, 39, 40]}, value = 38)
data3 = data3.replace(to_replace = {'What is your age?': [41, 42, 43, 44, 45]}, value = 43)
data3 = data3.replace(to_replace = {'What is your age?': [46, 47, 48, 49, 50]}, value = 48)
data3 = data3.replace(to_replace = {'What is your age?': [51, 52, 53, 54, 55]}, value = 53)
data3 = data3.replace(to_replace = {'What is your age?': [56, 57, 58, 59, 60]}, value = 58)
data3 = data3.replace(to_replace = {'What is your age?': [61, 62, 63, 64, 65]}, value = 63)
data3 = data3.replace(to_replace = {'What is your age?': [66, 67, 68, 69, 70]}, value = 68)
data3 = data3.replace(to_replace = {'What is your age?': [71, 72, 73, 74, 75]}, value = 73)

data3 = data3.replace(to_replace = {'What is your gender?': ['Male', 'male', 'M', 'm', 'man', 'Man', 'cis man', 'cis male', 'Cis male', 'dude', 'Dude', 'Male ', 'Male (cis)', 'male ', 'Cis Male']}, value = 0)
data3 = data3.replace(to_replace = {'What is your gender?': ['Female', 'female', 'F', 'f', 'woman', 'Woman', 'female/woman', 'cis female', 'cis woman', 'Female ', 'female ', 'fem', ' Female',]}, value = 1)
data3['What is your gender?'].fillna(2, inplace = True)
data3['What is your gender?'].replace(to_replace = (data3['What is your gender?'].unique()[2:].tolist()), value = 2, inplace = True)

data3 = data3.replace(to_replace = {'Do you work remotely?': 'Never'}, value = 0)
data3 = data3.replace(to_replace = {'Do you work remotely?': 'Sometimes'}, value = 1)
data3 = data3.replace(to_replace = {'Do you work remotely?': 'Always'}, value = 2)

#juntar las dos columnas
 # If maybe what condition(s) do you believe you have?
 # If yes what condition(s) have you been diagnosed with?
data3.rename(columns={"If yes what condition(s) have you been diagnosed with?": "label"}, inplace = True)

data3.loc[data3.label == 99, 'label'] = data3.loc[data3.label == 99, "If maybe what condition(s) do you believe you have?"]
data3.loc[data3.label == 99, 'label'] = 10
data3 = data3.drop("If maybe what condition(s) do you believe you have?", axis=1)


#data3.to_csv(r'C:\Users\lucia\OneDrive\Escritorio\resultado_2ej.csv', index=False);
data3.to_csv(r'C:\Users\lcalzado\Desktop\resultado_2ej.csv', index=False);
