shopping_cart = []
prices = []
iteam = ('anything')
destination = ('')

while destination != ('quit'):
   destination = input('Where would you like to go? add/remove/show/total/quit: ')
   if destination == ('add'):

      while iteam != (''):
         iteam = input('What would you like to add to the list? Enter enter to finalize: ')
         if iteam != (''):
            price = (input(f'How much does {iteam} cost?'))
            price = float(price)
            shopping_cart.append(iteam)
            prices.append(price)

   elif destination == ('remove'):
      remove = input('Would you like to remove an iteam from your list? yes/no: ')
      if remove == 'yes':
         for i in range(len(shopping_cart)):
            print(f' {i} {shopping_cart[i]}')

      number = int(input ('What is the number of the iteam you would like to remove? '))

      shopping_cart.pop(number)
      prices.pop(number)

   elif destination == ('show'):
      print(shopping_cart)
   
   elif destination == ('total'):
      print(sum(prices))
