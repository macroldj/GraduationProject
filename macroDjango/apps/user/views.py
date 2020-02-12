from random import choice

from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.shortcuts import render

from rest_framework import mixins , status
from rest_framework import viewsets
from rest_framework.response import Response

from macroDjango.settings import API_KEY
from user.models import UserProfile, VerifyCode
from user.serializers import UserProfileserializers, VerifyCodeSerializers
from utils.yunpian import YunPian


class VerifyCodeViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    自定义用户验证
    """
    queryset = VerifyCode.objects.all()
    serializer_class = VerifyCodeSerializers

    def generate_code(self):
        """
        生成四位数字的验证码
        :return:
        """
        seeds = "1234567890"
        random_str = []
        for i in range(4):
            random_str.append(choice(seeds))

        return "".join(random_str)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        mobile = serializer.validated_data["mobile"]
        yun_pian = YunPian(API_KEY)
        status_msg= yun_pian.send_sms(code=self.generate_code(), mobile=mobile)

        if status_msg["code"] != 0:
            return Response({
                "mobile":status_msg["msg"]
            }, status=status.HTTP_400_BAD_REQUEST)
        else:
            code_record = VerifyCode(code=self.generate_code(), mobile=mobile)
            code_record.save()
            return Response({
                "mobile":mobile
            }, status=status.HTTP_201_CREATED)


class UserProfileViewsets(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    用户信息 输出
    """
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileserializers
