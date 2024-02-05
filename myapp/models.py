# Importing the models module from Django's db module
from django.db import models

# Importing the User model from Django's auth models
from django.contrib.auth.models import User

# Category model definition
class Category(models.Model):
    # slug field for URL-friendly version of the category name
    slug = models.SlugField()
    # title field for the category name, with a maximum length of 255 characters
    title = models.CharField(max_length=255, db_index=True)

# MenuItem model definition
class MenuItem(models.Model):
    # title field for the menu item name, with a maximum length of 255 characters
    title = models.CharField(max_length=255, db_index=True)
    # price field for the price of the menu item, with a maximum of 6 digits and 2 decimal places
    price = models.DecimalField(max_digits=6, decimal_places=2, db_index=True)
    # featured field to indicate whether the menu item is featured or not
    featured = models.BooleanField(db_index=True)
    # category field as a foreign key to the Category model
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

# Cart model definition
class Cart(models.Model):
    # user field as a foreign key to the User model
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # menuitem field as a foreign key to the MenuItem model
    menuitem = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    # quantity field for the quantity of the menu item in the cart
    quantity = models.SmallIntegerField()
    # unit_price field for the price per unit of the menu item
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    # price field for the total price of the menu item in the cart
    price = models.DecimalField(max_digits=6, decimal_places=2)

    # Meta class for additional model configuration
    class Meta:
        # unique_together constraint to ensure that a user can only have one of each menu item in their cart
        unique_together = ("menuitem", "user")

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    delivery_crew = models.ForeignKey(
        User, on_delete=models.SET_NULL, related_name="delivery_crew", null=True
    )
    status = models.BooleanField(default=0, db_index=True)
    total = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    date = models.DateField(db_index=True)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="order")
    menuitem = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.SmallIntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        unique_together = ("order", "menuitem")