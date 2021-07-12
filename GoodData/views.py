from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.hashers import make_password, check_password
from .models import Customer, Campaign, Project, Project_Detail, User_Friends, Notice, app_version
from django.contrib import auth
import random
from django.template.defaultfilters import length
from allauth.socialaccount.models import SocialApp, SocialAccount


def Login(request):
    #로그인 페이지를 보여주기 위한 함수
    response_data = {}
    
    if request.method == "GET":
        print("login GET Enter")
        print("login request.session.get('user') :: ", request.session.get('user'))
        
        print("11111111 request.session.get('key') :: ", request.session.get('key'))
        print("22222222 request.session.get('user') :: ", request.session.get('user'))
        print()
        
        request.session['key'] = request.session.get('key')
        
        return render(request, 'GoodData/login.html')
    
    elif request.method == "POST":
        print("login POST 진입")
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        
        if not (username and password):
            response_data['error'] = "아이디와 비밀번호를 모두 입력하세요."
        else:
            user_exist = list(Customer.objects.values("cus_ID").all())
            
            for i in range(0,length(user_exist)):
                if user_exist[i]["cus_ID"] != username:
                    response_data['error'] = "아이디가 존재하지 않습니다."
                    
                else:
                    user = Customer.objects.get(cus_ID=username)
                    
                    if check_password(password, user.cus_PW):
                        request.session['user'] = user.cus_ID
                        print("request.session.get('user') :: ", request.session.get('user'))
                        
                        customer_update = Customer.objects.get(cus_ID=user.cus_ID)
                        print("customer_update :: ", customer_update)
                        print()
                        
                        print("request.session.get('key') :: ", request.session.get('key'))
                        if customer_update.key_number != request.session.get('key'):
                            customer_update.key_number = request.session.get('key')
                            customer_update.save()
                        
                        return redirect('campaign')
                    
                    else:
                        response_data['error'] = "비밀번호가 틀렸습니다."
                        break
        
        context={"response_data": response_data}
        return render(request, 'GoodData/login.html', context)


def Signup(request):
    #회원가입 페이지를 보여주기 위한 함수
    response_data = {}
    
    print("11111111 request.session.get('key') :: ", request.session.get('key'))
    print("22222222 request.session.get('user') :: ", request.session.get('user'))
    print()
        
    if request.method == "GET":
        return render(request, 'GoodData/signup.html')
    
    elif request.method == "POST":
        print()
        print("request.POST :: ", request.POST)
        print()
        print("request.FILES :: ", request.FILES)
        print()
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        name = request.POST['name']
        address = request.POST['address']
        #RRN = request.POST['RRN']
        phone_number = request.POST['phone_number']
        
        signup_confirm = list(Customer.objects.values('cus_ID').all())
        
        for i in range(0, length(signup_confirm)):
            if username == signup_confirm[i]['cus_ID']:
                response_data['error'] = '이미 등록된 아이디입니다.'
                return render(request, 'GoodData/signup.html', response_data)
            
        if password1 != password2:
            response_data['error'] = '비밀번호가 동일하지 않습니다.'
            return render(request, 'GoodData/signup.html', response_data)
            
        if username == '' or password1 == '' or password2 == '' or name == '' or address == '' or phone_number == '':
            response_data['error'] = '빈값은 저장할 수 없습니다.'
            return render(request, 'GoodData/signup.html', response_data)
        
        #=======================================================================
        # if length(RRN) != 6:
        #     response_data['error'] = "주민번호는 6자만 입력해주세요. '1999년 01월 01일' -> '990101'"
        #     return render(request, 'GoodData/signup.html', response_data)
        #=======================================================================
        
        profile_img = request.FILES.get('profile_img', None)
        
        if profile_img == None:
            profile_img = 'static/customer_img/profile_photo.jpg'
            
        new_customer = Customer(
            cus_ID = username,
            cus_PW = make_password(password1),
            cus_name = name,
            cus_address = address,
            #cus_RRN = RRN,
            cus_phone_number = phone_number,
            cus_image = profile_img,
            )
        new_customer.save()
        
        return HttpResponseRedirect(reverse('login'))


def Social_login_signup(request):
    print("social_login_signup Enter")
    
    print("11111111 request.session.get('key') :: ", request.session.get('key'))
    print("22222222 request.session.get('user') :: ", request.session.get('user'))
    
    response_data = {}
    
    if request.method == "POST":
        print()
        print("request.POST :: ", request.POST)
        print()
        print("request.FILES :: ", request.FILES)
        print()
        username = request.POST.get('username', None)
        password1 = request.POST.get('password1', None)
        password2 = request.POST.get('password2', None)
        name = request.POST.get('name', None)
        address = request.POST.get('address', None)
        #RRN = request.POST.get('RRN', None)
        phone_number = request.POST.get('phone_number', None)
        
        social_uid2 = request.POST.get('social_uid2', None)
        print("social_uid2 :: ", social_uid2)
        print()
        
        if social_uid2 != None:
            provider_name = list(SocialAccount.objects.values_list('provider').get(uid=social_uid2))
            print("provider_name[0] :: ", provider_name[0])
            print()
            
        signup_confirm = list(Customer.objects.values('cus_ID').all())
        
        for i in range(0, length(signup_confirm)):
            if username == signup_confirm[i]['cus_ID']:
                response_data['error'] = '이미 등록된 아이디입니다.'
                response_data['new_customer_show'] = 'new_customer_show'
                context={'response_data': response_data}
                return render(request, 'GoodData/social_login_confirm.html', context)
            
        #=======================================================================
        # if password1 != password2:
        #     response_data['error'] = '비밀번호가 동일하지 않습니다.'
        #     response_data['new_customer_show'] = 'new_customer_show'
        #     context={'response_data': response_data}
        #     return render(request, 'GoodData/social_login_confirm.html', context)
        #=======================================================================
            
        if username == '' or name == '' or address == '' or phone_number == '':
            response_data['error'] = '빈값은 저장할 수 없습니다. 프로필 사진을 선택했는지 확인해주세요.'
            response_data['new_customer_show'] = 'new_customer_show'
            context={'response_data': response_data}
            return render(request, 'GoodData/social_login_confirm.html', context)
        
        #=======================================================================
        # if length(RRN) != 6:
        #     response_data['error'] = "주민번호는 6자만 입력해주세요. '1999년 01월 01일' -> '990101'"
        #     response_data['new_customer_show'] = 'new_customer_show'
        #     context={'response_data': response_data}
        #     return render(request, 'GoodData/social_login_confirm.html', context)
        #=======================================================================
        
        profile_img = request.FILES.get('profile_img', None)
        
        if profile_img == None:
            profile_img = 'static/customer_img/profile_photo.jpg'
        
        if provider_name[0] == "naver":
            naver_uid_confirm = list(Customer.objects.values_list('naver_uid').all())
            print("naver_uid_confirm :: ", naver_uid_confirm)
            print()
            
            for i in range(0, length(naver_uid_confirm)):
                if naver_uid_confirm[i][0] == social_uid2:
                    response_data['error'] = "새로 가입하려는 naver 계정은 다른 아이디와 연동되어 있습니다. 기존 회원으로 로그인하세요."
                    response_data['new_customer_show'] = 'new_customer_show'
                    context={'response_data': response_data}
                    return render(request, 'GoodData/social_login_confirm.html', context)
                
            new_customer = Customer(
                cus_ID = username,
                #cus_PW = make_password(password1),
                cus_name = name,
                cus_address = address,
                #cus_RRN = RRN,
                cus_phone_number = phone_number,
                naver_uid = social_uid2,
                cus_image = profile_img,
                key_number = request.session.get('key'),
                )
            new_customer.save()
            
        elif provider_name[0] == "facebook":
            facebook_uid_confirm = list(Customer.objects.values_list('facebook_uid').all())
            print("facebook_uid_confirm :: ", facebook_uid_confirm)
            print()
            
            for i in range(0, length(facebook_uid_confirm)):
                if facebook_uid_confirm[i][0] == social_uid2:
                    response_data['error'] = "새로 가입하려는 facebook 계정은 다른 아이디와 연동되어 있습니다. 기존 회원으로 로그인하세요."
                    response_data['new_customer_show'] = 'new_customer_show'
                    context={'response_data': response_data}
                    return render(request, 'GoodData/social_login_confirm.html', context)
                
            new_customer = Customer(
                cus_ID = username,
                #cus_PW = make_password(password1),
                cus_name = name,
                cus_address = address,
                #cus_RRN = RRN,
                cus_phone_number = phone_number,
                facebook_uid = social_uid2,
                cus_image = profile_img,
                key_number = request.session.get('key'),
                )
            new_customer.save()
            
        elif provider_name[0] == "google":
            google_uid_confirm = list(Customer.objects.values_list('google_uid').all())
            print("google_uid_confirm :: ", google_uid_confirm)
            print()
            
            for i in range(0, length(google_uid_confirm)):
                if google_uid_confirm[i][0] == social_uid2:
                    response_data['error'] = "새로 가입하려는 google 계정은 다른 아이디와 연동되어 있습니다. 기존 회원으로 로그인하세요."
                    response_data['new_customer_show'] = 'new_customer_show'
                    context={'response_data': response_data}
                    return render(request, 'GoodData/social_login_confirm.html', context)
                
            new_customer = Customer(
                cus_ID = username,
                #cus_PW = make_password(password1),
                cus_name = name,
                cus_address = address,
                #cus_RRN = RRN,
                cus_phone_number = phone_number,
                google_uid = social_uid2,
                cus_image = profile_img,
                key_number = request.session.get('key'),
                )
            new_customer.save()
            
        
        user = Customer.objects.get(cus_ID=username)
        request.session['user'] = user.cus_ID
        print("33 request.session.get('user') :: ", request.session.get('user'))
        
        return redirect('campaign')
    
def Social_login_confirm(request):
    print("login_confirm Enter")
    print("33333333 request.session.get('key') :: ", request.session.get('key'))
    print("44444444 request.session.get('user') :: ", request.session.get('user'))
    print()
    social_info = SocialAccount.objects.values_list('provider', 'uid').filter(user=request.user)
    
    if social_info[0][0] == 'naver':
        print('naver Enter')
        naver_uid_all = Customer.objects.values_list('cus_ID', 'naver_uid').all()
        
        for count in range(0, length(naver_uid_all)):
            if social_info[0][1] == naver_uid_all[count][1]:
                request.session['user'] = naver_uid_all[count][0]
                return redirect('campaign')
        
    elif social_info[0][0] == 'facebook':
        print('facebook Enter')
        facebook_uid_all = Customer.objects.values_list('cus_ID', 'facebook_uid').all()
        
        for count in range(0, length(facebook_uid_all)):
            if social_info[0][1] == facebook_uid_all[count][1]:
                request.session['user'] = facebook_uid_all[count][0]
                return redirect('campaign')
        
    elif social_info[0][0] == 'google':
        print('google Enter')
        google_uid_all = Customer.objects.values_list('cus_ID', 'google_uid').all()
        
        for count in range(0, length(google_uid_all)):
            if social_info[0][1] == google_uid_all[count][1]:
                request.session['user'] = google_uid_all[count][0]
                return redirect('campaign')
            
    return render(request, "GoodData/social_login_confirm.html")


def Existing_cus_search(request):
    response_data = {}
    print("cus_search Enter")
    
    if request.method == "POST":
        cus_search = request.POST.get('search_username', None)
        print("cus_search :: ", cus_search)
        
        flag = 'false'
        
        if cus_search == "":
            response_data['error'] = "검색할 아이디를 입력해주세요."
            context = {'cus_search': cus_search, "response_data": response_data}
            return render(request, "GoodData/social_login_confirm.html", context)
        
        else:
            customer_entry = Customer.objects.all()
            customer_entry_cnt = customer_entry.values('cus_ID')
    
            customer_search = list(Customer.objects.values('cus_ID').all())
            
            for i in range(0, length(customer_entry_cnt)):
                if cus_search == customer_search[i].get('cus_ID'):
                    flag = 'true'
                    response_data['error'] = '가입이 완료된 아이디입니다.'
                    response_data['login_show'] = 'login_show'
                    break
            
            if flag == 'false':
                response_data['error'] = '회원가입된 아이디가 없습니다. 신규회원으로 등록하세요.'
                
            context = {'cus_search': cus_search, 'response_data': response_data}
            return render(request, "GoodData/social_login_confirm.html", context)
    
    
def Logout(request):
    #로그아웃 사용을 위한 함수
    print("Logout request.session['user'] ::::::::::::::: ", request.session['user'])
    customer_info = Customer.objects.get(cus_ID=request.session.get('user'))
    
    print("customer_info :: ", customer_info)
    
    customer_info.key_number = ""
    customer_info.save()
    
    auth.logout(request)
    return redirect('login')


def Campaign_fn(request):
    #캠페인리스트 페이지를 보여주기 위한 함수
    print("campaign 진입")
    
    social_uid1 = request.POST.get('social_uid1', None)
    print("social_uid1 :: ", social_uid1)
    print()
    
    if social_uid1 != None:
        provider_name = list(SocialAccount.objects.values_list('provider').get(uid=social_uid1))
        print("provider_name :: ", provider_name[0])
        print()
        
    if request.method == 'GET':
        cus_ID = request.session.get('user')
        print("request.session.get('user') :: ", cus_ID)
        print()
        
        img_list = Campaign.objects.all()
        context = {'img_list': img_list}
        return render(request, "GoodData/campaign_list.html", context)
    
    elif request.method == 'POST':
        response_data = {}
        
        cus_ID = request.session.get('user')
        print("POST1 request.session.get('user') :: ", cus_ID)
        print()
        
        cus_username = request.POST.get('cus_username', None)
        cus_password = request.POST.get('cus_password', None)
        
        if not (cus_username and cus_password):
            response_data['error'] = "아이디와 비밀번호를 모두 입력하세요."
            response_data['login_error'] = 'login_error'
            
        else:
            user_exist = list(Customer.objects.values("cus_ID").all())
            
            for i in range(0,length(user_exist)):
                
                if user_exist[i]["cus_ID"] != cus_username:
                    response_data['error'] = "아이디가 존재하지 않습니다."
                    response_data['login_error'] = 'login_error'
                    
                else:
                    user = Customer.objects.get(cus_ID=cus_username)
                    
                    if check_password(cus_password, user.cus_PW):
                        request.session['user'] = user.cus_ID
                        print("POST2 request.session.get('user') :: ", request.session.get('user'))
                        
                        customer_nfg_update = Customer.objects.get(cus_ID=request.session.get('user'))
                        
                        ###########################################################################################################
                        
                        if provider_name[0] == 'naver':
                            naver_uid_one = list(Customer.objects.values_list('cus_ID', 'naver_uid').filter(naver_uid=social_uid1))
                            print("naver_uid_one :: ", naver_uid_one)
                            print()
                            
                            if naver_uid_one == []:
                                naver_uid_exist = list(Customer.objects.values_list('cus_ID', 'naver_uid').get(cus_ID=request.session.get('user')))
                                
                                if social_uid1 == naver_uid_exist[1] or naver_uid_exist[1] == "":
                                    customer_nfg_update.naver_uid = social_uid1
                                    customer_nfg_update.save()
                                else:
                                    response_data['error'] = "입력한 아이디는 연동하고 있는 naver 아이디가 존재합니다. 연동할 다른 아이디를 검색하거나 신규회원으로 등록하세요."
                                    context = {'response_data': response_data}
                                    return render(request, "GoodData/social_login_confirm.html", context)
                                
                            else:
                                if cus_username != naver_uid_one[0][0]:
                                    response_data['error'] = "입력한 아이디는 연동하고 있는 naver 아이디가 존재합니다. 연동하고자하는 naver 아이디가 있다면 신규회원으로 등록하세요."
                                    context = {'response_data': response_data}
                                    return render(request, "GoodData/social_login_confirm.html", context)
                        
                        ###########################################################################################################
                        
                        elif provider_name[0] == 'facebook':
                            facebook_uid_one = list(Customer.objects.values_list('cus_ID', 'facebook_uid').filter(facebook_uid=social_uid1))
                            print("facebook_uid_one :: ", facebook_uid_one)
                            print()
                            
                            if facebook_uid_one == []:
                                facebook_uid_exist = list(Customer.objects.values_list('cus_ID', 'facebook_uid').get(cus_ID=request.session.get('user')))
                                
                                if social_uid1 == facebook_uid_exist[1] or facebook_uid_exist[1] == "":
                                    customer_nfg_update.facebook_uid = social_uid1
                                    customer_nfg_update.save()
                                else:
                                    response_data['error'] = "입력한 아이디는 연동하고 있는 facebook 아이디가 존재합니다. 연동할 다른 아이디를 검색하거나 신규회원으로 등록하세요."
                                    context = {'response_data': response_data}
                                    return render(request, "GoodData/social_login_confirm.html", context)
                                
                            else:
                                if cus_username != facebook_uid_one[0][0]:
                                    response_data['error'] = "입력한 아이디는 연동하고 있는 facebook 아이디가 존재합니다. 연동하고자하는 facebook 아이디가 있다면 신규회원으로 등록하세요."
                                    context = {'response_data': response_data}
                                    return render(request, "GoodData/social_login_confirm.html", context)
                            
                        ###########################################################################################################
                            
                        elif provider_name[0] == 'google':
                            google_uid_one = list(Customer.objects.values_list('cus_ID', 'google_uid').filter(google_uid=social_uid1))
                            print("google_uid_one :: ", google_uid_one)
                            print()
                            
                            if google_uid_one == []:
                                google_uid_exist = list(Customer.objects.values_list('cus_ID', 'google_uid').get(cus_ID=request.session.get('user')))
                                
                                if social_uid1 == google_uid_exist[1] or google_uid_exist[1] == "":
                                    customer_nfg_update.google_uid = social_uid1
                                    customer_nfg_update.save()
                                else:
                                    response_data['error'] = "입력한 아이디는 연동하고 있는 google 아이디가 존재합니다. 연동할 다른 아이디를 검색하거나 신규회원으로 등록하세요."
                                    context = {'response_data': response_data}
                                    return render(request, "GoodData/social_login_confirm.html", context)
                                
                            else:
                                if cus_username != google_uid_one[0][0]:
                                    response_data['error'] = "입력한 아이디는 연동하고 있는 google 아이디가 존재합니다. 연동하고자하는 google 아이디가 있다면 신규회원으로 등록하세요."
                                    context = {'response_data': response_data}
                                    return render(request, "GoodData/social_login_confirm.html", context)
                            
                        ###########################################################################################################
                            
                        img_list = Campaign.objects.all()
                        context = {'img_list': img_list}
                        return render(request, "GoodData/campaign_list.html", context)
                    else:
                        response_data['error'] = "비밀번호가 틀렸습니다."
                        response_data['login_error'] = 'login_error'
                        break
        
        cus_username = request.POST.get('cus_username', None)
        user = Customer.objects.get(cus_ID=cus_username)
        request.session['user'] = user.cus_ID
        
        cus_search = user.cus_ID
        context = {'cus_search': cus_search, 'response_data': response_data}
        return render(request, "GoodData/social_login_confirm.html", context)
    
    
def Project_fn(request, campaign_id):
    #프로젝트리스트 페이지를 보여주기 위한 함수
    print("project Enter111")
    cus_ID = request.session.get('user')
    print("request.session.get('user') :: ", cus_ID)
    print()
    
    response_data = {}
    project = Project.objects.values_list().filter(campaign_id=campaign_id)
    
    color_list = []
         
    for i in range(0, length(project)):
        color_select = list(Campaign.objects.values_list("background_color").get(cam_id=project[i][1]))
        color_list.append(color_select[0])
             
    print("color_list :: ", color_list)
     
    project_list = []
     
    for i in range(0, length(color_list)):
        result_list = []
        result_list.append(project[i])
        result_list.append(color_list[i])
         
        project_list.append(result_list)
         
    if length(project) == 0:
        img_list = Campaign.objects.all()
        response_data['error'] = '해당 캠페인에 대한 프로젝트 내용이 없습니다. 다른 캠페인을 선택하세요.'
        context = {'img_list': img_list, 'response_data': response_data}
        return render(request, 'GoodData/campaign_list.html', context)
    else:
        context = {'project': project_list}
        return render(request, 'GoodData/project_list.html', context)


def Project_all(request):
    #모든프로젝트리스트 페이지를 보여주기 위한 함수(footer 전용)
    print("all project Enter")
    cus_ID = request.session.get('user')
    print("request.session.get('user') :: ", cus_ID)
    print()
    
    project_test = list(Project.objects.values_list().all())
    
    color_list = []
        
    for i in range(0, length(project_test)):
        color_select = list(Campaign.objects.values_list("background_color").get(cam_id=project_test[i][1]))
        color_list.append(color_select[0])
        
    print("color_list :: ", color_list)
    
    project_list = []
    
    for i in range(0, length(color_list)):
        result_list = []
        result_list.append(project_test[i])
        result_list.append(color_list[i])
        
        project_list.append(result_list)
        
    context = {'project': project_list}
    return render(request, 'GoodData/project_list.html', context)
    
    
def Project_detail(request, campaign_id, project_id):
    #프로젝트상세 페이지를 보여주기 위한 함수
    cus_ID = request.session.get('user')
    print("request.session.get('user') :: ", cus_ID)
    print()
        
    project_detail = Project_Detail.objects.filter(project_id=project_id)
    print("111 project_detail :: ", project_detail)
    print()
        
    project_video_cnt = project_detail.values('pro_detail_id')
    #===========================================================================
    # print("222 length(project_video_cnt) : ", length(project_video_cnt))
    # print()
    #===========================================================================
        
    if length(project_video_cnt) == 0:
        response_data = {}
        response_data['error'] = "프로젝트 영상이 없습니다. 다른 프로젝트를 선택하세요."
        project = Project.objects.filter(campaign_id=campaign_id)
        context = {'project': project, 'response_data': response_data}
        return render(request, 'GoodData/project_list.html', context)
    else :
        response_data = {}
        change_flag = 0
        full_flag = 0
        
        random_list = []
            
        for i in range(0, length(project_video_cnt)):
            a = random.randint(1, length(project_video_cnt))
            while a in random_list:
                a = random.randint(1, length(project_video_cnt))
            random_list.append(a)
                
        print("333 random_list :: ", random_list)
        print()
        
        for i in range(0, length(project_video_cnt)):
            one_project_confirm = list(Project_Detail.objects.values_list('pro_order', 'user1', 'user2', 'user3', 'user4', 'user5').get(pro_order=random_list[i], project_id=project_id))
            print('444 one_project_confirm!!! :: ', one_project_confirm)
         
            if '' in one_project_confirm:
                if cus_ID not in one_project_confirm:
                    random_result = one_project_confirm[0]
                    change_flag += 1
                    break
        
        if change_flag == 0:
            print("All row cus_ID have1111111")
            response_data['error'] = "분류를 완료한 캠페인입니다. 다른 프로젝트를 선택해주세요."
            project = Project.objects.values_list().filter(campaign_id=campaign_id)
            
            color_list = []
         
            for i in range(0, length(project)):
                color_select = list(Campaign.objects.values_list("background_color").get(cam_id=project[i][1]))
                color_list.append(color_select[0])
                     
            print("color_list :: ", color_list)
             
            project_list = []
             
            for i in range(0, length(color_list)):
                result_list = []
                result_list.append(project[i])
                result_list.append(color_list[i])
                 
                project_list.append(result_list)
        
            context = {'project': project_list, 'response_data': response_data}
            return render(request, 'GoodData/project_list.html', context)
            
        print("555 random_result :: ", random_result)
        print()
            
        video_info = Project_Detail.objects.values().get(pro_order=random_result, project_id=project_id)
        print("666 video_info : ", video_info)
        print()
        
        #####################################################################################################
        if request.method == "GET":
            print("GETGETGETGETGETGETGETGETGETGETGETGETGETGET Enter")
            
            context = {'video_info': video_info, 'cus_ID': cus_ID}
            print("GET End")
            print()
            
            return render(request, 'GoodData/project_detail.html', context)
        #####################################################################################################
        elif request.method == "POST":
            print("POSTPOSTPOSTPOSTPOSTPOSTPOSTPOSTPOSTPOSTPOST Enter")
            
            pro_detail_id = request.POST.get('pro_detail_id', None)
            pro_order = request.POST.get('pro_order', None)
            project_id = request.POST.get('project_id', None)
            YN = request.POST.get('YN', None)
                
            project_detail_update = Project_Detail.objects.get(pro_detail_id=pro_detail_id)
            customer_update = Customer.objects.get(cus_ID=cus_ID)
            print("customer_update :: ", customer_update.point)
            customer_update.point += 10
            customer_update.save()
            
            if project_detail_update.user1 == '':
                project_detail_update.user1 = cus_ID
                project_detail_update.YN1 = YN
                project_detail_update.save()
            elif project_detail_update.user2 == '':
                project_detail_update.user2 = cus_ID
                project_detail_update.YN2 = YN
                project_detail_update.save()
            elif project_detail_update.user3 == '':
                project_detail_update.user3 = cus_ID
                project_detail_update.YN3 = YN
                project_detail_update.save()
            elif project_detail_update.user4 == '':
                project_detail_update.user4 = cus_ID
                project_detail_update.YN4 = YN
                project_detail_update.save()
            elif project_detail_update.user5 == '':
                project_detail_update.user5 = cus_ID
                project_detail_update.YN5 = YN
                project_detail_update.save()
                
            response_data = {}
            change_flag = 0
                
            random_list = []
                
            for i in range(0, length(project_video_cnt)):
                a = random.randint(1, length(project_video_cnt))
                while a in random_list:
                    a = random.randint(1, length(project_video_cnt))
                random_list.append(a)
                    
            print("777 random_list :: ", random_list)
            print()
                
            for i in range(0, length(project_video_cnt)):
                    
                one_project_confirm = list(Project_Detail.objects.values_list('pro_order', 'user1', 'user2', 'user3', 'user4', 'user5').get(pro_order=random_list[i], project_id=project_id))
                print("888 one_project_confirm :: ", one_project_confirm)
                
                if '' in one_project_confirm:
                    if cus_ID not in one_project_confirm:
                        random_result = one_project_confirm[0]
                        change_flag += 1
                        break
                    
            if change_flag == 0:
                print("All row cus_ID have2222222")
                response_data['error'] = "분류를 완료한 캠페인입니다. 다른 프로젝트를 선택해주세요."
                project = Project.objects.values_list().filter(campaign_id=campaign_id)
                
                color_list = []
         
                for i in range(0, length(project)):
                    color_select = list(Campaign.objects.values_list("background_color").get(cam_id=project[i][1]))
                    color_list.append(color_select[0])
                         
                print("color_list :: ", color_list)
                 
                project_list = []
                 
                for i in range(0, length(color_list)):
                    result_list = []
                    result_list.append(project[i])
                    result_list.append(color_list[i])
                     
                    project_list.append(result_list)
                
                context = {'project': project_list, 'response_data': response_data}
                return render(request, 'GoodData/project_list.html', context)
                
            print("999 random_result :: ", random_result)
            print()
            
            video_info = Project_Detail.objects.values().get(pro_order=random_result, project_id=project_id)
            print("000 video_info : ", video_info)
            print()
            
            context = {'video_info': video_info, 'cus_ID': cus_ID, 'campaign_id': campaign_id}
            print("POST End")
            print()
            
            return render(request, 'GoodData/project_detail.html', context)
        
        
def Donation(request):
    #기부현황 페이지를 보여주기 위한 함수
    print("donation 진입")

    cus_ID = request.session.get('user')
    print("request.session.get('user') :: ", cus_ID)
    print()
    
    point = list(Customer.objects.values_list("cus_ID", "point").all().order_by('point'))
    print("point : ", point)
    print()
    
    customer_point = Customer.objects.values().get(cus_ID=cus_ID)
    print("customer_point : ", customer_point)
    print()
    
    friends_list = []
    
    friends_info = list(User_Friends.objects.values_list("friend_id", "friend_name").filter(cus_ID=cus_ID).order_by('-input_date'))
    print("friends_info : ", friends_info)
    print()
    
    for count in range(0, length(friends_info)):
        cus_info = Customer.objects.values_list("cus_ID", "cus_name", "point", "cus_image").filter(cus_ID=friends_info[count][0])
        friends_list.append(cus_info[0])
    
    context = {'customer_point': customer_point, 'point': point, 'friends_list': friends_list}
    return render(request, "GoodData/donation.html", context)


def Information(request):
    #내정보 페이지를 보여주기 위한 함수
    print("information 진입")
    cus_ID = request.session.get('user')
    print("request.session.get('user') :: ", cus_ID)
    print()
    
    customer_info = Customer.objects.values().get(cus_ID=cus_ID)
    context = {'customer_info': customer_info}
    return render(request, "GoodData/information.html", context)


def Information_update(request):
    #계정회원변경 페이지를 보여주기 위한 함수
    print("information_update 진입")
    cus_ID = request.session.get('user')
    print("request.session.get('user') :: ", cus_ID)
    print()
    
    response_data = {}
    
    if request.method == "GET":
        customer_info = Customer.objects.values().get(cus_ID=cus_ID)
        context = {'customer_info': customer_info}
        return render(request, "GoodData/information_update.html", context)
    
    elif request.method == "POST":
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        name = request.POST['name']
        address = request.POST['address']
        #RRN = request.POST['RRN']
        phone_number = request.POST['phone_number']
        password_confirm = request.POST['password_confirm']

        if password_confirm != "password_confirm":
            if password1 != password2:
                response_data['error'] = '비밀번호가 동일하지 않습니다.'
                customer_info = Customer.objects.values().get(cus_ID=cus_ID)
                context = {'customer_info': customer_info, 'response_data': response_data}
                return render(request, 'GoodData/information_update.html', context)
            
            if username == '' or password1 == '' or password2 == '' or name == '' or address == '' or phone_number == '':
                response_data['error'] = '빈값은 저장할 수 없습니다.'
                customer_info = Customer.objects.values().get(cus_ID=cus_ID)
                context = {'customer_info': customer_info, 'response_data': response_data}
                return render(request, 'GoodData/information_update.html', context)
        
        #=======================================================================
        # if length(RRN) != 6:
        #     response_data['error'] = "주민번호는 6자만 입력해주세요. '1999년 01월 01일' -> '990101'"
        #     customer_info = Customer.objects.values().get(cus_ID=cus_ID)
        #     context = {'customer_info': customer_info, 'response_data': response_data}
        #     return render(request, 'GoodData/information_update.html', context)
        #=======================================================================
        
        profile_img = request.FILES.get('profile_img', None)
        
        if profile_img == None:
            profile_img = 'static/customer_img/profile_photo.jpg'
            
        before_customer = Customer.objects.get(cus_ID=cus_ID)
        
        if password_confirm != "password_confirm":
            before_customer.cus_PW = make_password(password1)
            
        before_customer.cus_name = name
        before_customer.cus_address = address
        #before_customer.cus_RRN = RRN
        before_customer.cus_phone_number = phone_number
        before_customer.cus_image = profile_img
        before_customer.save()
        
        customer_info = Customer.objects.values().get(cus_ID=cus_ID)
        context = {'customer_info': customer_info, 'response_data': response_data}
        return render(request, "GoodData/information.html", context)
    
    
def Information_delete(request):
    #계정회원탈퇴 페이지를 보여주기 위한 함수
    print("information_delete 진입")
    cus_ID = request.session.get('user')
    print("request.session.get('user') :: ", cus_ID)
    print()
    
    if request.method == "GET":
        customer_info = Customer.objects.values().get(cus_ID=cus_ID)
        context = {'customer_info': customer_info}
        return render(request, "GoodData/information_delete.html", context)
    elif request.method == "POST":
        customer_info = Customer.objects.get(cus_ID=cus_ID)
        friend_info1 = User_Friends.objects.filter(cus_ID=cus_ID)
        friend_info2 = User_Friends.objects.filter(friend_id=cus_ID)
        
        customer_info.delete()
        friend_info1.delete()
        friend_info2.delete()
        
        auth.logout(request)
        return redirect('login')
        
    
def User_friends(request):
    print("user_friends Enter")
    
    return render(request, "GoodData/user_friends.html")
    
    
def User_friends_search(request):
    print("user_friends_search Enter")
    response_data = {}
    
    cus_ID = request.session.get('user')
    print("request.session.get('user') :: ", cus_ID)
    print()
    
    user_search = request.POST.get("user_search", None)
    print("uesr_search :: ", user_search)
    print()
    
    if cus_ID == user_search:
        response_data["error"] = "자신의 정보는 친구 등록할 수 없습니다. 다른 아이디를 검색하세요."
        context = {"user_search": user_search, "response_data": response_data}
        return render(request, "GoodData/user_friends.html", context)
    
    flag = 'false'
    
    if user_search == "":
        response_data["error"] = "빈값은 검색할 수 없습니다. 사용자 ID를 검색해주세요."
        context = {"response_data": response_data}
        return render(request, "GoodData/user_friends.html", context)
    
    else:
        user_all = list(Customer.objects.values_list("cus_ID").all())
        
        for i in user_all:
            if user_search == i[0]:
                flag = 'true'
                user_info = list(Customer.objects.values_list("cus_ID", "cus_name", "cus_address", "cus_image").get(cus_ID=user_search))
                print("user_info :: ", user_info)
                print()
                user_enrollment = "user_enrollment"
                
                context = {"user_search": user_search, "user_info": user_info, "user_enrollment": user_enrollment}
                break
            
        if flag == 'false':
            response_data["error"] = "검색한 ID와 일치하는 사용자가 없습니다. 다시 입력해주세요."
            response_data["search_result_hide"] = "search_result_hide"
            context = {"user_search": user_search, "response_data": response_data}
            return render(request, "GoodData/user_friends.html", context)
        
        return render(request, "GoodData/user_friends.html", context)
    
    
def User_friends_enrollment(request):
    print("user_friends_enrollment Enter")
    response_data={}
    
    cus_ID = request.session.get('user')
    print("request.session.get('user') :: ", cus_ID)
    print()
    
    user_enrollment = request.POST.get("user_enrollment", None)
    user_ID = request.POST.get("user_ID", None)
    print("user_enrollment :: ", user_enrollment)
    print("user_ID :: ", user_ID)
    
    if cus_ID == user_ID:
        response_data["error"] = "자신의 정보는 친구 등록할 수 없습니다. 다른 아이디를 검색하세요."
        context = {"user_search": user_ID, "response_data": response_data}
        return render(request, "GoodData/user_friends.html", context)
    
    if user_enrollment == "user_enrollment":
        
        user_search = list(User_Friends.objects.values_list().filter(cus_ID=cus_ID, friend_id=user_ID))
        print("user_search :: ", user_search)
        print()
        
        if user_search == []:
            cus_info = list(Customer.objects.values_list("id", "cus_ID", "cus_name").get(cus_ID=cus_ID))
            friend_info = list(Customer.objects.values_list("cus_ID", "cus_name").get(cus_ID=user_ID))
            
            friend_enrollment = User_Friends(
                cus_idx_id = cus_info[0],
                cus_ID     = cus_info[1],
                cus_name   = cus_info[2],
                friend_id   = friend_info[0],
                friend_name = friend_info[1],
                )
            friend_enrollment.save()
            
            return redirect('donation')
        
        else:
            response_data["error"] = "현재 검색한 아이디는 이미 친구 등록된 계정입니다. 다른 아이디를 검색해주세요."
            context={"response_data": response_data}
            return render(request, "GoodData/user_friends.html", context)
        
    else:
        response_data["error"] = "검색한 ID와 일치하는 사용자가 없어 등록할 수 없습니다. 다시 검색해주세요."
        context={"response_data": response_data}
        return render(request, "GoodData/user_friends.html", context)
    

def App_version_info(request):
    return render(request, "GoodData/app_version_info.html")


def Question(request):
    return render(request, "GoodData/question.html")


def Notice_fn(request):
    print("Notice_fn Enter")
    notice_list = list(Notice.objects.values_list().all().order_by('-input_date'))
    
    print("notice_list :: ", notice_list)
    print("notice_list[0] :: ", notice_list[0])
    context={"notice_list": notice_list}
    return render(request, "GoodData/notice.html", context)


def Notice_detail(request, notice_id):
    print("Notice_detail Enter")
    
    notice_detail = list(Notice.objects.values_list().get(notice_id=notice_id))
    
    print("notice_detail :: ", notice_detail)
    
    context={"notice_detail": notice_detail}
    
    return render(request, "GoodData/notice_detail.html", context)
    

def Privacy_policy(request):
    return render(request, "GoodData/privacy_policy.html")


def Open_source_license(request):
    return render(request, "GoodData/open_source_license.html")


def Etc(request):
    return render(request, "GoodData/etc.html")
    
    
def App_version(request, type):
    print("App_version Enter")
    print("type :: ", type)
    print()
    
    if type == 'android':
        app_version_all = list(app_version.objects.values_list('type', 'version').get(type=type))
        
        print("app_version_all :: ", app_version_all)
        print("app_version_all[0] :: ", app_version_all[0])
        print("app_version_all[1] :: ", app_version_all[1])
        print()
        
        return HttpResponse(app_version_all[1], 'application/json')
    
    elif type == 'ios':
        app_version_all = list(app_version.objects.values_list('type', 'version').get(type=type))
        
        print("app_version_all :: ", app_version_all)
        print("app_version_all[0] :: ", app_version_all[0])
        print("app_version_all[1] :: ", app_version_all[1])
        print()
        
        return JsonResponse({'db_version': int(app_version_all[1])})
    
    
def IOS_get_info(request, key_number):
    print("ios_get_info Enter")
    user_info = list(Customer.objects.values_list('cus_ID', 'key_number').filter(key_number=key_number))
    print("ios_get_info user_info :: ", user_info)
    print()
    
    if user_info == []:
        flag = 0
    else:
        flag = 1

    request.session['key'] = key_number
    print("ios_get_info request.session['key'] :: ", request.session['key'])
    print("ios_get_info request.session.get('key') :: ", request.session.get('key'))
    print()
    
    return JsonResponse({'result': int(flag)})
    
    
def Login_auto(request, key_number):
    print("Login_auto Enter")
    print("login_auto key_number :: ", key_number)
    
    user_info = list(Customer.objects.values_list("cus_ID", "key_number").get(key_number=key_number))
    print("login_auto user_info[0] :: ", user_info[0])
    print()
    request.session['user'] = user_info[0]
    
    return redirect('campaign')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
