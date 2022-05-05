"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

import blog.views  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog.views.home, name = "home"),
    path('post/<int:id>/', blog.views.detail, name="detail"),
    path('new', blog.views.new, name = 'new'),
    path('create', blog.views.create, name = 'create'),
    path('post/edit/<int:id>', blog.views.edit, name = 'edit'),
    path('post/update/<int:id>', blog.views.update, name = 'update'),
    # update 경로인 path 함수로 요청이 들어올 경우 조금 특이하다. 
    # post/update/<int:id> 를 위한 html이 따로 있지 않다. 
    # update url로 요청과 데이터가 들어오면 view가 그걸 처리해서, 다른 url로 redirect시켜준다.
    # 결론 -> 요청은 항상 특정한 url로 받는구나. html이나 프론트가 없는 url도 있구나. 이런 url은 요청을 받기 위한 url이구나.
    path('post/delete/<int:id>', blog.views.delete, name = 'delete'),
]
