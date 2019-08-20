from rest_framework import permissions
import json


class Model:
    class IsAuthenticated(permissions.BasePermission):
        def has_permission(self, request, view):
            return bool(request.user)

    class IsOwnerOrReadOnly(permissions.BasePermission):
        def has_object_permission(self, request, view, obj):
            if request.method in permissions.SAFE_METHODS:
                return True

            return obj.user == request.user

    class IsAuthenticatedOrReadOnly(permissions.BasePermission):
        def has_permission(self, request, view):
            if request.method in permissions.SAFE_METHODS:
                return True

            return request.user is not None

    class IsAuthenticatedOrAdminOnly(permissions.BasePermission):
        def has_permission(self, request, view):
            if request.method in permissions.SAFE_METHODS:
                return bool(request.user.is_staff)

            return bool(request.user)

    class IsAdminOrReadOnly(permissions.BasePermission):
        def has_permission(self, request, view):
            if request.method in permissions.SAFE_METHODS:
                return True

            return bool(request.user.is_staff)


class Document:
    class IsOwnerOrReadOnly(permissions.BasePermission):
        def has_object_permission(self, request, view, obj):
            if request.method in permissions.SAFE_METHODS:
                return True

            return obj.user['id'] == request.user.pk

    class IsAuthenticatedOrReadOnly(permissions.BasePermission):
        def has_permission(self, request, view):
            if request.method in permissions.SAFE_METHODS:
                return True

            if not request.user.is_anonymous:
                jsonbody = json.loads(request.body.decode('utf-8'))
                jsonbody['user'] = {
                    'id': request.user.pk,
                    'username': request.user.username,
                    'email': request.user.email
                }
                request.body = json.dumps(jsonbody).encode('utf-8')
                print(request.body)
                return True

            return False

    class IsAuthenticatedOrAdminOnly(permissions.BasePermission):
        def has_permission(self, request, view):
            if request.method in permissions.SAFE_METHODS:
                return bool(request.user.is_staff)

            return bool(request.user)
