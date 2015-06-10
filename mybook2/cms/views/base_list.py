from django.views.generic.list import ListView

class BaseList(ListView):
    '''標準リストview'''
    paginate_by = 5
    object = None
    object_list = None

    def get(self, request, *args, **kwargs):
        self.object_list = self.object.objects.all().order_by('-update', 'id')
        context = self.get_context_data(object_list=self.object_list)
        return self.render_to_response(context)