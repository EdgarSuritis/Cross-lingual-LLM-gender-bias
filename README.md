# Cross-lingual-LLM-gender-bias


Requirements to go from WinoBias dataset to tsv file for NLPScholar evaluation.
- Merge the 8 testing files together into one dataset, labeling each row with type1 / type2 and and pro/anti steryotype depending on the file it came from.
- Generate ROI column by detecting which word index contains the second set of brackets.
- Remove all brackets from the sentences.
