import csv

langFiles = ['../mt_gender/translations/google/en-de.txt', 
'../mt_gender/translations/google/en-nl.txt', 
'../mt_gender/translations/google/en-it.txt',
'../mt_gender/translations/google/en-es.txt',
'../mt_gender/translations/google/en-ru.txt',
'../mt_gender/translations/google/en-he.txt'
]
biasStart = 1583

outFiles = ['../Cross-lingual-LLM-gender-bias/biasedTranslations/bias-de.txt',
 '../Cross-lingual-LLM-gender-bias/unbiasedTranslations/unbias-nl.txt',
 '../Cross-lingual-LLM-gender-bias/unbiasedTranslations/unbias-it.txt',
 '../Cross-lingual-LLM-gender-bias/unbiasedTranslations/unbias-es.txt',
 '../Cross-lingual-LLM-gender-bias/unbiasedTranslations/unbias-ru.txt',
 '../Cross-lingual-LLM-gender-bias/unbiasedTranslations/unbias-he.txt'
 ]


for i in range(len(langFiles)):
    toPrint= []

    with open(langFiles[i], 'r') as inFile:
        lines = inFile.readlines()
        for idx, line in enumerate(lines):
            if idx > biasStart:
                continue
            line = line.split('|||')
            toPrint.append(line[1])
            print(line[0])

    with open(outFiles[i], 'w') as outFile:
        idx = 1
        for line in toPrint:
            string = str(idx)+line + '\n'
            outFile.write(string)
            idx +=1 