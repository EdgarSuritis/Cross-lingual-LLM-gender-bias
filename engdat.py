import csv

langFiles = ['../mt_gender/data/aggregates/en_pro.txt'
]

outFiles = ['../Cross-lingual-LLM-gender-bias/biasedTranslations/bias-en.txt'
]

for i in range(len(langFiles)):
    toPrint = []
    with open(langFiles[i], 'r') as inFile:
        lines = inFile.readlines()
        for line in lines:
            strings = line.split("\t")
            print(strings)
            toPrint.append(strings[2])

    with open(outFiles[i], 'w') as outFile:
        idx = 1
        for line in toPrint:
            string = str(idx)+ ' ' +line + '\n'
            outFile.write(string)
            idx +=1 