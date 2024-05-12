
from django.urls import path
from . import views

urlpatterns = [
    path("",views.home, name="home"),
    path('about/', views.about_us, name="about_us"),
    path('login/',views.login_user,name="login"),
    path('register/',views.register_user,name="register"),
     path('categories/', views.list_categories, name='category_list'),
    path('categories/<int:category_id>/', views.category_products, name='category_products'),
    path('logout/',views.logout_user,name="logout"),
    path('admin_session/',views.admin_session,name="admin_session"),
    path('profile/<int:pk>/', views.profile, name='profile'),
    path('product/<int:pk>/', views.product_details, name='product_details'),
    path('product/<int:pk>/update/', views.update_product, name='update_product'),
    path('update_user/',views.update_user,name="update_user"),
    path('add_product/', views.add_product, name='add_product'),
    path('search_products',views.search_products, name = 'search_products'),
    path('delete_product/<int:pk>', views.delete_product, name="delete_product"), 
    path('<str:slug>/', views.page_not_found, name = "page_not_found"), 
]
