
# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view

from rest_framework.response import Response

from qna.models import Question
from qna.serializers import QuestionSerializer


@api_view(['GET', 'PUT', 'DELETE'])
def question_detail(request, **kwargs):
    _id = kwargs.get("id")
    try:
        question = Question.objects.get(id=_id)
    except Question.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        data = QuestionSerializer(question).data
        return Response(data)
    elif request.method == "PUT":
        data = request.data
        ques_serializer = QuestionSerializer(question, data=data)
        if ques_serializer.is_valid():
            ques_serializer.save()
            return Response(ques_serializer.data, status=status.HTTP_200_OK)
        return Response(ques_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        question.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
