# Generated by Django 3.0.6 on 2020-05-10 07:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0003_auto_20200510_0015'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='passwordresetcodes',
            name='id',
        ),
        migrations.AlterField(
            model_name='passwordresetcodes',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]