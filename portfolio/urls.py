from django.urls import path
from portfolio import views

urlpatterns = [
    path('', views.customer_list),
    path('api/customers/', views.customer_list),
    path('api/mycustomers/', views.my_customer_list),
    path('api/customers/<int:pk>/', views.getCustomer),  # Added a trailing slash for consistency
    path('api/reviews/', views.review_list),
    path('api/reviews/<int:pk>/', views.getReview),  # Added a trailing slash for consistency
    path('api/reservations/', views.reservation_list),
    path('api/reservations/<int:pk>/', views.getReservation),  # Added a trailing slash for consistency
    path('api/menu/', views.menu_list),  # URL for the menu_list view
    path('api/menu/<int:pk>/', views.getMenu),  # URL for the getMenu view
    path('api/user/', views.getUser),  # URL for the getUser view
    # If you're planning to use RegisterView, add URLs for that as well. Example:
    # path('api/register/', views.RegisterView.as_view()),
]