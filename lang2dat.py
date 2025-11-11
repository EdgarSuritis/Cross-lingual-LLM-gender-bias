import csv

langFiles = ['../mt_gender/translations/google/en-de.txt', 
'../mt_gender/translations/google/en-nl.txt', 
'../mt_gender/translations/google/en-it.txt',
'../mt_gender/translations/google/en-es.txt',
'../mt_gender/translations/google/en-ru.txt',
'../mt_gender/translations/google/en-he.txt'
]
biasStart = 1583

outFiles = ['../Cross-lingual-LLM-gender-bias/biasedTranslations/bias-de.tsv',
 '../Cross-lingual-LLM-gender-bias/unbiasedTranslations/unbias-nl.tsv',
 '../Cross-lingual-LLM-gender-bias/unbiasedTranslations/unbias-it.tsv',
 '../Cross-lingual-LLM-gender-bias/unbiasedTranslations/unbias-es.tsv',
 '../Cross-lingual-LLM-gender-bias/unbiasedTranslations/unbias-ru.tsv',
 '../Cross-lingual-LLM-gender-bias/unbiasedTranslations/unbias-he.tsv'
 ]


for i in range(len(langFiles)):
    toPrint= []

    with open(langFiles[i], 'r') as inFile:
        lines = inFile.readlines()
        for idx, line in enumerate(lines):
            if idx > biasStart:
                continue
            line = line.split('|||')
            toPrint.append(line[1].strip('\n').strip())
            #print(line)

    with open(outFiles[i], 'w') as outFile:
        writer = csv.writer(outFile, delimiter = '\t')
        writer.writerow(['text'])
        for line in toPrint:
            writer.writerow([line])
            #print(line)