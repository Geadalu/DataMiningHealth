# -*- coding: utf-8 -*-
"""
@author: lucia
"""

escribir = []

with open(r"C:\Users\lucia\OneDrive\Escritorio\resultado_2ej.csv", 'r', encoding='iso-8859-1') as f:
#with open(r"C:\Users\lcalzado\Desktop\resultado_2ej.csv", 'r', encoding='iso-8859-1') as f:
    
    #print(f.readline())
    primeraLinea = ''
    for c in f.readline():
        if c != "\"":
            primeraLinea += c
    
    escribir.append(primeraLinea)
    
    for line in f.readlines():
        escribir.append(line)

    escribir[0] = escribir[0].replace('Has your employer ever formally discussed mental health (for example, as part of a wellness campaign or other official communication)?', 
            'Has your employer ever formally discussed mental health?')
    
    escribir[0] = escribir[0].replace('If a mental health issue prompted you to request a medical leave from work, asking for that leave would be:',
            'If a mental health issue prompted you to request a medical leave from work asking for that leave would be:')
    
    escribir[0] = escribir[0].replace('If you have a mental health issue, do you feel that it interferes with your work when being treated effectively?',
            'If you have a mental health issue do you feel that it interferes with your work when being treated effectively?')
    
    escribir[0] = escribir[0].replace('If you have a mental health issue, do you feel that it interferes with your work when NOT being treated effectively?',
            'If you have a mental health issue do you feel that it interferes with your work when NOT being treated effectively?')
     
    escribir[0] = escribir[0].replace('If yes, what condition(s) have you been diagnosed with?', 'If yes what condition(s) have you been diagnosed with?')
    
    escribir[0] = escribir[0].replace('If maybe, what condition(s) do you believe you have?', 'If maybe what condition(s) do you believe you have?')
    
    



with open(r"C:\Users\lucia\OneDrive\Escritorio\resultado_2ej.csv", 'w+', encoding='iso-8859-1') as f:
#+with open(r"C:\Users\lcalzado\Desktop\resultado_2ej.csv", 'w+', encoding='iso-8859-1') as f:
    for x in escribir:
        f.write(x)