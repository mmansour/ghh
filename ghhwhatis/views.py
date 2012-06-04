# Create your views here.
from django.http import HttpResponse, Http404

def what_is(request):
    try:
        # Retrieve the user account associated with the current subdomain.
#        user = User.objects.get(username=request.subdomain)
        print request.subdomain
        return HttpResponse(request.subdomain)
    except:
#    except User.DoesNotExist:
        # No user matches the current subdomain, so return a generic 404.
        raise Http404

