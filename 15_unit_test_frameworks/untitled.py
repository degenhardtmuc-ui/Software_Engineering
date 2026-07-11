class OrderManager:
    def __init__(self):
        self.orders = []

    def create_order(self, item_name: str, item_quantity: int, item_price: float):
        order_id = len(self.orders) + 1

        order_total = item_quantity * item_price

        order = {
            "id": order_id,
            "item": item_name,
            "quantity": item_quantity,
            "price": item_price,
            "total": order_total
        }

        self.orders.append(order)

        return f"Bestellung #{order_id}: {item_quantity}x {item_name} für insgesamt {order_total} Euro wurde angelegt."

    def get_total_price(self):
        total_price = 0

        for order in self.orders:
            total_price = total_price + order["total"]

        return total_price

    def get_all_orders(self):
        return self.orders


class OrderController:
    def __init__(self, manager: OrderManager):
        self.manager = manager

    def handle_create_order(self, item_name, quantity, price):
        return self.manager.create_order(item_name, quantity, price)

    def handle_get_total_price(self):
        return self.manager.get_total_price()

    def handle_get_all_orders(self):
        return self.manager.get_all_orders()


class OrderGUI:
    def __init__(self, controller: OrderController):
        self.controller = controller

    def render_order_form(self):
        while True:
            item = input("Was möchtest Du bestellen? Oder 'fertig' eingeben: ")

            if item == "fertig":
                break

            quantity = int(input("Menge: "))
            price = float(input("Preis pro Stück: "))

            print("GUI sendet Daten an den Controller")
            print("Controller koordiniert die Anfrage und sendet sie an das Model")

            response = self.controller.handle_create_order(item, quantity, price)

            print("Antwort:", response)
            print("----------------------")

        print("Alle Bestellungen:")
        orders = self.controller.handle_get_all_orders()

        for order in orders:
            print(order)

        total_price = self.controller.handle_get_total_price()
        print("Gesamtpreis:", total_price, "Euro")


order_manager = OrderManager()
order_controller = OrderController(order_manager)
gui = OrderGUI(order_controller)

gui.render_order_form()