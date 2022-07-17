"""
This module contains all functions invoked by the backend API.
"""

from api import datasetParser
from api import jobAdParser

#import datasetParser
#import jobAdParser

def calculateScore(keyword, scoreMetric, resumeFile, factor=0.25):
    datasetResults = datasetParser.parseDataset(keyword)
    resumeResults = jobAdParser.parseJobAd(resumeFile)

    print(datasetResults)
    print(resumeResults)

    neededSkills = [val[0] for val in datasetResults]
    totalNeededSkills = len(neededSkills)
    currentSkills = [val[0] for val in resumeResults]

    print('Needed Skills:', neededSkills)
    print('Current Skills:', currentSkills)

    # Calculate the number of skills the user mentions
    count = 0
    for skill in neededSkills:
        if skill in currentSkills:
            count += 1

    # scoreMetric = 0: base technique
    # scoreMetric = 1: adjust based on missing skills
    if (scoreMetric):
        for skill in neededSkills:
            if skill not in currentSkills:
                count -= factor
        count = max(count, 0)

    print(count)
    print(totalNeededSkills)
    return count / totalNeededSkills * 100 if totalNeededSkills != 0 else 0


if __name__ == "__main__":
    score = calculateScore("Computer Hardware Engineer", 1)
    print(score)
