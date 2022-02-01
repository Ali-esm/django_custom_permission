from django.shortcuts import render, HttpResponse


from User.models import User, UserGroup, Permission
from django.views import View


# Create your views here.
def user_list(request, username):
    users = User.objects.all()
    group = UserGroup.objects.get(user__username=username)

    if group.name in ['adminstrator', 'normal users', 'limited admin']:
        context = {
            'users': users
        }

        return render(request, 'user/user_list.html', context)
    else:
        return HttpResponse('Not Authenticated', status=401)


class PermissionList(View):

    def get(self, request, username):
        group = UserGroup.objects.get(user__username=username)
        permissions = group.permissions.all()

        if group.name in ['adminstrator', 'limited admin']:
            context = {
                'permissions': permissions
            }
            return render(request, 'user/permission_list.html', context)
        else:
            return HttpResponse('Not Authenticated', status=401)


class CreateUser(View):

    def get(self, request, username):
        group = UserGroup.objects.get(user__username=username)
        groups = UserGroup.objects.all()

        if group.name in ['adminstrator']:
            context = {
                'groups': groups
            }
            return render(request, 'user/createuser_form.html', context=context)
        else:
            return HttpResponse('Not Authenticated', status=401)

    def post(self, request, username):
        group = UserGroup.objects.get(user__username=username)

        if group.name in ['adminstrator']:
            username = request.POST['username']
            group_name = request.POST['group']
            user = User(username=username)
            group = UserGroup.objects.get(name=group_name)
            user.save()
            user.groups.add(group)
            return HttpResponse('User Created', status=201)
        else:
            return HttpResponse('Not Authenticated')