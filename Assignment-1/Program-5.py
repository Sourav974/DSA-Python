# 5. Write a program to find the frequency of a character in a string.

input_string = input("Enter the String only!! ")
freq = {}

for i in input_string:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
print("frquencies of all characters is: ", str(freq))



