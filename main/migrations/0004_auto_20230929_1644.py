# Generated by Django 3.2.21 on 2023-09-29 19:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stands', '0001_initial'),
        ('main', '0003_remove_reserva_email_empresa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='stand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stands.stand', verbose_name='Stand'),
        ),
        migrations.DeleteModel(
            name='Stand',
        ),
    ]