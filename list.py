a = [1, 2, 3]
print(a[1])

# 수열 만들기
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list(range(0, 10, 2))

# 연습문제 7. 리스트의 평균 구하기
# nums = [1, 2, 3, 4, 5]
nums = list(range(1,6))
print(len(nums))
sum_nums = (nums[4]+nums[3]+nums[2]+nums[1]+nums[0])
average = sum_nums / len(nums)
print(average)


# 리스트에 요소 추가하기
num_list = [1, 2, 3, 4, 5]
num_list.append(1212)
print(num_list)

num_list.remove(1212)
print(num_list)

