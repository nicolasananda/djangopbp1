from django.urls import path
from wishlist.views import show_wishlist
from wishlist.views import show_xml #customize to the name of the function created
from wishlist.views import show_json # adjust the name of the function created
from wishlist.views import show_json_by_id #customise the name of the function created
from wishlist.views import register # Customize with the name of the function created
from wishlist.views import login_user  # Customize with the name of the function created
from wishlist.views import logout_user

app_name = 'wishlist'

urlpatterns = [
    path('', show_wishlist, name='show_wishlist'),
    path('xml/', show_xml, name='show_xml'), #customize the name of the function created
    path('json/', show_json, name='show_json'), #customise the name of the function created
    path('json/<int:id>', show_json_by_id, name='show_json_by_id'), #customise the name of the function created
    path('register/', register, name='register'), # Customize with the name of the function created
    path('login/', login_user, name='login'),  # Customize with the name of the function created
    path('logout/', logout_user, name='logout'),  # Customize with the name of the function created
]