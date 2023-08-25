from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view

User = get_user_model()

# Create your views here.


@api_view(["POST"])
def get_distribution_view(request):
    req_data = request.data.copy()
    data = req_data.pop("user")
    data.get("1")




    # "user": {
    #     "1": [1, 2],
    #     "2": [2, 3],
    #     "3": [1, 2],
    # }

