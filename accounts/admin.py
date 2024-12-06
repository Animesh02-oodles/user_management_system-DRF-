from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'role', 'is_active')  # Display role directly
    list_filter = ('role', 'is_active')  # Use 'role' for filtering
    search_fields = ('username', 'email')
    ordering = ('username',)

    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Permissions', {'fields': ('role', 'is_active')}),
        ('Personal Info', {'fields': ('gender', 'age')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'role', 'is_active'),
        }),
    )

    def save_model(self, request, obj, form, change):
        """
        Automatically update computed properties (if needed) based on the selected role.
        """
        # Ensure that the role field is the source of truth, so no separate flags are needed.
        super().save_model(request, obj, form, change)

# Register the CustomUser model with the customized admin interface
admin.site.register(CustomUser, CustomUserAdmin)
