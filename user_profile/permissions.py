from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        '''Разрешение на запись только владельцу'''
        return obj.owner== request.user


class LikedOrReadOlnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        '''Разрешение на запись только владельцу'''
        return obj.up_liked_by == request.user or obj.dawn_liked_by == request.user