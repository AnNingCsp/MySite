# Generated by Django 2.1.7 on 2019-02-28 18:30

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Areas',
            fields=[
                ('area_id', models.AutoField(primary_key=True, serialize=False)),
                ('area_name', models.CharField(max_length=20, verbose_name='名称')),
                ('area_parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='subs', to='medical.Areas', verbose_name='上级行政区划')),
            ],
            options={
                'verbose_name': '行政区划',
                'verbose_name_plural': '行政区划',
            },
        ),
        migrations.CreateModel(
            name='Diagnosis',
            fields=[
                ('diagnosis_id', models.AutoField(primary_key=True, serialize=False)),
                ('diagnosis_title', models.CharField(help_text='诊断标题', max_length=30, verbose_name='诊断标题')),
                ('diagnosis_note', models.CharField(default='无', help_text='备注信息', max_length=200, verbose_name='备注信息')),
                ('diagnosis_image', models.ImageField(help_text='用户上传眼底图', upload_to='diagnosis/images/', verbose_name='眼底图')),
                ('diagnosis_prop', models.CharField(help_text='诊断结果', max_length=10, verbose_name='诊断结果')),
                ('diagnosis_addtime', models.DateTimeField(default=django.utils.timezone.now, help_text='诊断时间', verbose_name='诊断时间')),
                ('user', models.ForeignKey(help_text='用户名', on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '诊断结果',
                'verbose_name_plural': '诊断结果',
            },
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('hospital_id', models.AutoField(primary_key=True, serialize=False)),
                ('hospital_name', models.CharField(help_text='唯一医院名', max_length=30, unique=True, verbose_name='医院名')),
                ('hospital_desc', models.CharField(blank=True, help_text='允许为空的简介', max_length=200, verbose_name='简介')),
                ('hospital_address', models.CharField(blank=True, help_text='允许为空的区县以下地址', max_length=50, verbose_name='区县以下地址')),
                ('hospital_tel', models.CharField(blank=True, help_text='允许为空的联系方式', max_length=16, validators=[django.core.validators.RegexValidator(regex='((\\d{11})|^((\\d{7,8})|(\\d{4}|\\d{3})-(\\d{7,8})|(\\d{4}|\\d{3})-(\\d{7,8})-(\\d{4}|\\d{3}|\\d{2}|\\d{1})|(\\d{7,8})-(\\d{4}|\\d{3}|\\d{2}|\\d{1}))$)')], verbose_name='联系方式')),
                ('hospital_email', models.EmailField(blank=True, help_text='允许为空的电子邮箱', max_length=254, verbose_name='电子邮箱')),
                ('hospital_detail', models.TextField(blank=True, help_text='允许为空的详情', verbose_name='医院详情')),
                ('hospital_city', models.ForeignKey(help_text='市', on_delete=django.db.models.deletion.PROTECT, related_name='hospital_city', to='medical.Areas')),
                ('hospital_district', models.ForeignKey(help_text='区县', on_delete=django.db.models.deletion.PROTECT, related_name='hospital_district', to='medical.Areas')),
                ('hospital_province', models.ForeignKey(help_text='省', on_delete=django.db.models.deletion.PROTECT, related_name='hospital_province', to='medical.Areas')),
            ],
            options={
                'verbose_name': '医院',
                'verbose_name_plural': '医院',
            },
        ),
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.CharField(max_length=1024, verbose_name='message_body')),
                ('createtime', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=False)),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='message_receiver', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='message_sender', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'messages',
                'verbose_name_plural': 'messages',
            },
        ),
    ]
