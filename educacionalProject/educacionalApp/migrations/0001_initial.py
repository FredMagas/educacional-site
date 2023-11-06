# Generated by Django 4.2.2 on 2023-11-05 20:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('primeiro_acesso', models.BooleanField(default=True)),
                ('endereco', models.CharField(default='', max_length=255)),
                ('celular', models.CharField(default='(00)00000-0000', max_length=20)),
                ('telefone', models.CharField(default='(00)0000-0000', max_length=20)),
                ('cpf', models.CharField(default='000.000.000-00', max_length=11)),
                ('nome_juridico', models.CharField(default='', max_length=255)),
                ('nome_fantasia', models.CharField(default='', max_length=255)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]