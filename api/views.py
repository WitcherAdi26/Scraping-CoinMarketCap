from django.http import HttpResponse,JsonResponse
from rest_framework import status
from rest_framework.views import APIView
from .serializer import StartScrapingSerializer
from celery.result import AsyncResult
from .tasks import scrape_crypto_data
import pandas as pd
import json
import base64

# Create your views here.
def index(req):
    return HttpResponse("API ready to scrape...")

# To add a task
class StartScrapingView(APIView):
    def post(self,req):
        serializer=StartScrapingSerializer(data=req.data)
        if serializer.is_valid(raise_exception=True):
            payload=req.data.get('payload',[])
            task=scrape_crypto_data.delay(payload)
            return JsonResponse({'job_id':task.id},status=status.HTTP_202_ACCEPTED)
        return JsonResponse({"error": serializer.error_messages}, status=status.HTTP_400_BAD_REQUEST)
            
        
# To view the status of a task
class ScrapingStatusView(APIView):
    def get(self,req,job_id):
        task_result=AsyncResult(job_id)
        if task_result.status=='SUCCESS':
            try:
                df = pd.DataFrame(task_result.result)
                filename = f"{job_id}.xlsx"
                df.to_excel(filename, index=False, engine='openpyxl')
            except:
                print("Failed to create .xlsx file")

            return JsonResponse({'job_id':job_id,'status':task_result.state,'task':task_result.result},status=status.HTTP_200_OK)
        else:
            return JsonResponse({'job_id':job_id,'status':task_result.state},status=status.HTTP_200_OK)
            

# To terminate a task
class TerminateTaskView(APIView):
    def post(self,req,job_id):
        try:
            task_result = AsyncResult(job_id)
            task_result.revoke(terminate=True)
            return JsonResponse({"message": f"Task {job_id} terminated successfully."}, status=status.HTTP_200_OK)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

