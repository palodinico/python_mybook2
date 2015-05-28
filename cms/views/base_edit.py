from django.shortcuts import get_object_or_404, redirect, render_to_response
from django.template import RequestContext
from django.views.generic import View

class BaseEdit(View):
    template_name = None
    redirect_view = None
    object = None
    form_object = None

    def get_instance(self, pk):
        if pk:
            return get_object_or_404(self.object, pk=pk)
        else:
            return self.object()

    def get(self, request, *args, **kwargs):
        instance_obj = self.get_instance(kwargs.get('pk'))
        form = self.form_object(instance=instance_obj)
        return render_to_response(self.template_name,
                                  dict(form=form, pk=kwargs.get('pk')),
                                  context_instance=RequestContext(request))

    def post(self, request, *args, **kwargs):
        instance_obj = self.get_instance(kwargs.get('pk'))
        form = self.form_object(request.POST, instance=instance_obj)
        if form.is_valid():
            object = form.save(commit=False)
            object.save()
        return redirect(self.redirect_view)