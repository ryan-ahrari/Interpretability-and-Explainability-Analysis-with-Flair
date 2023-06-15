paper_analyses = [
    r'C:\Users\ryana\OneDrive\Documents\GitHub\Interpretability-and-Explainability-Analysis-with-Flair\code\Paper_1_output.txt',
    r'C:\Users\ryana\OneDrive\Documents\GitHub\Interpretability-and-Explainability-Analysis-with-Flair\code\Paper_2_output.txt',
    r'C:\Users\ryana\OneDrive\Documents\GitHub\Interpretability-and-Explainability-Analysis-with-Flair\code\Paper_3_output.txt',
    r'C:\Users\ryana\OneDrive\Documents\GitHub\Interpretability-and-Explainability-Analysis-with-Flair\code\Paper_4_output.txt',
    r'C:\Users\ryana\OneDrive\Documents\GitHub\Interpretability-and-Explainability-Analysis-with-Flair\code\Paper_5_output.txt',
    r'C:\Users\ryana\OneDrive\Documents\GitHub\Interpretability-and-Explainability-Analysis-with-Flair\code\Paper_6_output.txt',
    r'C:\Users\ryana\OneDrive\Documents\GitHub\Interpretability-and-Explainability-Analysis-with-Flair\code\Paper_7_output.txt',
    r'C:\Users\ryana\OneDrive\Documents\GitHub\Interpretability-and-Explainability-Analysis-with-Flair\code\Paper_8_output.txt',
    r'C:\Users\ryana\OneDrive\Documents\GitHub\Interpretability-and-Explainability-Analysis-with-Flair\code\Paper_9_output.txt',
    r'C:\Users\ryana\OneDrive\Documents\GitHub\Interpretability-and-Explainability-Analysis-with-Flair\code\Paper_10_output.txt',
]

for paper in paper_analyses:
    fr = open(paper, "r", encoding='utf-8')
    lines = fr.readlines()
    score = 0.0
    for line in lines:
        line = line[:-1]
        line = line.split()
        line[-1] = line[-1].replace('(', '')
        line[-1] = line[-1].replace(')', '')
        if 'POSITIVE' in line:
            score += float(line[-1])
        if 'NEGATIVE' in line:
            score -= float(line[-1])
    print('Score: '+str(score)+' number of lines '+str(len(lines)))