from io import BytesIO
from celery import shared_task
import pdfkit
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings
from orders.models import Order

@shared_task
def payment_completed(order_id):
    print('in payment completed')
    order = Order.objects.get(id = order_id)
    subject = f'My Shop – Invoice no. {order.id}'
    message = 'Please, find attached the invoice for your recent purchase.'
    email = EmailMessage(subject,
                         message,
                         'admin@myshop.com',
                         [order.email])
    html = render_to_string('admin/orders/order/pdf.html', {'order': order})

    wkhtmltopdf_path = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
    pdfkit_config = pdfkit.configuration(wkhtmltopdf = wkhtmltopdf_path)
    css_path = settings.STATIC_ROOT / 'css/pdf.css'

    pdf_content = pdfkit.from_string(html, False, configuration=pdfkit_config, css=css_path)
    pdf_buffer = BytesIO(pdf_content)

    email.attach(f'order_{order.id}.pdf',
                 pdf_buffer.getvalue(),
                 'application/pdf')
    email.send()