from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Recommendation

@login_required
def user_recommendations(request):
    recommendations = Recommendation.objects.filter(user=request.user)[:20]
    return render(request, 'recommendations.html', {'recommendations': recommendations})