from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from column.models.column import Column

class CheckPreferView(APIView):
    def get(self, request, column_id, user_id):
        try:
            column = Column.objects.get(pk=column_id)
            user_prefer = column.prefer.filter(user_id=user_id).exists()

            data = {'user_prefer': user_prefer}
            return Response(data, status=status.HTTP_200_OK)
        except Column.DoesNotExist:
            return Response({'error': 'Column not found.'}, status=status.HTTP_404_NOT_FOUND)