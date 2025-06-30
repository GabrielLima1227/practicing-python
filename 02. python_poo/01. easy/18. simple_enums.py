class OrderStatus:
    PENDING = "Pending"
    PROCESSING = "Processing"
    SHIPPED = "Shipped"
    DELIVERED = "Delivered"
    CANCELED = "Canceled"
    VALID_STATUSES = {PENDING, PROCESSING, SHIPPED, DELIVERED, CANCELED}

class Order:
    def __init__(self, order_id: int):
        self.order_id = order_id
        self.status = OrderStatus.PENDING
        print(f"Order {self.order_id} created with status: {self.status}")

    def __str__(self):
        return f"Order ID: {self.order_id}, Current Status: {self.status}"

    def change_status(self, new_status: str) -> None:
        if new_status in OrderStatus.VALID_STATUSES:
            self.status = new_status
            print(f"Status of Order {self.order_id} changed to: {self.status}")
        else:
            print(f"Error: '{new_status}' is not a valid order status. "
                f"Valid statuses are: {', '.join(OrderStatus.VALID_STATUSES)}")

order1 = Order(order_id=101)
print(order1)

order1.change_status(OrderStatus.PROCESSING)
print(order1)

order1.change_status(OrderStatus.SHIPPED)
print(order1)

order1.change_status("InTransit")
print(order1)

order1.change_status(OrderStatus.DELIVERED)
print(order1)

order2 = Order(order_id=102)
order2.change_status(OrderStatus.CANCELED)
print(order2)