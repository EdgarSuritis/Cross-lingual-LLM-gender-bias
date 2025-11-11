import csv

langFiles = ['../mt_gender/data/aggregates/en_anti.txt'
]

outFiles = ['../Cross-lingual-LLM-gender-bias/unbiasedTranslations/unbias-en.tsv'
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
        writer = csv.writer(outFile, delimiter = '\t')
        writer.writerow(['text'])
        for line in toPrint:
            writer.writerow([line])