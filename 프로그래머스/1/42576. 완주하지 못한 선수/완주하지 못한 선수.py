def solution(participant, completion):
    participant_people = dict()
    completion_people = dict()
        
    for people in completion:
        completion_people.setdefault(people, 0)
        completion_people[people] += 1
    
    for people in participant:
        completion_people.setdefault(people, 0)
        if not completion_people[people]:
            return people
    
    for people in participant:
        participant_people.setdefault(people, 0)
        participant_people[people] += 1

    for people in participant:
        if participant_people[people] != completion_people[people]:
            return people
