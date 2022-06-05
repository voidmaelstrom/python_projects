def hello():
  print("Hello!")

def pack(item1, item2, item3):
  return [item1, item2, item3]

def create_list():
    ''' Function to return list '''
    your_list = []
    for i in range(10):
        your_list.append(i)
    return your_list

def eat_lunch(my_lst):
  if len(my_lst) == 0:
    print("My lunchbox is empty!")
  else:
    for i in range(len(my_lst)):
      if i == 0:
        print(f"First I eat {my_lst[0]}")
      else:
        print(f"Next I eat {my_lst[i]}")

hello()
print('Items packed for lunch', pack('sandwich', 'raspberries', 'dessert'))
lunch_list = pack('sandwich', 'raspberries', 'dessert')
eat_lunch(lunch_list)
