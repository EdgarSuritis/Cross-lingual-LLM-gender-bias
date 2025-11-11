import csv

langFiles = ['../mt_gender/translations/google/en-de.txt', 
'../mt_gender/translations/google/en-nl.txt', 
'../mt_gender/translations/google/en-it.txt',
'../mt_gender/translations/google/en-es.txt',
'../mt_gender/translations/google/en-ru.txt',
'../mt_gender/translations/google/en-he.txt'
]
biasStart = 1584

outFiles = ['../Cross-lingual-LLM-gender-bias/biasedTranslations/bias-de.txt',
 '../Cross-lingual-LLM-gender-bias/biasedTranslations/bias-nl.txt',
 '../Cross-lingual-LLM-gender-bias/biasedTranslations/bias-it.txt',
 '../Cross-lingual-LLM-gender-bias/biasedTranslations/bias-es.txt',
 '../Cross-lingual-LLM-gender-bias/biasedTranslations/bias-ru.txt',
 '../Cross-lingual-LLM-gender-bias/biasedTranslations/bias-he.txt'
 ]


for i in range(len(langFiles)):
    toPrint= []

    with open(langFiles[i], 'r') as inFile:
        lines = inFile.readlines()
        for idx, line in enumerate(lines):
            if idx < biasStart:
                continue
            line = line.split('|||')
            toPrint.append(line[1])

    with open(outFiles[i], 'w') as outFile:
        idx = 1
        for line in toPrint:
            string = str(idx)+line
            outFile.write(string)
            idx +=1 