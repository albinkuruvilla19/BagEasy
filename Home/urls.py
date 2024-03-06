
from django.urls import path,include
from . import views


urlpatterns = [
    path('',views.home,name="home"),
    path('account',views.account,name="account"),
    path('contact',views.contact,name="contact"),
    path('collections',views.collections,name="collections"),
    path('collections/<str:name>',views.collectionsview,name="collections"),
    path('collections/<str:cname>/<str:pname>',views.productsview,name="productsview"),
    path('addproduct/',views.add_product,name="addproduct"),
    path('editproduct/<int:product_id>/',views.edit_product,name="editproduct"),
    path('delete/<int:product_id>/',views.delete_product, name='deleteproduct'),
    path('view/',views.view,name="view"),
    path('register/',views.register,name="register"),
    path('login/',views.loginpage,name="login"),
    path('adminlogin/',views.admin_login,name="admin_login"),
    path('logout/', views.logout_view, name='logout'),
    path('addtocart', views.add_to_cart, name='addtocart'),
    path('cart', views.viewcart, name='cart'),
    path('removecart/<str:cid>', views.removecart, name='removecart'),
    path('checkout/', views.checkout, name='checkout'),
    path('order_history/',views.order_history, name='order_history'),
    path('search/', views.product_search, name='product_search'), 
]


