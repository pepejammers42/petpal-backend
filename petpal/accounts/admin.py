from django.contrib import admin
from .models import AccountType, Seeker, Shelter

from django.contrib.auth.models import Group

# from customauth.models import AccountType
# Now register the new UserAdmin...
admin.site.register(AccountType)
admin.site.register(Shelter)
admin.site.register(Seeker)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
admin.site.unregister(Group)
