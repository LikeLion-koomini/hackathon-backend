from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from column.models.column import Column, ColumnPrefer
from user.models.user import User

class CheckPreferView(APIView):
    def get(self, request, column_id, user_id):
        try:
            column = Column.objects.get(column_id=column_id)
            user = User.objects.get(uuid=user_id)
            user_prefer = ColumnPrefer.objects.filter(column=column, user=user).exists()

            return Response({'user_prefer': user_prefer}, status=status.HTTP_200_OK)
        except Column.DoesNotExist:
            return Response({'error': 'Column not found.'}, status=status.HTTP_404_NOT_FOUND)
        except User.DoesNotExist:
            return Response({'error': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)