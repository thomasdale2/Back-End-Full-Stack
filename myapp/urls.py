# Importing the path function from Django's urls module
from django.urls import path

# Importing the views module from the current directory
from . import views

# Defining the urlpatterns list which Django will use to route incoming HTTP requests
urlpatterns = [
    # Routing requests with the path 'categories' to the CategoriesView
    path("categories", views.CategoriesView.as_view()),

    # Routing requests with the path 'menu-items' to the MenuItemsView
    path("menu-items", views.MenuItemsView.as_view()),

    # Routing requests with the path 'menu-items/<int:pk>' to the SingleMenuItemView
    # <int:pk> is a path converter that matches an integer and passes it as a 'pk' keyword argument to the view
    path("menu-items/<int:pk>", views.SingleMenuItemView.as_view()),

    # Routing requests with the path 'cart/menu-items' to the CartView
    path("cart/menu-items", views.CartView.as_view()),

    # Routing requests with the path 'orders' to the OrderView
    path("orders", views.OrderView.as_view()),

    # Routing requests with the path 'orders/<int:pk>' to the SingleOrderView
    # <int:pk> is a path converter that matches an integer and passes it as a 'pk' keyword argument to the view
    path("orders/<int:pk>", views.SingleOrderView.as_view()),

    # Routing requests with the path 'groups/manager/users' to the GroupViewSet
    # The as_view method is called with a dictionary that maps HTTP methods to viewset methods
    path(
        "groups/manager/users",
        views.GroupViewSet.as_view(
            {"get": "list", "post": "create", "delete": "destroy"}
        ),
    ),

    # Routing requests with the path 'groups/delivery-crew/users' to the DeliveryCrewViewSet
    # The as_view method is called with a dictionary that maps HTTP methods to viewset methods
    path(
        "groups/delivery-crew/users",
        views.DeliveryCrewViewSet.as_view(
            {"get": "list", "post": "create", "delete": "destroy"}
        ),
    ),
]