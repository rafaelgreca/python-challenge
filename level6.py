#
# github.com/rafaelgreca
# Copyright © Rafael Greca Vieira
#

import re
import zipfile

def returnNothing(file_data):
    new_nothing = re.search(r'\d\d+', str(file_data))
    return new_nothing.group()

def returnComment(nothing, end_file, zip):
    info = zip.getinfo(nothing + end_file)
    return eval(str(info.comment)).decode()

zip = zipfile.ZipFile('Channel/channel.zip')
nothing = '90052'
end_file = '.txt'
comment = []

for i in range(908):
    
    file_data = zip.read(nothing + end_file)
    comment.append(returnComment(nothing, end_file, zip))
    nothing = returnNothing(file_data)

print("".join(comment))