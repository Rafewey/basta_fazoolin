from datetime import datetime

class Menu:
    def __init__(self, name, items, start_time, end_time):     
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time

    def __repr__(self):
        real_time_start_time = datetime.strptime(str(self.start_time), "%H")
        start_time_final_clean = real_time_start_time.strftime("%I:%M %p")

        real_time_end_time = datetime.strptime(str(self.end_time), "%H")
        end_time_final_clean = real_time_end_time.strftime("%I:%M %p")

        return "{name} menu available from {start_time} to {end_time}".format(name=self.name, start_time=start_time_final_clean, 
        end_time=end_time_final_clean)

    def calculate_bill(self, purchased_items):
      total_to_return = 0
      for items in purchased_items:
        total_to_return += items
      return total_to_return

class Franchise:
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus

  def __repr__(self):
    return "This franchise is located on {address}.".format(address=self.address)

  def available_menus(self, time):
    available_menus = []
    for menu in self.menus:
      if time >= menu.start_time and time <= menu.end_time:
        available_menus.append(menu)
    return available_menus

class Business:
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises

brunch = Menu("brunch", {
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}, 11, 16)

early_bird = Menu("early_bird", {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}, 15, 18)

dinner = Menu("dinner", {
  'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}, 17, 23)

kids = Menu("kids", {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}, 11, 21)

flagship_store = Franchise("1232 West End Road", [brunch, early_bird, dinner, kids])
new_installment = Franchise("12 East Mulberry Street", [brunch, early_bird, dinner, kids])

first_business = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])

arepas_items = {
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}
arepas_menu = Menu("Take a' Arepa", arepas_items, 10, 20)
arepas_place = Franchise("189 Fitzgerald Avenue", [arepas_menu])
arepas_business = Business("Take a' Arepa", [arepas_place])
