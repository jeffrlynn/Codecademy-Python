#take the duplicates out of a list

def remove_duplicates(inputlist):
    if inputlist == []:
        return [] 
    inputlist = sorted(inputlist)
    outputlist = [inputlist[0]]
    for i in inputlist:
        if i > outputlist[-1]:
            outputlist.append(i) 
    return outputlist

#-------------- or -----------------

#def remove_duplicates(inputlist):
#  if inputlist == []:
#    return []
#  outputlist = []
#  for number in inputlist:
#    if number in outputlist:
#      continue
#    else:
#      outputlist.append(number)
#  return outputlist
