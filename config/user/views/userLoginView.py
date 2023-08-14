from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.views import APIView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.response import Response
from user.models.user import User
from user.serializers import UserLoginSerializer

class UserLoginView(APIView):
    def post(self, request):
        user = authenticate(
            userId = request.data.get("userId"),
            password = request.data.get("password")
        )
        if user is not None:
            serializer = UserLoginSerializer(user)
            # 토큰 생성
            token = TokenObtainPairSerializer.get_token(user)
            # 재생성 토큰( 액세스 토큰 생성 시 사용 ) : 유효기간 1주일
            refresh_token = str(token)
            # 액세스 토큰( 사용자 인증시 사용 ) : 유효 기간 2시간 
            access_token = str(token.access_token)
            res = Response(
                {
                    "user":serializer.data,
                    "message":"login success",
                    "token":{
                        "refresh":refresh_token,
                        "access":access_token,
                    }
                },
                status=status.HTTP_200_OK
            )
            # jwt 토큰 => 쿠키에 저장
            res.set_cookie("access_token", access_token, httponly=True)
            res.set_cookie("refresh_token", refresh_token, httponly=True)
            return res
        else:
          return Response({"message":"회원 정보가 없음"},status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request):
        res = Response(
            {
                "message": "logout success",
            },
            status=status.HTTP_200_OK
        )
        res.delete_cookie("access_token")
        res.delete_cookie("refresh_token")
        return res