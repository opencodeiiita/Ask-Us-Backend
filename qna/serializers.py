from rest_framework import serializers
from .models import Answer, Question


class QuestionSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    class Meta:
        model = Question
        fields = "__all__"


class AnswerSerializer(serializers.ModelSerializer):
    question = serializers.ReadOnlyField(source='question.id')
    author = serializers.ReadOnlyField(source='author.username')
    class Meta:
        model = Answer
        fields = "__all__"

