from django.views.generic.edit import FormView
from tom_alerts.alerts import get_service_class
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic.list import ListView

from tom_alerts.models import BrokerQuery


class BrokerQueryCreateView(FormView):
    template_name = 'tom_alerts/query_form.html'

    def get_broker_name(self):
        if self.request.method == 'GET':
            return self.request.GET.get('broker')
        elif self.request.method == 'POST':
            return self.request.POST.get('broker')

    def get_form_class(self):
        broker_name = self.get_broker_name()

        if not broker_name:
            raise ValueError('Must provide a broker name')

        return get_service_class(broker_name).form

    def get_form(self):
        form = super().get_form()
        form.helper.form_action = reverse('tom_alerts:create')
        return form

    def get_initial(self):
        initial = super().get_initial()
        initial['broker'] = self.get_broker_name()
        return initial

    def form_valid(self, form):
        form.save()
        return redirect(reverse('tom_alerts:list'))


class BrokerQueryUpdateView(FormView):
    template_name = 'tom_alerts/query_form.html'

    def get_object(self):
        return BrokerQuery.objects.get(pk=self.kwargs['id'])

    def get_form_class(self):
        self.object = self.get_object()
        return get_service_class(self.object.broker).form

    def get_form(self):
        form = super().get_form()
        form.helper.form_action = reverse('tom_alerts:update', kwargs={'id': self.object.id})
        return form

    def get_initial(self):
        initial = super().get_initial()
        initial.update(self.object.parameters_as_dict)
        initial['broker'] = self.object.broker
        return initial

    def form_valid(self, form):
        form.save(query_id=self.object.id)
        return redirect(reverse('tom_alerts:list'))


class BrokerQueryListview(ListView):
    model = BrokerQuery
