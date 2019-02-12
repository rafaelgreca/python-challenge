#
# github.com/rafaelgreca
# Copyright © Rafael Greca Vieira
#

#decode the string and returns the final result
def decodeString(string):
    answer = ''
    for i in string:
        if i in 'abcdefghijklmnopqrstuvwxyz':
            value = ord(i) + 2
            
            if value > 122:
                value = (value - 122) + 96
            
            answer += chr(value)
        else:
            answer += i
    return answer

print(decodeString('map'))