def solution(participant, completion):
    participant.sort()
    completion.sort()
    
    for p, c in zip(participant, completion):
        if p != c:
            return p
    return participant[-1]

if __name__ == '__main__':
    participants = [
        ["leo", "kiki", "eden"],
        ["marina", "josipa", "nikola", "vinko", "filipa"],
        ["mislav", "stanko", "mislav", "ana"]
    ]
    completions = [
        ["eden", "kiki"],
        ["josipa", "filipa", "marina", "nikola"],
        ["stanko", "ana", "mislav"]
    ]

    for participant, completion in zip(participants, completions):
        print(solution(participant, completion))