from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# 团队
class Team(models.Model):
    Tname = models.CharField(max_length=100)  # 团队名称
    create_time = models.DateTimeField(auto_now=True)  # 创建时间
    number = models.IntegerField()  # 团队人数
    Team_peo = models.CommaSeparatedIntegerField(max_length=1000)  # 团队成员id

    def __str__(self):
        return self.Tname

# 项目
class Project(models.Model):
    Pname = models.CharField(max_length=100)  # 项目名称
    create_time = models.DateTimeField(auto_now=True)  # 创建时间
    all_bugs = models.IntegerField()  # 总缺陷数
    Project_peo = models.CommaSeparatedIntegerField(max_length=1000)  # 项目成员id


    def __str__(self):
        return self.Pname

# 缺陷
class Bug(models.Model):
    status_list = (
        (1, '待处理'),
        (2, '待审核'),
        (3, '已修复'),
        (4, '已拒绝')
    )
    degree_list = (
        (1, '致命'),
        (2, '严重'),
        (3, '较重'),
        (4, '一般'),
        (5, '建议')
    )
    priority_list = (
        (1, '马上解决'),
        (2, '急需解决'),
        (3, '高度重视'),
        (4, '正常处理'),
        (5, '低优先级')
    )

    Pid = models.ForeignKey(Project, on_delete=models.DO_NOTHING,)  # 所属项目
    Bname = models.CharField(max_length=200)  # 缺陷标题
    status = models.IntegerField(choices=status_list)  # 缺陷状态
    degree = models.IntegerField(choices=degree_list)  # 严重程度
    priority = models.IntegerField(choices=priority_list)  # 优先级
    create_peo = models.IntegerField()  # 创建人
    Dealing_people = models.IntegerField()  # 处理人
    create_time = models.DateTimeField(auto_now=True)  # 创建时间
    close_time = models.DateTimeField()  # 关闭时间
    # description = RichTextUploadingField()  # 描述
    description = models.BinaryField()  # 描述

    def __str__(self):
        return self.Bname

# 用户扩展
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
