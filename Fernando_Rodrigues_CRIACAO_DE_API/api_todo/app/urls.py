from app.views import TodoViewSet
from rest_framework.routers import DefaultRouter
#from django.urls import path

router = DefaultRouter()
router.register(r'',TodoViewSet)
urlpatterns = router.urls

'''
urlpatterns = [
    path('', TodoListAndCreate.as_view()),
    path('<int:pk>/', TodoDetailChangeAndDelete.as_view()),
]
'''
