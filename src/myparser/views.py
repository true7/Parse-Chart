import json
from django.shortcuts import render
from django.views import View

from .forms import UploadFileForm
from .utils import handle_uploaded_file, handle_queryset


class UploadFile(View):
    def get(self, request, *args, **kwargs):
        form = UploadFileForm()
        context = {'form': form}
        return render(request, 'base.html', context)

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = UploadFileForm(request.POST, request.FILES)
            if form.is_valid():
                # handle_uploaded_file function returns a filtered queryset
                queryset = handle_uploaded_file(request.FILES['file'])
                # convert_to_json function returns data ready to converting into json
                result = handle_queryset(queryset)
                json_data = json.dumps(result)
                context = {'form': form,
                           'json_data': json_data,
                           "queryset": queryset}
                return render(request, 'base.html', context)
