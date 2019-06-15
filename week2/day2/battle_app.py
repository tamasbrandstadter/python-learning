from weeks.week2.day2.ship import Ship

ship1 = Ship('Alma Ship1')
ship1.fill_ship()
ship1.drink_for_captain()

ship2 = Ship('Korte Ship2')
ship2.fill_ship()
ship2.drink_for_captain()

ship1.print_ship()
ship2.print_ship()

ship1.battle(ship2)
ship1.print_ship()
ship2.print_ship()
