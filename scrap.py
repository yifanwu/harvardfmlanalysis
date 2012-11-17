def parseLine():
  for line in str(text):
    cleaned = str(line)[48:-13]
    if cleaned is "":      
      print "ERROR!!! String empty, detected line is:"
      print line
      return
    print cleaned+","
  