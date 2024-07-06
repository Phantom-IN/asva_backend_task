from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import TextInputSerializer
from .services import model_service
from .utils import calculate_classification_metrics, calculate_ner_metrics, calculate_qa_metrics, calculate_summarization_metrics

class TaskView(APIView):
    def post(self, request):
        serializer = TextInputSerializer(data=request.data)
        if serializer.is_valid():
            task_type = serializer.validated_data['task_type']
            text = serializer.validated_data['text']
            
            if task_type == 'text-classification':
                results = model_service.classify_text(text)
            elif task_type == 'ner':
                results = model_service.ner(text)
            elif task_type == 'qa':
                results = model_service.answer_question(text)
            elif task_type == 'summarization':
                results = model_service.summarize_text(text)
            else:
                return Response({'error': 'Invalid task type'}, status=status.HTTP_400_BAD_REQUEST)
            
            return Response(results, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BenchmarkView(APIView):
    def post(self, request):
        task_type = request.data.get('task_type')
        dataset = request.data.get('dataset')
        
        if not task_type or not dataset:
            return Response({'error': 'Task type and dataset are required'}, status=status.HTTP_400_BAD_REQUEST)
        
        if task_type == 'text-classification':
            metrics = calculate_classification_metrics(dataset)
        elif task_type == 'ner':
            metrics = calculate_ner_metrics(dataset)
        elif task_type == 'qa':
            metrics = calculate_qa_metrics(dataset)
        elif task_type == 'summarization':
            metrics = calculate_summarization_metrics(dataset)
        else:
            return Response({'error': 'Invalid task type'}, status=status.HTTP_400_BAD_REQUEST)
        
        return Response(metrics, status=status.HTTP_200_OK)

class HealthCheckView(APIView):
    def get(self, request):
        return Response({'status': 'ok'}, status=status.HTTP_200_OK)
