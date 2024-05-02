from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Course
from .serializers import CourseSerializer


class ForgeCourseViewSet(viewsets.ModelViewSet):
    """API endpoint позволяющий создавать просматривать и редактировать курсы"""
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    authentication_classes = (TokenAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        """Создание курса с привязкой автора"""
        serializer.save(author_uuid=self.request.user)

    def get_queryset(self):
        """Получение списка курсов принадлежащих автору"""
        user = self.request.user
        # Используя обратную связь получаем все связанные с user объекты из таблицы Courses
        queryset = Course.objects.filter(author_uuid=user)
        return queryset
