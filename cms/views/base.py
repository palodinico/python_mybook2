from django.shortcuts import get_object_or_404, redirect
from django.views.generic import View
from django.views.generic.list import ListView

class BaseList(ListView):
    '''標準リストview'''
    paginate_by = 5
    object_list = None

    def refresh_object_list(self):
        return None

    def get(self, request, *args, **kwargs):
        self.object_list = self.refresh_object_list();
        context = self.get_context_data(object_list=self.object_list)
        return self.render_to_response(context)

class BaseDelete(View):
    '''標準削除view'''
    redirect_view = None
    object = None

    def get_object(self, pk):
        return get_object_or_404(self.object, pk=pk)

    def get(self, request, *args, **kwargs):
        object = self.get_object(kwargs['pk'])
        object.delete()
        return redirect(self.redirect_view)