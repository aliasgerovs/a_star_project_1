import heapq  # import heapq module for heap data structure
from math import ceil  # import ceil function from math module
import sys  # import sys module for sys.maxsize
from statistics import mean  # import mean function from statistics module

def read_input_file(file_path):
    with open(file_path) as f:
        my_tuple = tuple(map(int, f.readline().strip().split(',')))  # read the first line from the file, strip any leading/trailing white spaces, split it by comma and map the resulting string to integers, and then create a tuple from the resulting sequence of integers
        target_quantity = int(f.readline())  # read the second line from the file and convert it to an integer
        capacities = (sys.maxsize,) + my_tuple  # create a new tuple by concatenating sys.maxsize with the previous tuple
    return capacities, target_quantity  # return the new tuple and target_quantity as a tuple

def initial_state(capacities):
    return (0,) * len(capacities)  # create a tuple of zeros with the same length as the capacities tuple and return it as the initial state

def heuristic(state, capacities, target_quantity):
    # If the target quantity has already been achieved, the heuristic value is zero
    if target_quantity == state[0]:
        return 0

    # Check if the sum of the quantities in the state tuple matches the target quantity
    # If it does, return a small positive value as the heuristic
    # This ensures that a solution is found as soon as the target quantity is reached
    j = 1
    while j < len(capacities):
        if target_quantity == state[0] + state[j]:
            return 1 / target_quantity
        else:
            j += 1
    
    # Calculate the actual distance and next distance from the current state to the target quantity
    total_distance_actual = target_quantity
    total_distance_next = target_quantity
    # If the target quantity is greater than the sum of the first element in the state tuple and the maximum capacity in capacities, 
    # calculate the actual and next distances to the target quantity
    if target_quantity > state[0] + max(state[1:]):
        total_distance_actual = (target_quantity - state[0])
        total_distance_next = (target_quantity - state[0] - max(state[1:]))
        
    # If the target quantity is greater than the first element in the state tuple and less than the sum of the first element 
    # and the maximum capacity in capacities, calculate the actual and next distances to the target quantity
    if state[0] < target_quantity and state[0] + max(state[1:]) > target_quantity and  state[0] + max(state[1:]) - max(capacities[1:]) < target_quantity:
        total_distance_actual = (target_quantity - state[0])
        total_distance_next = abs(target_quantity - state[0] - max(state[1:]))
    
    # Check all possible combinations of adding the maximum capacity to the state tuple and add it to the first element
    # to see if the resulting sum matches the target quantity
    # If it does, return a heuristic value based on the distance to the target quantity
    for i in range(len(capacities)):
        if target_quantity == max(state[1:]) + state[0] + capacities[i]:
            return ((total_distance_actual + total_distance_next) / 2) / target_quantity

    # If the target quantity is not achieved using the above conditions, return a heuristic value based on the distance 
    # to the target quantity
    return (total_distance_actual + total_distance_next) / target_quantity

def next_states(state, capacities):
    states = []    
    for i, amount in enumerate(state):
        # Skip the first element in the tuple, as it represents the total amount in the state
        if i == 0:
            continue
        # Create a new state tuple with the current element emptied
        new_state_empty = list(state)
        new_state_empty[i] = 0
        states.append(new_state_empty)    
        # Create new state tuples by transferring water from the current element to other elements
        for j, c in enumerate(state):
            # Skip transferring water to the same element, as it will not result in a new state tuple
            if i == j:
                continue          
            # If the current element is empty, fill it up to its maximum capacity from the other element
            if amount == 0:
                new_state = list(state)
                new_state[i] += capacities[i]
                states.append(new_state)
            # If the other element has enough capacity to receive water from the current element,
            # transfer water from the current element to the other element
            elif amount >= capacities[j] - state[j] and capacities[j] - state[j] >= 0:
                new_state = list(state)
                new_state[i] = amount - (capacities[j] - state[j])
                new_state[j] = new_state[j] + (capacities[j] - state[j])
                states.append(new_state)
            # If the other element does not have enough capacity to receive all the water from the current element,
            # transfer as much water as possible from the current element to the other element
            elif amount < capacities[j] - state[j]:
                new_state = list(state)
                new_state[i] = 0
                new_state[j] = new_state[j] + amount
                states.append(new_state)

    return states

def a_star(capacities, target_quantity): 
    start_state = initial_state(capacities)
    frontier = [(heuristic(start_state, capacities, target_quantity), 0, start_state)]
    explored = set()
    while frontier:
        tc, cost_so_far, current_state = heapq.heappop(frontier)
        if current_state[0] > target_quantity:
            continue
        if str(current_state) in explored:
            continue

        if current_state[0] == target_quantity:
            return cost_so_far
        
        while frontier :
            x, y, z = heapq.heappop(frontier)

        explored.add(str(current_state))
        for next_state in next_states(current_state, capacities):                
            next_cost = cost_so_far + 1 
            total_cost = next_cost + heuristic(next_state, capacities, target_quantity)
            heapq.heappush(frontier, (total_cost, next_cost, next_state))
        
        if current_state[0] > target_quantity+2*max(capacities[1:]):
            return -1
    return -1


if __name__ == '__main__':
    capacities, target_quantity = read_input_file('C:/Users/aliasgarov/Desktop/input.txt')
    steps = a_star(capacities, target_quantity)
    print(steps)
