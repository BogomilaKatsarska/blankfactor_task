from pathlib import Path

from django.utils.datetime_safe import datetime
from rest_framework.parsers import FormParser
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView

from bf_task.compute.models import UserCSVProvidedFile
from bf_task.compute.signals import calc_and_save


class CSVFileUploadView(APIView):

    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        print(request.FILES['filename'])
        print(request.data)
        location = ""

        if request.data['filename']:
            file_obj = request.data['filename']

            if not file_obj.name.endswith('.csv'):
                return Response({'error': 'The provided file is not a CSV file'}, status=403)

            p = Path(__file__).resolve().parent
            file_name = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
            location = p / f'{file_name}.csv'

            UserCSVProvidedFile.objects.create(
                user=request.user,
                name_of_request=file_name,
                file_reference=file_obj,
            )
            calc_and_save(
                sender=UserCSVProvidedFile,
                instance=request.data,
                created=True,
            )

        return Response({"message": "File uploaded successfully", "file_path": str(location)}, status=201)
