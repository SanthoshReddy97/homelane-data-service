import json

from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.views import APIView

from homes.const import CONTENT_TYPE
from homes.utils import HomesHandler, standard_price_calculation


@method_decorator(csrf_exempt, name="dispatch")
class HomesViewset(APIView):

    def post(self, request):
        try:
            request_body = json.loads(request.body)
            homes = HomesHandler(request_body=request_body).get_home_data()
            return Response(homes)
        except Exception as e:
            response = {'success': False, 'error': "{}".format(e)}
        return HttpResponse(json.dumps(response), status=500, content_type=CONTENT_TYPE)

    def get(self, request):
        try:
            homes = standard_price_calculation()
            return Response(homes)
        except Exception as e:
            response = {'success': False, 'error': "{}".format(e)}
        return HttpResponse(json.dumps(response), status=500, content_type=CONTENT_TYPE)
