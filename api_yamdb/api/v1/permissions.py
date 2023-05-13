from rest_framework import permissions


class Everyone(permissions.BasePermission):
    def has_permission(self, request, view):
        return (request.method in permissions.SAFE_METHODS)

    def has_object_permission(self, request, view, obj):
        return (request.method in permissions.SAFE_METHODS)


class IsUser(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        return (user.is_authenticated and user.is_user)

    def has_object_permission(self, request, view, obj):
        user = request.user
        return (user.is_authenticated
                and user.is_user
                and user == obj.author)


class IsModerator(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        return user.is_authenticated and user.is_moderator

    def has_object_permission(self, request, view, obj):
        user = request.user
        return user.is_authenticated and user.is_moderator


class IsAdminOrSuperuser(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        return user.is_authenticated and (user.is_admin
                                          or user.is_superuser)

    def has_object_permission(self, request, view, obj):
        user = request.user
        return user.is_authenticated and (user.is_admin
                                          or user.is_superuser)
