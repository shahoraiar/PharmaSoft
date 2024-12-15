from .utils import prepare_menu_item
from apps.user.models import User
# Assuming _thread_local is defined elsewhere

def global_context_processor(request):
    # print('Authenticated:', request.user.is_authenticated)
    user_id = request.user.id if request.user.is_authenticated else None
    # print('user id : ', user_id)
    context = {
        'menu_items': prepare_menu_item()
    }
    context['user_id'] = user_id
    return context