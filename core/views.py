# shape_analyzer/views.py

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import GridInputSerializer
from .utils import get_layout


@api_view(['GET'])
def default_success_view(request):
    return Response({'message': 'Welcome to the API! It\'s working.'})


@api_view(['POST'])
def analyze_grid(request):
    if request.method == 'POST':
        serializer = GridInputSerializer(data=request.data)
        if serializer.is_valid():
            grid = serializer.validated_data['grid']
            results = get_layout(grid)
            return Response(results)
        return Response(serializer.errors, status=400)
