# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from qna.models import Question, Answer
from qna.serializers import QuestionSerializer, AnswerSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.generics import ListAPIView

@api_view(['GET'])
def root(request):
    endpoints = [
        {
        "request": "GET",
        "url": "question/all/",
        "description": "Retrieves all question"
        },
        {
        "request": "POST",
        "url": "question/new/",
        "description": "Post a question"
        },
        {
        "request": "GET,PUT,DELETE",
        "url": "question/{qid}",
        "description": "Get, edit ,delete a question with its id"
        },
        {
        "request": "GET",
        "url": "question/{qid}/answer/all/",
        "description": "Retrieves all answers for a question with its id"
        },
        {
        "request": "POST",
        "url": "question/{qid}/answer/new/",
        "description": "Post answer for a question with its id"
        },
        {
        "request": "GET,PUT,DELETE",
        "url": "question/{qid}/answer/{aid}",
        "description": "Get, edit ,delete answer with its id for a question with its id"
        },
        {
        "request": "POST",
        "url": "users/register/",
        "description": "Registers a User"
        },
        {
        "request": "POST",
        "url": "users/login/",
        "description": "Logs in a user"
        },
        {
        "request": "POST",
        "url": "users/logout/",
        "description": "Logs out a user"
        },
        {
        "request": "GET",
        "url": "users/view/",
        "description": "Lists all users that don't have staff-level permissions"
        },
        {
        "request": "PUT",
        "url": "users/change-password/",
        "description": "Post answer for a question with its id"
        },
        {
        "request": "GET",
        "url": "users/{username}/questions/",
        "description": "Retrieves all questions posted by a User"
        },
        {
        "request": "GET",
        "url": "users/{username}/answers/",
        "description": "Retrieves all answers posted by a User"
        },
        {
        "request": "PUT,PATCH",
        "url": "users/{username}/update/",
        "description": "Updates the information of a user"
        }
    ]
    return Response(endpoints,status=status.HTTP_200_OK)
        
        
        

@api_view(['POST'])
def question_create(request):
    if request.method == 'POST':
        question=Question(author=request.user)
        serializer = QuestionSerializer(question,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class QuestionList(ListAPIView):
    serializer_class=QuestionSerializer
    queryset=Question.objects.all().order_by('-date_posted')
    def list(self, request):
        queryset = self.get_queryset()
        serializer = QuestionSerializer(queryset, many=True).data
        return Response(serializer)

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def question_detail(request, **kwargs):
    _id = kwargs.get("id")
    try:
        question = Question.objects.get(id=_id)
    except Question.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        data = QuestionSerializer(question).data
        return Response(data)
    if question.author!=request.user:
        return Response({'response':"You don't have permission to do that"})
   
    if request.method == "PUT":
        data = request.data
        ques_serializer = QuestionSerializer(question, data=data)
        if ques_serializer.is_valid():
            ques_serializer.save()
            return Response(ques_serializer.data, status=status.HTTP_200_OK)
        return Response(ques_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "PATCH":
        data = request.data
        ques_serializer = QuestionSerializer(question, data=data, partial=True)
        if ques_serializer.is_valid():
            ques_serializer.save()
            return Response(ques_serializer.data,status=status.HTTP_200_OK)
        return Response(ques_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        question.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def answer_create(request, **kwargs):
    _id = kwargs.get("id")
    if request.method == 'POST':
        ans=Answer(author=request.user,question=Question.objects.get(id=_id))
        serializer = AnswerSerializer(ans,data=request.data)
        if serializer.is_valid():
            serializer.save()
            question = Question.objects.get(id=_id)
            question.no_of_answers += 1
            question.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
class AnswerList(ListAPIView):
    queryset=Answer.objects.all().order_by('-date_posted')
    serializer_class=AnswerSerializer
    def list(self, request, *args, **kwargs):
        _id=kwargs.get("id")
        queryset=self.get_queryset()
        serializer = AnswerSerializer(queryset.filter(question=_id), many=True).data
        return Response(serializer)
        
@api_view(['GET', 'PUT', 'DELETE', 'PATCH'])
def answer_detail(request, **kwargs):
    _id = kwargs.get("aid")
    _qid = kwargs.get("qid")
    try:
        answer = Answer.objects.get(id=_id)
    except Answer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        ser =  AnswerSerializer(answer)
        return Response(ser.data)
    if answer.author!=request.user:
        return Response({'response':"You don't have permission to do that"})
        
    if request.method == "PUT":
        ans_ser = AnswerSerializer(answer, data=request.data)
        if ans_ser.is_valid():
            ans_ser.save()
            return Response(ans_ser.data, status=status.HTTP_200_OK)
        return Response(ans_ser.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "PATCH":
        data = request.data
        ans_serializer = AnswerSerializer(answer, data=data, partial=True)
        if ans_serializer.is_valid():
            ans_serializer.save()
            return Response(ans_serializer.data,status=status.HTTP_200_OK)
        return Response(ans_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        answer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
