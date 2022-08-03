import re

file = open("/Users/dongliwen/Projects/py4e/c3_w1/regex_sum_1605940.txt").read()

number_list = re.findall(r'[0-9]+', file)
sum = 0
for number in number_list:
    sum += int(number)
print(sum)