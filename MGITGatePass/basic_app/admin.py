from django.contrib import admin
from basic_app.models import StudentProfileInfo,GatepassRequests,AllGatepassRequests

# Register your models here.

admin.site.register([StudentProfileInfo,GatepassRequests,AllGatepassRequests])

