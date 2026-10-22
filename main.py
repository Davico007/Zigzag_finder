# this code checks for the presence of zigzag(s) in an array

# numbers=[1,2,3]
result=[]
def solution(numbers):
    for i in range(0, len(numbers) -2):
        # print(numbers[i+2])
        if (numbers[i]>numbers[i+1] and numbers[i+1]<numbers[i+2]) or (numbers[i]<numbers[i+1] and numbers[i+1]>numbers[i+2]):
            result.append(1)
            # print(result)
        else:
            result.append(0)
            # print(result)
    # print(result)
    numbers = result
    return numbers

array= input("enter the numbers in your array. Separate numbers with comma (e.g 1,2,3): \n")
array = array.split(",")
# print(array)
print(solution(array))
# print(solution(numbers))