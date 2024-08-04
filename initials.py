# initials
def run():

  # ask name, split into list
  while True:
    is_invalid = False

    full_name = input('Please enter your full name: ')
  
    for i in range(0,len(full_name)):
      if full_name[i:i+1].isdigit():
        is_invalid = True

    if is_invalid:  #  if there is a digit
      print('please enter a valid name (no numbers)')
      continue
    break

  # split name into list
  names = full_name.split(' ')

  # cap initials and append
  initials = []
  for name in names:
    initials.append(name[0].upper())
    initials.append(". ")

  # display
  print(''.join(initials))
