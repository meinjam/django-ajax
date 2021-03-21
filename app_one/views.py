from django.shortcuts import render, redirect
from .models import *
from django.views import View
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_list_or_404, get_object_or_404


def homepage(request):
    return render(request, "index.html")


def get_data(request, types):
    if request.method == "GET":
        if types == 'TODOS':
            entries = Posts.objects.order_by(
                '-id').values('id', 'title', 'is_published', 'created_at')
        e = list(entries)
        return JsonResponse(e, safe=False)


@csrf_exempt
def delete_data(request, id):
    todo = get_object_or_404(Posts, pk=id)
    todo.delete()
    return JsonResponse({"delete": True})
