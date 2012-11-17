import codecs

def clean_txt():
  f_add = '/Users/yifanwu/Dropbox/Dev/harvardfmlanalysis/data/fml_text.txt'
  f_out_add = '/Users/yifanwu/Dropbox/Dev/harvardfmlanalysis/data/fml_cleaned_text.txt'
  f_w = codecs.open(f_out_add,'w+', "utf-8")
  for i, line in enumerate(codecs.open(f_add, 'r',"utf-8")):
    if i % 2 == 1:
      #this is to get rid of the quotation marks at first
      line = line[2:]
      print line
      #line = line.encode('utf-8')
      f_w.write(line)

clean_txt()
