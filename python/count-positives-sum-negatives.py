def count_positives_sum_negatives(arr):
    # if arr == []:
        # return [0,0]
    # else:
    count = int()
    sum_negative = int()
    for i in arr:
        if i > 0:
            count += 1
        elif i < 0:
            sum_negative += i
    return [count, sum_negative]

print(count_positives_sum_negatives([1,2,3,-1,-2,-3]))
print(count_positives_sum_negatives([0,0]))
print(count_positives_sum_negatives([1,2,3,0,-1,-2,-3]))
print(count_positives_sum_negatives([1,0]))
print(count_positives_sum_negatives([0,1]))
print(count_positives_sum_negatives([]))
print(count_positives_sum_negatives([0,0,0,0,0,0,0,0,0]))