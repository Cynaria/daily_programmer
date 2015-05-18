def name_game(name):
  name = name.replace(name[-1], "")
  starting_letter = name[0]
  ending = name.replace(name[0], "", 1)
  output_rhyme(name, starting_letter, ending)

def output_rhyme(name, starting_letter, ending):
  print b_line(name, ending, starting_letter)
  print f_line(name, ending, starting_letter)
  print m_line(name, ending, starting_letter)
  print end_line(name)

def b_line(name, ending, starting_letter):
  if (starting_letter == 'B'):
    return "%(name)s, %(name)s bo-%(ending)s " %locals()
  else:
    return "%(name)s, %(name)s bo-b%(ending)s" %locals()

def f_line(name, ending, starting_letter):
  if (starting_letter == 'F'):
    return "Bonana fanna fo-%(ending)s" %locals()
  else:
    return "Bonana fanna fo-F%(ending)s " %locals()

def m_line(name, ending, starting_letter):
  if (starting_letter == 'M'):
    return "Fee fy mo-%(ending)s," %locals()
  else:
    return "Fee fy mo-m%(ending)s," %locals()

def end_line(name):
  return "%(name)s!" %locals()

name_game("Beth!")
name_game("Lincoln!")
