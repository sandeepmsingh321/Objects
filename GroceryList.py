class GroceryItemOrder:
    def __init__(self, name, quantity, price_per_unit):
        self.name = name
        self.quantity = quantity
        self.price_per_unit = price_per_unit

    def cost(self):
        return self.quantity * self.price_per_unit

    def display(self):
        return f"{self.name}, Quantity: {self.quantity}, Price per unit: ${self.price_per_unit}, Total Cost: ${self.cost()}"

class GroceryList:
    def __init__(self):
        self.items = []

    def add(self, item):
        if isinstance(item, GroceryItemOrder):
            self.items.append(item)
        else:
            print("Please provide a valid GroceryItemOrder object.")

    @property
    def total_cost(self):
        return sum(item.cost() for item in self.items)

    def display_items(self):
        for item in self.items:
            print(item.display())
        print(f"Total Cost: ${self.total_cost}")


if __name__ == '__main__':
    cookies = GroceryItemOrder("Cookies", 4, 5)
    milk = GroceryItemOrder("Milk", 2, 3)
    bread = GroceryItemOrder("Bread", 3, 2)

    my_grocery_list = GroceryList()

    my_grocery_list.add(cookies)
    my_grocery_list.add(milk)
    my_grocery_list.add(bread)

    my_grocery_list.display_items()
