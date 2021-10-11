
# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from qna.models import Question, Answer
from qna.serializers import QuestionSerializer, AnswerSerializer


@api_view(['GET', 'POST'])
def question_list(request):
    if request.method == 'GET':
        questions = Question.objects.all()
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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


@api_view(['GET', 'POST'])
def answer_list(request, **kwargs):
    _id = kwargs.get("id")
    if request.method == 'GET':
        data = AnswerSerializer(Answer.objects.all(), many=True).data
        return Response(data)
    elif request.method == 'POST':
        request.data["question"]=_id
        serializer = AnswerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


