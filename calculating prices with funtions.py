def calculating_price():
  while True:
    try:
        def total_price(new,used):
            new_videogames_cost = new * 1000
            used_videogames_cost = used * 350
            total = new_videogames_cost + used_videogames_cost
            return total

        new_videogames_units = int(input("number of new videogames to buy\n"))
        used_videogames_units = int(input("number of used videogames to buy\n"))

        total = total_price(new_videogames_units,used_videogames_units)
        print(total)
        return
    except ValueError:
        print("Please give a valid value")
calculating_price()

