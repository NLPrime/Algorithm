def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i == j:
                continue
            if answer.count(numbers[i] + numbers[j]) == 0:
                answer.append(numbers[i] + numbers[j])
    answer.sort()
    return answer