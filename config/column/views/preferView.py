from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from column.models import Column, ColumnPrefer
from user.models import CustomUser  # CustomUser 모델을 임포트해야 합니다.

class PreferView(APIView):
    def post(self, request, column_id, user_id):
        try:
            column = Column.objects.get(pk=column_id)
            user = CustomUser.objects.get(pk=user_id)
            column_prefer, created = ColumnPrefer.objects.get_or_create(column=column, user=user)
            if created:
                return Response({'message': 'Column liked successfully'}, status=status.HTTP_201_CREATED)
            else:
                return Response({'message': 'Column already liked'}, status=status.HTTP_200_OK)
        except (Column.DoesNotExist, CustomUser.DoesNotExist):
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, column_id, user_id):
        try:
            column = Column.objects.get(pk=column_id)
            user = CustomUser.objects.get(pk=user_id)
            column.prefer.filter(user=user).delete()
            return Response({'message': 'Column like removed'}, status=status.HTTP_200_OK)
        except (Column.DoesNotExist, CustomUser.DoesNotExist):
            return Response(status=status.HTTP_404_NOT_FOUND)
