from django.urls import path
from .views import (
    index,
    product_list,
    product_detail,
    cart_view,
    add_to_cart,
    checkout,
    order_history,
    register,
    profile,
    login_view,  # Импортируйте login_view
)

from django.contrib.auth import views as auth_views

app_name = 'store'

urlpatterns = [
    path('', index, name='index'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),

    path('products/', product_list, name='product_list'),
    path('products/<int:product_id>/', product_detail, name='product_detail'),
    path('cart/', cart_view, name='cart'),
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('checkout/', checkout, name='checkout'),
    path('order_history/', order_history, name='order_history'),
    path('register/', register, name='register'),  # Убедитесь, что эта строка присутствует только один раз
    path('profile/', profile, name='profile'),
    path('login/', login_view, name='login'),  # Используйте ваш login_view
    path('logout/', auth_views.LogoutView.as_view(next_page='store:index'), name='logout'),  # Измените next_page на нужный
]
