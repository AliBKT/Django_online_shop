from products.models import Product

class Cart:
    
    def __init__(self, request):
        # Get request
        self.request = request
        
        # Create session
        self.session = request.session
        
        # Get cart from session
        cart = self.session.get('cart')
        
        # If session cart not be created 
        if not cart :
            self.session['cart'] = {}
            cart = self.session['cart']
        
        # Assain cart
        self.cart = cart
    
    def add(self, product, quantity=1, replaced_current_quantity=False):
        
        # Get product id 
        product_id = str(product.id)
        
        # Add product to cart if not in cart or update quantity
        if product_id not in self.cart :
            self.cart[product_id] = {'quantity': 0}
        
        
        if replaced_current_quantity :
            self.cart[product_id]['quantity'] = quantity
        else :
            self.cart[product_id]['quantity'] += quantity    
            
        
        
        # Save session
        self.save()
    
    def remove(self, product):
        # Remove product from cart
        
        product_id = str(product.id)
        
        # Remove product_id from cart if product exsist 
        if product_id in self.cart :
            del self.cart[product_id]
            
            # Save session
            self.save()
        
    def save(self):
        # Save session modified
        self.session.modified = True      
        
    def __iter__(self):
        
        # Get ids form cart
        products_ids = self.cart.keys()
        
        # Get product from Product model
        products = Product.objects.filter(id__in=products_ids)
        
        # Get copy of cart
        cart = self.cart.copy()
        
        for product in products :
            cart[str(product.id)]['product_obj'] = product
        
        for item in cart.values() :
            item['total_price'] = item['product_obj'].price * item['quantity']
            yield item
        
    def __len__(self) :
        
        # Return len of cart
        return len(self.cart.keys())
    
    def clear(self):
        
        # Claer all products in cart  
        del self.session['cart']
        
        # Save session
        self.save()
    
    # clac total price
    def get_total_price(self):
        
        # Get ids of products in cart
        product_ids = self.cart.keys()
        
        # Get products object which in cart
        products = Product.objects.filter(id__in=product_ids)
        
        # Sum price of products
        return sum(product.price for product in products)