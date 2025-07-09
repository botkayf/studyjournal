from django.urls import path

from . import views


app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('topics/', views.topics, name='topics'),
    path('topics/<int:topic_id>', views.topic_entries, name='topic_entries'),
    path('new_topic/', views.new_topic, name = 'new_topic'),
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
    path('edit_topic/<int:topic_id>/', views.edit_topic, name='edit_topic'),
    path('delete_topic/<int:topic_id>/', views.delete_topic_page, name='delete_topic_page'),
    path('delete_topic/<int:topic_id>/confirm/', views.delete_topic_confirm, name='delete_topic_confirm'),
    path('delete_entry/<int:entry_id>/', views.delete_entry_page, name='delete_entry_page'),
    path('delete_entry/<int:entry_id>/confirm/', views.delete_entry_confirm, name='delete_entry_confirm'),

]