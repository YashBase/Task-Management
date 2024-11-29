from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin
from django.core.mail import send_mail
from django.urls import path
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils.html import format_html
from django import forms
from .models import OAuthKey, UserProfile
from django.conf import settings

# Unregister the default User admin
admin.site.unregister(User)

# Form for sending an invitation
class InvitationForm(forms.Form):
    email = forms.EmailField(label="Recipient's Email", required=True)

# Inline for UserProfile
class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'Profiles'

# Admin for OAuthKey - Avoid multiple registration
if not admin.site.is_registered(OAuthKey):
    @admin.register(OAuthKey)
    class OAuthKeyAdmin(admin.ModelAdmin):
        list_display = ('client_id', 'created_at')
        list_filter = ('created_at',)
        search_fields = ('client_id',)

# Custom User Admin with Send Invitation Feature
@admin.register(User)
class CustomUserAdmin(DefaultUserAdmin):
    inlines = [UserProfileInline]
    list_display = ('username', 'email', 'is_staff', 'send_invitation')
    search_fields = ('username', 'email')

    def send_invitation(self, obj):
        if not obj.email:
            return "No Email"
        return format_html(
            '<a class="btn btn-primary" href="{}">Send Invite</a>',
            f"/admin/users/send_invite/{obj.id}/"
        )
    send_invitation.short_description = 'Send Invitation'

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('send_invite/<int:user_id>/', self.admin_site.admin_view(self.send_invitation_view), name="send_invite"),
        ]
        return custom_urls + urls

    def send_invitation_view(self, request, user_id):
        if request.method == "POST":
            form = InvitationForm(request.POST)
            if form.is_valid():
                email = form.cleaned_data['email']
                # Generate a registration link (customize this URL)
                registration_link = f"{settings.SITE_URL}/register/?invited_by={email}"
                
                # Send an email
                send_mail(
                    "You're Invited to Register",
                    f"Please use the following link to register: {registration_link}",
                    settings.DEFAULT_FROM_EMAIL,
                    [email],
                    fail_silently=False,
                )
                self.message_user(request, f"Invitation sent to {email}.")
                return HttpResponseRedirect("../")
        else:
            form = InvitationForm()

        return render(request, "admin/send_invitation.html", {"form": form})

# Optional: Register UserProfile independently if necessary
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'invited_by')
    search_fields = ('user__username', 'invited_by')
