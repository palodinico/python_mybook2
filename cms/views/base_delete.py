from django.shortcuts import get_object_or_404, redirect
from django.views.generic import View

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