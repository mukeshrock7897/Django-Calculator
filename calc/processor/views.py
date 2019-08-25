from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from . import computing


@csrf_exempt
def compute(request):

    expr = request.POST.get('data', None)

    if expr is None:
        return JsonResponse({'error': 'No data field specified'})

    is_ok, answer = computing.compute(expr)

    if is_ok:
        return JsonResponse({'answer': answer})
    else:
        return JsonResponse({'error': answer})
