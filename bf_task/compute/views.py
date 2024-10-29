from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET', 'POST'])
def compute_view(request):
    if request.user.is_authenticated:
        result = {"message": "Computation successful"}
    else:
        pass
    return Response(result)
