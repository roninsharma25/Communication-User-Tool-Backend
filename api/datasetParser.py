"""

Takes an input job field and returns the top communication skills required for that job field.

"""

import pandas as pd
import numpy as np

jobAdDataset = "merged_data_final.csv"
commSkillsMapping = "coded_list_items.csv"


def detectSkills(phrase, skillFields):
    skills = [i for i in skillFields if isinstance(i, str)]

    # ADD MORE CASES IF NEEDED
    if 'team' in phrase or 'teamwork' in phrase or 'teams' in phrase or 'group' in phrase or 'groups' in phrase or 'groupwork' in phrase or 'conflict management' in phrase or 'managing conflict' in phrase or 'feedback' in phrase:
        skills += ['teams']
    if 'empathy' in phrase or 'listening' in phrase or 'active listening' in phrase or 'listening actively' in phrase or 'empathetic listening' in phrase or "point of view" in phrase or 'understanding others' in phrase:
        skills += ['listening']
    if 'writing' in phrase or 'writing skill' in phrase or 'writing ability' in phrase or 'technical writing' in phrase or 'technical document' in phrase or 'presentation' in phrase or 'drafting documents' in phrase or 'creating presentations' in phrase or 'memo writing' in phrase or 'memo creation' in phrase or 'creating reports' in phrase or 'drafting emails' in phrase or 'email drafting' in phrase:
        skills += ['technical creation']
    if 'relationships' in phrase or 'engaging' in phrase or 'small talk' in phrase or 'rapport' in phrase or 'impromptu speaking' in phrase or 'body language' in phrase or 'small talk' in phrase or 'working in diverse group' in phrase:
        skills += ['personableness']
    # if 'oral communication' in phrase or 'public speaking' in phrase or 'speaking public' in phrase or 'orally communicating' in phrase or 'verbal communication' in phrase or 'verbal skill' in phrase or 'respect' in phrase or 'confidence' in phrase or 'friendliness' in phrase or 'friendly' in phrase:
    #     skills += ['oral communication']
    if 'negotiation' in phrase or 'persuasion' in phrase or 'infleunce' in phrase:
        skills += ['negotiation']
    if 'planning' in phrase or 'structuring' in phrase or 'structure' in phrase or 'organizing' in phrase or 'organize' in phrase or 'arrange' in phrase or 'arranging' in phrase:
        skills += ['planning']

    return list(set(skills))


def parseDataset(keyword):
    # if len(sys.argv) > 1:
    #     keyword = sys.argv[1]
    # else:
    #     keyword = "Software Engineer"
    df = pd.read_csv("data/" + jobAdDataset)
    df = df[df["Keyword"] == keyword]
    df2 = pd.read_csv("data/" + commSkillsMapping)
    allSkills = []

    for des in df["Description"].to_numpy():
        des = des.lower()
        for row in df2.to_numpy():
            phrase = row[2].lower()
            if phrase in des:
                skillFields = np.array(row[-4:])
                skills = detectSkills(phrase, skillFields)
                allSkills += skills

    dict_ = dict((val, allSkills.count(val))
                 for val in set(allSkills) if val != "complicated!")
    sortedDict = sorted(dict_.items(), key=lambda x: x[1], reverse=True)
    print("Important Skills For", keyword+"s", "Are:", sortedDict)

    return sortedDict


if __name__ == "__main__":
    print("Input your job field below")
    jobFieldAsString = str(input())
    parseDataset(jobFieldAsString)
