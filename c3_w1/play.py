s = 'abcbcd' # String we are working with

prev_str = ''
current_str = ''

#outer loop to iterate through the string
for i in range(len(s)):
    current_str = s[i]
    
    #inner loop to compare if the next character is still in alphabetical order
    for j in range(len(s)):
        if i + j + 1 < len(s) and s[i+j] <= s[i+j+1]:
            current_str += s[i+j+1]
        else:
            break
    
    #if we have a new longest string, update the longest string
    if len(current_str) > len(prev_str):
        prev_str = current_str
           
print(prev_str)



