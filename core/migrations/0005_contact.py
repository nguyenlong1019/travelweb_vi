# Generated by Django 4.2.9 on 2024-10-14 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_touristdestination_detail_touristdestination_slug_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(blank=True, editable=False, null=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('phone', models.CharField(max_length=15)),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
            ],
            options={
                'verbose_name': 'Liên hệ',
                'verbose_name_plural': 'Liên hệ',
                'db_table': 'contact',
            },
        ),
    ]
