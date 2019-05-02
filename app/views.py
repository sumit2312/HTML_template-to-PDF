from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.template.loader import get_template
from .utils import render_to_pdf


# class GeneratePDF(View):
#     def get(self, request, *args, **kwargs):
#         data = {
#             #  'today': datetime.date.today(), 
#             'amount': 39.99,
#             'customer_name': 'Cooper Mann',
#             'order_id': 1233434,
#         }
#         pdf = render_to_pdf('app/invoice.html', data)
#         return HttpResponse(pdf, content_type='application/pdf')

class GeneratePDF(View):
    def get(self, request, *args, **kwargs):
        # template = get_template('app/invoice.html')
        context = {
            "invoice_id": 123,
            "customer_name": "John Cooper",
            "amount": 1399.99,
            "today": "Today",
        }
        # html = template.render(context)
        pdf = render_to_pdf('app/invoice.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Invoice_%s.pdf" %("12341231")
            content = "inline; filename='%s'" %(filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename='%s'" %(filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not found")