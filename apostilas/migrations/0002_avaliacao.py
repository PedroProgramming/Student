# Generated by Django 5.0.1 on 2024-01-19 16:33

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apostilas', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Avaliacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avaliacao', models.CharField(choices=[('B', 'Bom'), ('M', 'Medio'), ('R', 'Ruim')], max_length=1)),
                ('apostila', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='apostilas.apostila')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
