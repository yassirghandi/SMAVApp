from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q
from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView, View)
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from .forms import UserRegisterForm, UserUpdateForm
from .models import Notification
from .serializers import LoginSerializer, NotificationSerializer


class HomeView(LoginRequiredMixin, View):
    def get(self, request):
        return redirect("listDeviceGroups")


class RegisterView(View):
    def get(self, request):
        form = UserRegisterForm()
        return render(request, "users/register.html", {"form": form})

    def post(self, request):
        form = UserRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(
                request, f"Your account has been created! You are now able to log in"
            )
            return redirect("authentication:LoginView")
        return render(request, "users/register.html", {"form": form})


class ProfileView(LoginRequiredMixin, View):
    def get(self, request):
        u_form = UserUpdateForm(instance=request.user)

        context = {"u_form": u_form}

        return render(request, "users/profile.html", context)

    def post(self, request):
        u_form = UserUpdateForm(request.POST, request.FILES, instance=request.user)

        if u_form.is_valid():
            u_form.save()
            messages.success(request, f"Your account has been updated!")
            return redirect("authentication:ProfileView")
        context = {"u_form": u_form}
        return render(request, "users/profile.html", context)


class ChangePasswordView(LoginRequiredMixin, PasswordChangeView):
    template_name = "users/change_password.html"

    def get_success_url(self):
        return reverse("authentication:HomeView")


@login_required
def alerts_data_view(request):
    notifications = request.user.notifications.all().order_by("-created_at")[:50]
    serializer = NotificationSerializer(data=notifications, many=True)
    serializer.is_valid()
    data = {
      "notifications": serializer.data
    }
    return JsonResponse(data, safe=False)

@csrf_exempt
@login_required
def mark_notifications_read(request):
    notifications = request.user.notifications.filter(read=False)
    for notification in notifications:
        notification.read = True
    Notification.objects.bulk_update(notifications, ["read"])
    data = {
      "success": True
    }
    return JsonResponse(data, status=200, safe=False)


class LoginAPIView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data
        refresh = RefreshToken.for_user(user)

        return Response(
            {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            },
            status=status.HTTP_200_OK
        )
