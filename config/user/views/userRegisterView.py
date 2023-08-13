from user.serializers import UserRegisterSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class UserRegisterView(APIView):
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            # UserRegisterSerializer의 create 호출 --> user 반환
            user = serializer.save()
            
            # 토큰 생성
            token = TokenObtainPairSerializer.get_token(user)
            # 재생성 토큰( 액세스 토큰 생성 시 사용 ) : 유효기간 1주일
            refresh_token = str(token)
            # 액세스 토큰( 사용자 인증시 사용 ) : 유효 기간 2시간 
            access_token = str(token.access_token)
            
            res = Response(
                {
                    "user":request.data,
                    "message": "user register success",
                    "token":{
                        "refresh_token":refresh_token,
                        "access_token":access_token
                    },
                },
                status=status.HTTP_200_OK
            )

            # res.set_cookie("access_token",access_token, httponly=True)
            # res.set_cookie("refresh_token", refresh_token, httponly=True)
            return res
        return Response(
          {
            "errors":serializer.errors,
            "message":"invalid data",
          }, 
          status=status.HTTP_400_BAD_REQUEST
        )

