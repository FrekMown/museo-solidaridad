"""museo_solidaridad URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.shortcuts import render
import pandas as pd
import os
from museo_solidaridad.settings import STATIC_DIR
from .escenas_youtube import escenas 

def get_parallax_pics():
    df_imgs = pd.read_csv(os.path.join(STATIC_DIR, 'df_imgs2.csv'), index_col=0).dropna(subset=['parallax'])
    return [os.path.join('/static', 'img_new', df_imgs.loc[idx, 'folder'], df_imgs.loc[idx, 'file']) for idx in df_imgs.index]

def get_gallery_pics():
    df_imgs = pd.read_csv(os.path.join(STATIC_DIR, 'df_imgs2.csv'), index_col=0).dropna(subset=['include'])
    return df_imgs[['folder','file']].groupby('folder')['file'].apply(list).to_dict()

def index(request):
    dict_out = {
        'parallax': get_parallax_pics(),
        'gallery': get_gallery_pics(),
        'escenas': escenas,
    }
    print(dict_out['escenas'])
    return render(request, 'index.html', dict_out)
    


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
]
