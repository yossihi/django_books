"""
appppppppppppppppppppppppppppppppppplication
"""
from django.contrib import admin
from django.urls import path
from base import views

urlpatterns = [
    path('', views.index),
    path('books/', views.all_books),
    path('books/<int:id>', views.all_books)
]
