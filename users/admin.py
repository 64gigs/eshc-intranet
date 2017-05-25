from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User


from users.models import Profile
from leases.models import Lease

admin.site.unregister(User)

class ProfileInLine(admin.StackedInline):
	model = Profile
	can_delete = False

class LeaseInLine(admin.StackedInline):
	model = Lease
	extra = 0

class UserAdmin(BaseUserAdmin):
	inlines = [LeaseInLine, ProfileInLine, ]

	def ref_number(self, obj):
		try:
			return obj.profile.ref_number
		except Profile.DoesNotExist:
			return ''

	list_display = BaseUserAdmin.list_display + ('ref_number', )

admin.site.register(User, UserAdmin)
