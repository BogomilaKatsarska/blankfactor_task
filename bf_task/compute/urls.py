from django.urls import path
from bf_task.compute.views import CSVFileUploadView

urlpatterns = (
    path('compute/', CSVFileUploadView.as_view()),
)