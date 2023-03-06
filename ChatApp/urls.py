from django.urls import path
from . import views
from rest_framework_simplejwt import views as jwt_views
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

def is_string_an_url(url_string: str) -> bool:
    validate_url = URLValidator(verify_exists=True)
    try:
        validate_url(url_string)
    except ValidationError as e:
        return e
    return True

urlpatterns = [
    path('api/create-thread', views.CreateThread.as_view(), name='create-thread'), #creating a new thread, accepts the POST method
    path('api/delete-thread/<pk>', views.DeleteThread.as_view(), name='delete-thread'), #deleting thread by pk in get parameter, accepts the DELETE method

    path('api/get-threads-by-user', views.GetAllThreadByUser.as_view(), name='get-threads-by-user'), #get all threads with messages by user, accepts the GET method

    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'), #getting jwt token
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'), #jwt token update

    path('api/add-new-message', views.CreateNewMessage.as_view(), name='add-new-message'), #adding a new message, accepts the POST method
    path('api/get-all-message/<pk>', views.GetMessageForThread.as_view(), name='get-all-message'), #get all messages for a thread by pk in get parameter, accepts the GET method
    path('api/get-count-unread-messages', views.GetCountUnreadMessageForUser.as_view(), name='get-unread-messages'), #get the number of unread messages for the user, accepts the GET method
    path('api/put-mark-read-message/<pk>', views.MarkReadMessage.as_view(), name='put-mark-read-message') #change status of unread message, accepts PUT method
]
