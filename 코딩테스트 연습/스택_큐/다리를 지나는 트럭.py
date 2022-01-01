def solution(bridge_length, weight, truck_weights):
    elapsed_t, passed_truck, passing, index, current_weight, n_truck = 0, 0, [0] * bridge_length, 0, 0, len(truck_weights)

    while passed_truck < n_truck:
        passed = passing.pop()
        passing = [0] + passing
        current_weight -= passed
        if passed != 0: passed_truck += 1
        # 다리를 건너야하는 트럭이 남아있고 다리 하중이 충분하면
        if index < n_truck and current_weight + truck_weights[index] <= weight:
            current_weight += truck_weights[index]
            passing[0] = truck_weights[index]
            index += 1
        elapsed_t += 1
        
    return elapsed_t

if __name__ == '__main__':
    bridge_lengths = [2, 100, 100]
    weights = [10, 100, 100]
    truck_weightss = [[7, 4, 5, 6], [10], [10]*10]

    for bridge_length, weight, truck_weights in zip(bridge_lengths, weights, truck_weightss):
        print(solution(bridge_length, weight, truck_weights))