from django.contrib import admin #Import the admin
from models import todo #Import our todo Model.
 
admin.site.register(todo) #Register the model with the admin
