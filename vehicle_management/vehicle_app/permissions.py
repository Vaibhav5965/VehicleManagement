from rest_framework import permissions


class RoleBasedPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method == 'POST':
            return bool(request.user and request.user.is_authenticated and request.user.user_type == 'SA')
        return bool(request.user and request.user.is_authenticated)

    # delete, retreive
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return bool(request.user and request.user.is_authenticated and request.user.user_type in ['SA', 'AD'])

