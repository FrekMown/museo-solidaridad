from django.contrib import admin
from django.urls import path
from django.shortcuts import render
import pandas as pd
import os
from personal.settings import BASE_DIR
from museo_solidaridad.escenas_youtube import escenas 

STATIC_DIR = os.path.join(BASE_DIR, 'static', 'museo_solidaridad')

def get_parallax_pics():
    df_imgs = pd.read_csv(os.path.join(STATIC_DIR, 'df_imgs2.csv'), index_col=0).dropna(subset=['parallax'])
    return [os.path.join('/static', 'museo_solidaridad', 'img_new', df_imgs.loc[idx, 'folder'], df_imgs.loc[idx, 'file']) for idx in df_imgs.index]

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
    return render(request, 'museo_solidaridad/index.html', dict_out)
    


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
]
