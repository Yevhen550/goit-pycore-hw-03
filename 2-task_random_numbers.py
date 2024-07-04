import random

def get_numbers_ticket(min, max, quantity):
    
    try:
      if min < 1 or max > 1000 or quantity < 1 or quantity > (max - min + 1):
        return []
            
      random_num = random.sample(range(min, max + 1), quantity)
      random_num.sort()
    #   unique_numbers = set(random_num)  #***Чи потрібна перевірка на унікальність чисел в списку за допомогою множин?***
    #   res = sorted(unique_numbers)    
      
      print("Рандомні числа згенеровані!)")
      return random_num
  
    except TypeError:
      return print("Не коректно введені дані...")
  
  
            
lottery_numbers = get_numbers_ticket(1, 5, 3)
print("Ваші лотерейні числа:", lottery_numbers)

