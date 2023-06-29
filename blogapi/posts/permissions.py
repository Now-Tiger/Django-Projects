from rest_framework import permissions


class isAutherOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj) -> bool:
        # read only permission allowed to any usesr
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # write permission are only allowed to author of the post
        return obj.author == request.user