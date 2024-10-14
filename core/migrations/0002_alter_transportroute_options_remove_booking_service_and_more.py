# Generated by Django 4.2.9 on 2024-10-14 04:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='transportroute',
            options={'verbose_name': 'Tour du lịch', 'verbose_name_plural': 'Tour du lịch'},
        ),
        migrations.RemoveField(
            model_name='booking',
            name='service',
        ),
        migrations.AddField(
            model_name='booking',
            name='transport',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.transportroute'),
        ),
        migrations.AddField(
            model_name='transportroute',
            name='amount',
            field=models.IntegerField(default=1, verbose_name='Số lượng người'),
        ),
        migrations.AddField(
            model_name='transportroute',
            name='quantity',
            field=models.IntegerField(default=10, verbose_name='Số vé còn'),
        ),
        migrations.AddField(
            model_name='transportroute',
            name='vehicle',
            field=models.CharField(choices=[('Xe khách', 'Xe khách'), ('Máy bay', 'Máy bay'), ('Tàu hỏa', 'Tòa hỏa')], default='Xe khách', max_length=31, verbose_name='Loại hình di chuyển'),
        ),
        migrations.AlterField(
            model_name='transportroute',
            name='arrival_time',
            field=models.DateField(auto_now_add=True, verbose_name='Ngày về'),
        ),
        migrations.AlterField(
            model_name='transportroute',
            name='departure',
            field=models.CharField(max_length=255, verbose_name='Điểm khởi hành'),
        ),
        migrations.AlterField(
            model_name='transportroute',
            name='departure_time',
            field=models.DateField(auto_now_add=True, verbose_name='Ngày đi'),
        ),
        migrations.AlterField(
            model_name='transportroute',
            name='destination',
            field=models.CharField(max_length=255, verbose_name='Điểm đến'),
        ),
        migrations.AlterField(
            model_name='transportroute',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=18, null=True, verbose_name='Giá vé'),
        ),
        migrations.AlterField(
            model_name='transportroute',
            name='service_provider',
            field=models.ForeignKey(db_column='service_provider', null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.tourservice', verbose_name='Nhà cung cấp dịch vụ'),
        ),
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(blank=True, editable=False, null=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=255)),
                ('transport_route', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.transportroute')),
            ],
            options={
                'verbose_name': 'Hoạt động trong tour',
                'verbose_name_plural': 'Hoạt động trong tour',
                'db_table': 'activities',
            },
        ),
    ]