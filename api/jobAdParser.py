
def convert_txt_to_text(path):
    content = open(path).read().split()
    return content


def checkSkillGroups(word):

    team = {'team', 'teamwork', 'teams', 'group', 'groups', 'groupwork',
            'conflict management', 'managing conflict', 'feedback'}
    listening = {'empathy', 'listening', 'listen', 'active listening',
                 'listening actively', 'empathetic listening', "point of view", 'understanding others'}
    technical_creation = {'writing skill', 'writing ability', 'technical writing', 'technical document', 'presentation', 'drafting documents',
                          'creating presentations', 'memo writing', 'memo creation', 'creating reports', 'drafting emails', 'email drafting'}
    personableness = {'relationships', 'engaging', 'small talk', 'rapport',
                      'impromptu speaking', 'body language', 'small talk', 'working in diverse group'}
    oral_communication = {'oral communication', 'public speaking', 'speaking public', 'orally communicating',
                          'verbal communication', 'verbal skill', 'respect', 'confidence', 'friendliness', 'friendly'}
    negotiation = {'negotiation', 'persuasion', 'infleunce'}
    planning = {'planning', 'structuring', 'structure',
                'organizing', 'organize', 'arrange', 'arranging'}

    if word in team:
        return "teams"
    elif word in listening:
        return "listening"
    elif word in technical_creation:
        return "technical creation"
    elif word in personableness:
        return "personableness"
    elif word in oral_communication:
        return "oral communication"
    elif word in negotiation:
        return "negotiation"
    elif word in planning:
        return "planning"


def parseJobAd(jobAdFileAsString):
    allSkills = list(map(lambda word: word.lower() if len(
        word) > 2 else None, jobAdFileAsString.split()))
    jobAdWords = set(allSkills)
    skillsSet = {'team', 'teamwork', 'teams', 'group', 'groups', 'groupwork', 'conflict management', 'managing conflict', 'feedback',
                 'empathy', 'listening', 'listen', 'active listening', 'listening actively', 'empathetic listening', "point of view", 'understanding others',
                 'writing skill', 'writing ability', 'technical writing', 'technical document', 'presentation', 'drafting documents', 'creating presentations',
                 'memo writing', 'memo creation', 'creating reports', 'drafting emails', 'email drafting', 'relationships', 'engaging', 'small talk', 'rapport',
                 'impromptu speaking', 'body language', 'small talk', 'working in diverse group', 'oral communication', 'public speaking', 'speaking public',
                 'orally communicating', 'verbal communication', 'verbal skill', 'respect', 'confidence', 'friendliness', 'friendly', 'negotiation', 'persuasion',
                 'infleunce', 'planning', 'structuring', 'structure', 'organizing', 'organize', 'arrange', 'arranging'}
    dict_ = {}

    individualSkillsCount = 0
    jobAdWords = []
    for skill in skillsSet:
        count = jobAdFileAsString.count(skill)
        if count > 0:
            individualSkillsCount += count
            jobAdWords.append(skill)

            skillGroup = checkSkillGroups(skill)
            if skillGroup in dict_.keys():
                dict_[skillGroup] += count
            else:
                dict_[skillGroup] = count
    
    print('Job Ad Words: ', jobAdWords)

    sortedDict = sorted(dict_.items(), key=lambda x: x[1], reverse=True)
    print("# of Times Each Skill Is Mentioned in Job Ad:", sortedDict)

    return sortedDict


if __name__ == "__main__":
    print("Input your job ad below")
    jobAdFileAsString = str(input())
    parseJobAd(jobAdFileAsString)
