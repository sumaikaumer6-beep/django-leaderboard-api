from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Score
# Create your views here.
@api_view(['POST'])
def save_score(request):
    name=request.data.get("player_name")
    score=request.data.get("score")
    Score.objects.create(player_name=name,score=score)
    return Response({"message":"Score saved"})
@api_view(['GET'])
def get_leaderboard(request):
    top_score=Score.objects.order_by('-score')[:10]
    data=[{"player_name": s.player_name,"score": s.score} for s in top_score]
    return Response(data)
