from time import sleep
while True:
  start = input('Type c for collection or a for analysis: \n')
  if start == 'c' or start == 'C':
    import collection
  if start == 'a' or start == 'A':
    import extraCells
  if start != 'c' or start != 'a' or start != 'C' or start != 'A':
    print('Try again\n')
time.sleep(5)