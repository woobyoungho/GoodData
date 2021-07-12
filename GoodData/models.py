from django.db import models

# Create your models here.
class Customer(models.Model):
    cus_ID = models.CharField(max_length=100)
    cus_PW = models.CharField(max_length=100, null=False)
    cus_name = models.CharField(max_length=100)
    cus_address = models.CharField(max_length=500)
    cus_phone_number = models.CharField(max_length=13)
    point = models.IntegerField(default=0, null=False)
    naver_uid = models.CharField(max_length=500, default='', blank=True, null=False)
    facebook_uid = models.CharField(max_length=500, default='', blank=True, null=False)
    google_uid = models.CharField(max_length=500, default='', blank=True, null=False)
    cus_image = models.ImageField(upload_to='static/customer_img', blank=True, null=True)
    key_number = models.CharField(max_length=500, default='', blank=True, null=False)
    input_date = models.DateTimeField(auto_now_add = True)
    update_date = models.DateTimeField(auto_now = True)
    
    
class Campaign(models.Model):
    color_choices = {
        ('#eaf3fd', '시청'),
        ('#ced8e4', '위원회'),
        ('#b7d5f7', '공단'),
        ('#d1c7e6', '소방청'),
        ('#e2e6fb', '경찰청'),
        ('#d0d0d0', '센터'),
        ('#fdeaea', '연합회'),
        ('#e0edf1', '공사'),
        ('#adc9e2', '연구기관'),
        ('#c1e3ff', '재단'),
        ('#efefef', '진흥원'),
        ('#b3bef9', '정당'),
        ('#bde6f3', '법원'),
        ('#cdcce0', '행정부'),
        ('#c7cfff', '지자체'),
    }
    
    cam_id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='static/campaign_img', null=False)
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=500, null=True, blank=True)
    background_color = models.CharField(max_length=30, choices=color_choices, null=False, default='')
    input_date = models.DateTimeField(auto_now_add = True)
    update_date = models.DateTimeField(auto_now = True)
    
    
class Project(models.Model):
    pro_id = models.AutoField(primary_key=True)
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)
    pro_title = models.CharField(max_length=100)
    pro_content = models.TextField()
    pro_inputer = models.CharField(max_length=50)
    input_date = models.DateTimeField(auto_now_add = True)
    update_date = models.DateTimeField(auto_now = True)
    
    
class Project_Detail(models.Model):
    pro_detail_id = models.AutoField(primary_key=True)
    pro_order = models.IntegerField(default=1, null=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    video = models.FileField(upload_to='static/project_video', null=False)
    pro_detail_title = models.CharField(max_length=100)
    pro_detail_content = models.TextField()
    pro_detail_inputer = models.CharField(max_length=50)
    user1 = models.CharField(max_length=50, default='', blank=True)
    user2 = models.CharField(max_length=50, default='', blank=True)
    user3 = models.CharField(max_length=50, default='', blank=True)
    user4 = models.CharField(max_length=50, default='', blank=True)
    user5 = models.CharField(max_length=50, default='', blank=True)
    YN1 = models.CharField(max_length=50, default='', blank=True)
    YN2 = models.CharField(max_length=50, default='', blank=True)
    YN3 = models.CharField(max_length=50, default='', blank=True)
    YN4 = models.CharField(max_length=50, default='', blank=True)
    YN5 = models.CharField(max_length=50, default='', blank=True)
    input_date = models.DateTimeField(auto_now_add = True)
    update_date = models.DateTimeField(auto_now = True)
    

class User_Friends(models.Model):
    friends_id = models.AutoField(primary_key=True)
    cus_idx = models.ForeignKey(Customer, on_delete=models.CASCADE)
    cus_ID = models.CharField(max_length=100, blank=False)
    cus_name = models.CharField(max_length=100, blank=False)
    friend_id = models.CharField(max_length=100, blank=False)
    friend_name = models.CharField(max_length=100, blank=False)
    input_date = models.DateTimeField(auto_now_add = True)
    update_date = models.DateTimeField(auto_now = True)
    
    
class Notice(models.Model):
    notice_id = models.AutoField(primary_key=True)
    notice_title = models.CharField(max_length=100)
    notice_content = models.TextField()
    notice_inputer = models.CharField(max_length=50)
    input_date = models.DateTimeField(auto_now_add = True)
    update_date = models.DateTimeField(auto_now = True)
    

class app_version(models.Model):
    app_version_id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=100)
    version = models.CharField(max_length=100)
    
    
    
    
    
    
    
    
