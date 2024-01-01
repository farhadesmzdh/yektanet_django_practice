from django.shortcuts import get_object_or_404
from django.utils.deprecation import MiddlewareMixin


class SaveUserClickMiddleware(MiddlewareMixin):
    def process_request(self, request):
        from .models import Click, Ad
        ad_id = request.POST.get('ad_id') or request.GET.get('ad_id')
        if ad_id is not None:
            click_instance = Click.objects.create(
                ad_id=get_object_or_404(Ad, id=ad_id),
                ip=request.META.get('REMOTE_ADDR')
            )

            click_instance.save()
            request.click_instance = click_instance
