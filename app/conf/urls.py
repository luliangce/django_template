from django.core.exceptions import PermissionDenied
from django.http.request import HttpRequest
from django.http.response import HttpResponse, JsonResponse
from django.urls import path
from ninja import NinjaAPI

from authentication.views import auth_router
from ecode import LOGINREQUIRED

api = NinjaAPI(title="demo")
api.add_router('auth/', auth_router)


@api.exception_handler(PermissionDenied)
def handleLoginRequired(request: HttpRequest, exc: PermissionDenied):
    return JsonResponse(LOGINREQUIRED.body,
                        json_dumps_params={"ensure_ascii": False})


urlpatterns = [path("", api.urls)]
