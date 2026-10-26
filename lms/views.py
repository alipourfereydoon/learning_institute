from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Submission
@login_required
def my_submissions(request):
    return render(request,'lms/submissions.html',{'submissions':Submission.objects.filter(student=request.user)})
