import pandas as pd
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import UploadedFile
from .llm_service import get_model_recommendation

class UploadCSVView(APIView):
    def post(self, request):
        file = request.FILES.get('file')

        if not file:
            return Response(
                {'error': 'No file uploaded'},
                status=status.HTTP_400_BAD_REQUEST
            )

        if not file.name.endswith('.csv'):
            return Response(
                {'error': 'Only CSV files are allowed'},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Save file to database
        uploaded = UploadedFile.objects.create(file=file)

        # Parse CSV with pandas
        df = pd.read_csv(uploaded.file.path)

        # Build dataset summary for LLM
        summary = f"""
Filename: {file.name}
Rows: {df.shape[0]}
Columns: {df.shape[1]}
Column Names: {list(df.columns)}
Data Types: {df.dtypes.astype(str).to_dict()}
Missing Values: {int(df.isnull().sum().sum())}
Sample Data: {df.head(3).to_string()}
        """

        # Get LLM recommendation
        recommendation = get_model_recommendation(summary)

        # Build response
        stats = {
            'filename': file.name,
            'rows': df.shape[0],
            'columns': df.shape[1],
            'column_names': list(df.columns),
            'missing_values': int(df.isnull().sum().sum()),
            'dtypes': df.dtypes.astype(str).to_dict(),
            'recommendation': recommendation
        }

        return Response(stats, status=status.HTTP_200_OK)