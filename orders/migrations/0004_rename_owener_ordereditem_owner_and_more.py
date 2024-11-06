# Generated by Django 5.0.4 on 2024-10-20 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_order_ordereditem_delete_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ordereditem',
            old_name='owener',
            new_name='owner',
        ),
        migrations.AlterField(
            model_name='order',
            name='order_status',
            field=models.IntegerField(choices=[(0, 'CART_STAGE'), (1, 'ORDER_CONFORMED'), (2, 'ORDER_PROCESSED'), (3, 'ORDER_DELIVERED'), (4, 'ORDER_REJECTED')], default=0),
        ),
    ]
