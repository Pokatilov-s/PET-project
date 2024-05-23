# Generated by Django 5.0.3 on 2024-05-23 16:43

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('forge', '0004_alter_course_status'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TransactionsDetails',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('bank', models.CharField(max_length=30)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'transactions_details',
            },
        ),
        migrations.CreateModel(
            name='UserCourse',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('status', models.CharField(choices=[('processing', 'Processing'), ('success', 'Success'), ('error', 'Error')], default='processing', max_length=10)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('course_uuid', models.ForeignKey(db_column='course_uuid', on_delete=django.db.models.deletion.CASCADE, to='forge.course')),
                ('transaction_uuid', models.ForeignKey(db_column='transaction_uuid', on_delete=django.db.models.deletion.PROTECT, to='store.transactionsdetails')),
                ('user_uuid', models.ForeignKey(db_column='user_uuid', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'user_courses',
                'indexes': [models.Index(fields=['user_uuid'], name='user_course_user_uu_042ecd_idx')],
                'unique_together': {('user_uuid', 'course_uuid')},
            },
        ),
    ]
