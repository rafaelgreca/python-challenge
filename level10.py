#
# github.com/rafaelgreca
# Copyright © Rafael Greca Vieira
#

def look_and_say(size):
    
    string = '1'

    if size == 0:
        print("0")
        exit()
    
    for k in range(size):

        j = 0
        var_aux = 0
        string_aux = ''

        while j < len(string):
            count = 0

            while var_aux < len(string) and string[j] == string[var_aux]:
                count += 1
                var_aux += 1
            
            string_aux += str(count) + string[j]

            j = var_aux

        string = string_aux
    
    print(len(string))

look_and_say(30)