import math


def max_binary_gap(N):
    binary_string = bin(N)
    max_count = 0
    count = 0
    for b in binary_string[2:]:
        if b == '0':
            count += 1
        elif b == '1':
            if count > max_count:
                max_count = count
            count = 0
    return max_count


def cyclic_rotation(array, R):
    l = len(array)
    if l == 0 or R == 0:
        return array
    offset = R % l
    new_list = array[l - offset:]
    new_list.extend(array[:l - offset])
    return new_list


def odd_occurence(array):  # XOR trick: XOR binary number representations; all bits will be zero except for 1s in the odd number
    result = 0
    for element in array:
        result = result ^ element
    return result


def jumping(start, goal, distance):
    return math.ceil((goal - start) / distance)


def element_in_sequence_missing(list):  # SUM trick: don't search, sum and find the missing element
    return sum(range(len(list) + 2)) - sum(list)


def minimal_partition(list):  # there are multiple minimums
    total = sum(list)
    left_sum = list[0]
    min_diff = abs(left_sum - (total - left_sum))
    for element in list[1:-1]:
        left_sum += element
        diff = abs(left_sum - (total - left_sum))
        if diff <= min_diff:
            min_diff = diff
    return min_diff


def earliest_unique_elements(list, max):  # count and remember how many uniques you've already seen
    uniques = {}
    for x in range(max+1):
        uniques[x] = True
    for count in range(len(list)):
        number = list[count]
        if uniques.get(number):
            uniques[number] = False
            max -= 1
            if max == 0:
                return count
    return -1

def is_permutation(list):  # check the negative condition
    uniques = {}
    for i in range(1,len(list)+1):
        uniques[i] = True
    for n in list:
        if uniques.get(n):
            uniques[n] = False
        else:
            return 0
    return 1


def find_last_max_command(max, list):
    for i in range(-1, -1 * len(list)):
        if list[i] > max:
            return len(list) - i


def increase_by_one_or_max_counters(max, list):
    index = find_last_max_command(max, list)

