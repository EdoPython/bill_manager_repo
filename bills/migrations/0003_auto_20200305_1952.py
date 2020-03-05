# Generated by Django 3.0.3 on 2020-03-05 19:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bills', '0002_auto_20200303_1837'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bill',
            name='fecha',
        ),
        migrations.RemoveField(
            model_name='bill',
            name='hora',
        ),
        migrations.AddField(
            model_name='bill',
            name='fechahora',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='bill',
            name='metodo',
            field=models.CharField(choices=[('CA', 'Cash'), ('CC', 'Credit card'), ('TR', 'Transfer'), ('PA', 'Paypal'), ('CH', 'Check'), ('OT', 'Other')], default='EF', max_length=2),
        ),
        migrations.AlterField(
            model_name='bill',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
