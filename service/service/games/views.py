from django.shortcuts import render

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from games.models import VideoGame
from games.serializers import VideoGameSerializer

@csrf_exempt
def game_list(request):
    """
    List all code snippets, or create a new game.
    """
    if request.method == 'GET':
        games = VideoGame.objects.all()
        serializer = VideoGameSerializer(games, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = VideoGameSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def game_detail(request, pk):
    """
    Retrieve, update or delete a game.
    """
    try:
        game = VideoGame.objects.get(pk=pk)
    except VideoGame.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = VideoGameSerializer(game)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = VideoGameSerializer(game, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        game.delete()
        return HttpResponse(status=204)
