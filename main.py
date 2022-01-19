numbers = [2,5,5,5,45,67,87,55,65,65,78,963,3,3,4,5,6,7,7]
count_pair = 0
i=0
while i <  len(numbers)-1:
    if numbers[1]==numbers[i+1]:
        count_pair+=1
        i+=2
    else:
        i+=1
print(count_pair)