# Cross-lingual-LLM-gender-bias


Requirements to go from WinoBias dataset to tsv file for NLPScholar evaluation:
- Merge the 8 testing files together into one dataset, labeling each row with type1 / type2 and and pro/anti steryotype depending on the file it came from.
- Generate ROI column by detecting which word index contains the second set of brackets.
- Remove all brackets from the sentences.


How to go from NLPScholar output to graphs / charts:
- We will make a chart in LaTeX with the average difference between expected and unexpected predictions for each model (as returned by analyze in NLPScholar)
- We will graph the individual differences from the by_pair output file using a histogram for each model to see the distribution of bias between models.
