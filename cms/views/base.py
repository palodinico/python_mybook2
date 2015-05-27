from django.views.generic.list import ListView

class BaseList(ListView):
    paginate_by = 5
    object_list = None

    def refresh_object_list(self):
        return None

    def get(self, request, *args, **kwargs):
        self.object_list = self.refresh_object_list();
        context = self.get_context_data(object_list=self.object_list)
        return self.render_to_response(context)