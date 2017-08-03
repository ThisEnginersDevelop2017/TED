from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from . import views
from .views import (
    DeveloperCreation,
    DeveloperUpdate,
    DeveloperDelete,
    TemplateCreation,
    TemplateUpdate,
    TemplateDelete,
    contact,
    about,
)
urlpatterns = [
    # urls del modelo developer
    url(r'^$', views.principal, name='principal'),
    # url(r'^inicio/',views.inicio, name='inicio'),
    url(r'^Lista/developers/', views.DeveloperList, name='developer_list'),
    url(r'^developer/(?P<pk>[0-9]+)/$',
        views.DeveloperDetail,
        name='developer_detail'),
    url(r'^developer/Nuevo',
        DeveloperCreation.as_view(),
        name="developer_new"),
    url(r'^Editar/(?P<pk>\d+)',
        login_required(DeveloperUpdate.as_view()),
        name='edit'),
    url(r'^Borrar/(?P<pk>\d+)',
        login_required(DeveloperDelete.as_view()),
        name='delete'),

    # urls del modelo templates
    url(r'^Lista/templates/',
        views.TemplateList,
        name='template_list'),
    url(r'^template/(?P<pk>[0-9]+)/$',
        views.TemplateDetail,
        name='template_detail'),
    url(r'^template/Nuevo',
        TemplateCreation.as_view(),
        name="template_new"),
    url(r'^template/Editar/(?P<pk>\d+)',
        login_required(TemplateUpdate.as_view()),
        name='template_edit'),
    url(r'^template/Borrar/(?P<pk>\d+)',
        login_required(TemplateDelete.as_view()),
        name='template_delete'),

    #url de ajax
    url(r'^template/modal_ajax/$', views.ModalAjaxView),

    #urls de la pagina en general
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^about/$', about, name='about'),

]
