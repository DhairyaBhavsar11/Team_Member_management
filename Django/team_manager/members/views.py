from django.shortcuts import render, redirect
from .models import TeamMember

def list_view(request):
    team_members = TeamMember.objects.all()
    return render(request, 'list.html', {'team_members': team_members})

def add_view(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        phone = request.POST['phone']
        email = request.POST['email']
        role = request.POST['role']
        TeamMember.objects.create(
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            email=email,
            role=role,
        )
        return redirect('list')
    return render(request, 'add.html')

def edit_view(request, pk):
    team_member = TeamMember.objects.get(pk=pk)
    if request.method == 'POST':
        team_member.first_name = request.POST['first_name']
        team_member.last_name = request.POST['last_name']
        team_member.phone = request.POST['phone']
        team_member.email = request.POST['email']
        team_member.role = request.POST['role']
        team_member.save()
        return redirect('list')
    return render(request, 'edit.html', {'team_member': team_member})

def delete_view(request, pk):
    team_member = TeamMember.objects.get(pk=pk)
    team_member.delete()
    return redirect('list')