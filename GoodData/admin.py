from django.contrib import admin
from GoodData.models import Customer, Campaign, Project, Project_Detail, User_Friends, Notice, app_version


class Customer_Admin(admin.ModelAdmin):
    list_display = ('cus_ID', 'cus_PW', 'cus_name', 'cus_address', 'cus_phone_number', 'point', 'naver_uid', 'facebook_uid', 'google_uid', 'cus_image', 'input_date', 'update_date')
    
class Campaign_Admin(admin.ModelAdmin):
    list_display = ('cam_id', 'image', 'title', 'content', 'background_color', 'input_date', 'update_date')
     
class Project_Admin(admin.ModelAdmin):
    list_display = ('pro_id', 'campaign_id', 'pro_title', 'pro_content', 'pro_inputer', 'input_date', 'update_date')
      
class Project_Detail_Admin(admin.ModelAdmin):
    list_display = ('pro_detail_id', 'pro_order', 'project_id', 'video', 'pro_detail_title', 'pro_detail_content', 'pro_detail_inputer', 'user1', 'user2', 'user3', 'user4', 'user5', 'YN1', 'YN2', 'YN3', 'YN4', 'YN5', 'input_date', 'update_date')

class User_Friends_Admin(admin.ModelAdmin):
    list_display = ('friends_id', 'cus_idx_id', 'cus_ID', 'cus_name', 'friend_id', 'friend_name', 'input_date', 'update_date')

class Notice_Admin(admin.ModelAdmin):
    list_display = ('notice_id', 'notice_title', 'notice_content', 'notice_inputer', 'input_date', 'update_date')
    
class app_version_Admin(admin.ModelAdmin):
    list_display = ('app_version_id', 'type', 'version')    
    
# Register your models here.
admin.site.register(Customer, Customer_Admin)
admin.site.register(Campaign, Campaign_Admin)
admin.site.register(Project, Project_Admin)
admin.site.register(Project_Detail, Project_Detail_Admin)
admin.site.register(User_Friends, User_Friends_Admin)
admin.site.register(Notice, Notice_Admin)
admin.site.register(app_version, app_version_Admin)
