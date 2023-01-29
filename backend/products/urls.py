from django.urls import path

from . import views

urlpatterns=[
    # path('',views.product_create_view), # '/api/product/- Only for create
    path('',views.product_list_create_view), # List and create
    
    # path('<int:pk>/',views.ProductDetailAPIView.as_view()), # Retrieves single object
    path('<int:pk>/',views.product_detail_view),

    path('<int:pk>/update/',views.product_update_view),
    path('<int:pk>/delete/',views.product_delete_view),

    # path('',views.product_mixin_view),
    # path('<int:pk>/',views.product_mixin_view)

    # Function based view
    # path('',views.product_alt_view),
    # path('<int:pk>/',views.product_alt_view)
    
]