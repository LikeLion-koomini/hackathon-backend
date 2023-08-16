from rest_framework.response import Response
from rest_framework import status
from column.models.column import Column, ColumnPrefer
from rest_framework.views import APIView

class PreferView(APIView):
    def patch(self, request, column_id, *args, **kwargs):
        try:
            instance = Column.objects.get(column_id=column_id)
            
            # 사용자의 좋아요 확인
            user = self.request.user
            if ColumnPrefer.objects.filter(column=instance, user=user).exists():
                print(ColumnPrefer.objects.all())
                # return Response({'message': 'Already liked'}, status=status.HTTP_400_BAD_REQUEST)
                return self.delete_prefer(instance)
            # 좋아요 생성
            ColumnPrefer.objects.create(column=instance, user=user)

            # 컬럼의 prefer 값 증가
            instance.prefer += 1
            instance.save()

            return Response({'message': 'Column liked successfully'}, status=status.HTTP_200_OK)
        except Column.DoesNotExist:
            return Response({'message': 'Column not found'}, status=status.HTTP_404_NOT_FOUND)

    def delete_prefer(self, instance):
        try:
            # 사용자의 좋아요 확인
            user = self.request.user
            try:
                prefer = ColumnPrefer.objects.get(column=instance, user=user)
                prefer.delete()

                # 컬럼의 prefer 값 감소
                instance.prefer -= 1
                instance.save()

                return Response({'message': 'Column like removed'}, status=status.HTTP_200_OK)
            except ColumnPrefer.DoesNotExist:
                return Response({'message': 'Not liked'}, status=status.HTTP_400_BAD_REQUEST)
        except Column.DoesNotExist:
            return Response({'message': 'Column not found'}, status=status.HTTP_404_NOT_FOUND)