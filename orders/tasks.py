
from django.core.mail import send_mail
from .models import Order

# не даработа пока

def order_created(order_id):
    """
    Задача отправки уведомления по электронной почте при
    успешном создании заказа.
    """
    order = Order.objects.get(id=order_id)
    subject = 'Номер заказа. {}'.format(order.id)
    message = '{},\n\nВы успешно разместили заказ.\
                  Ваш идентификатор заказа - это {}.'.format(order.first_name,
                                            order.id)
    mail_sent = send_mail(subject,
                          message,
                          'admin@myshop.com',
                          [order.email])
    return mail_sent
