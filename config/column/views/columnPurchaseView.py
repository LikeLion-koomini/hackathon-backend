from rest_framework.generics import ListAPIView
from column.models._init_ import Column, Purchaser
from user.models import User
from column.serializers.columnSerializer import ColumnSerializer
from rest_framework.response import Response
from rest_framework import status

class ColumnPurchaseView(ListAPIView):
    # 구매 여부 확인
    def is_purchase(self, column_id):
        # 사용자 정보 조회 불가시 : 
        if self.request.user is None:
            return False
        # 구매자 정보 조회 여부
        try:
          if Purchaser.objects.get(user_id=self.request.user.uuid, column_id=Column.objects.get(column_id=column_id).column_id):
            return True
        except:
          return False
    # 구매 처리
    def patch(self, request, *args, **kwargs):
        column_id = self.request.data.get("column_id")
        column = Column.objects.get(column_id=column_id)
        user = User.objects.get(uuid=request.user.uuid)
        # 사용자 여부 확인하기
        if user is None:
            return Response({
                "message":"need access_token",
            }, status=status.HTTP_400_BAD_REQUEST)
        # Purchaser 생성
        if user.money < column.price:
            return Response({
                "success":False,
                "message":"보유 금액이 충분하지 않습니다."
            },status=status.HTTP_200_OK)
        elif self.is_purchase(column_id):
            return Response({
                "success":"exist",
                "message":"이미 구매했습니다."
            },status=status.HTTP_200_OK)
        elif user.money >= column.price:
            user.money = user.money - column.price
            user.save()
            Purchaser.objects.create(user_id=user, column_id=column)
            return Response({
                "success":True,
                "message":"구매 완료"
            },status=status.HTTP_200_OK)

    # 구매 여부
    def get(self, request, *args, **kwargs):
        column_id = self.request.GET.get("column_id")
        print(column_id)
        if Column.objects.filter(column_id=column_id).exists:
          try:
            column = Column.objects.get(column_id=column_id)
          except:
             return Response({
                  "purchase":False,
                  "message":"칼럼이 없어요"
              },status=status.HTTP_400_BAD_REQUEST)
          try: 
            if Purchaser.objects.get(user_id=self.request.user, column_id=column):
              return Response({
                  "purchase":True,
                  "message":"구매 완료"
              },status=status.HTTP_200_OK)
          except:
            return Response({
                "purchase":False,
                "message":"미구매"
            },status=status.HTTP_200_OK)