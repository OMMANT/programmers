def solution(priorities, location):
    indices = list(range(len(priorities)))
    for i in range(len(priorities) - 1):
        # Find max index
        max_index = priorities.index(max(priorities))
        if indices[max_index + i] == location:
            return i + 1
        else:
            indices = indices[:i] + indices[max_index + i] + indices[max_index + 1:] + indices[:max_index]
            priorities = priorities[max_index + 1: ] + priorities[:max_index]
