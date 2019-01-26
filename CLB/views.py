from django.shortcuts import render
from django.contrib import auth
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from CLB.models import Team, Project, Bug  # 从模版引入字段
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404

# Create your views here.

# 登录
def login(request):
    return render(request, 'login.html')

# 登录动作处理
def login_action(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)  # 登录
            request.session['user'] = username  # 将session信息记录到浏览器
            response = HttpResponseRedirect('/my_projects/')
            return response
        else:
            return render(request, 'login.html', {'error': '用户名或密码错误'})
# 退出
# 退出登录
@login_required
def logout(request):
    auth.logout(request)  # 退出登录
    response = HttpResponseRedirect('/login/')
    return response

# 我的项目
@login_required
def my_projects(request):
    username = request.session.get('user', '')
    userid = request.user.id  # 获取当前用户的id
    project_list = Project.objects.filter(Project_peo__contains=userid)
    paginator = Paginator(project_list, 10)
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # 如果page不是整数，取第一页数据
        contacts = paginator.page(1)
    except EmptyPage:
        # 如果page不在范围内，取最后一页数据
        contacts = paginator.page(paginator.num_pages)
    return render(request,'my_projects.html', {'user': username,
                                               'projects': contacts})
# 根据项目名称搜索
@login_required
def search_name(request):
    username = request.session.get('user', '')
    userid = request.user.id  # 获取当前用户的id
    search_name = request.GET.get('Pname', '')
    project_list = Project.objects.filter(Project_peo__contains=userid, Pname__contains=search_name)
    paginator = Paginator(project_list, 10)
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # 如果page不是整数，取第一页数据
        contacts = paginator.page(1)
    except EmptyPage:
        # 如果page不在范围内，取最后一页数据
        contacts = paginator.page(paginator.num_pages)
    return render(request, 'my_projects.html', {'user': username,
                                                'projects': contacts})

# 新建项目
@login_required
def create_project(request):
    userid = request.user.id  # 获取当前用户的id
    username = request.session.get('user', '')
    return render(request, 'create_project.html', {'user': username})



