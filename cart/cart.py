CART_SESSION_ID = 'cart'

class Cart:
    def __init__(self, request: object) -> None:
        self.session = request.session
        cart = self.session.get(CART_SESSION_ID)
        if not cart:
            cart = {}
            self.session[CART_SESSION_ID] = cart
        self.cart = cart

    def count(self):
        return sum(item['quantity'] for item in self.cart.values())

    def add(self, product, quantity=1, update_quantity=False):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0, 'price': float(product.price)}

        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity

        self.save()

    def save(self):
        self.session.modified = True

    def get_total_price(self):
        return sum(item['price'] * item['quantity'] for item in self.cart.values())
