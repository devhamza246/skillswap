from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from rest_framework.authtoken.models import Token
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import PasswordResetTokenGenerator


User = get_user_model()


class RegisterView(APIView):
    def register(request):
        email = request.POST["email"]
        password = request.POST["password"]
        if User.objects.filter(email=email).exists():
            return JsonResponse({"error": "Email already exists"}, status=400)
        else:
            user = User.objects.create_user(email=email, password=password)
            token, created = Token.objects.get_or_create(user=user)
            return JsonResponse({"token": token.key})


class LoginView(APIView):
    def login(request):
        username = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            return JsonResponse({"token": token.key})
        else:
            return JsonResponse({"error": "Login Failed"}, status=400)


class SignoutView(APIView):
    def signout(request):
        logout(request)
        return redirect("auth:signin")


class ResetPasswordView(APIView):
    def reset_password(request):
        email = request.POST["email"]
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            scheme = "https" if request.is_secure() else "http"
            full_host = request.get_host()
            base_url = f"{scheme}://{full_host}"
            user.send_forgot_password_email(base_url, email)
            return JsonResponse({"message": "Password reset email sent"})
        else:
            return JsonResponse({"error": "Email does not exist"}, status=400)


class VerifyPasswordResetView(APIView):
    def verify_password_reset(request, uidb64=None, token=None, **kwargs):
        try:
            user_id = force_str(urlsafe_base64_decode(uidb64))
            user = get_user_model().objects.get(id=user_id)
        except get_user_model().DoesNotExist:
            return JsonResponse({"error": "User does not exist"}, status=400)
        token_generator = PasswordResetTokenGenerator()
        check_token = token_generator.check_token(user, token)
        if not check_token:
            return JsonResponse({"error": "Invalid/Expired token"}, status=400)
        user.set_password(request.POST.get("password"))
        user.save()
        return JsonResponse({"message": "Password reset successful"}, status=200)
