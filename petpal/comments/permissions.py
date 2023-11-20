from rest_framework import permissions
#Only the specific shelter and pet seeker can comment on their application.

class IsApplicationRelated(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated()
    def has_object_permission(self, request, view, obj):
        return obj.shelter == request.user or obj.seeker == request.user