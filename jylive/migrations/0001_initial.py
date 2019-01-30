# Generated by Django 2.0.1 on 2019-01-23 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='liveparam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=300, null=True, verbose_name='用户名')),
                ('case_no', models.CharField(max_length=300, null=True, verbose_name='编号')),
                ('param_phone', models.CharField(max_length=30, null=True, verbose_name='电话号码')),
                ('param_pwd', models.CharField(max_length=300, null=True, verbose_name='密码')),
                ('param_name', models.CharField(max_length=300, null=True, verbose_name='姓名')),
                ('param_idNo', models.CharField(max_length=300, null=True, verbose_name='身份证')),
                ('param_bcard', models.CharField(max_length=300, null=True, verbose_name='银行')),
                ('param_cardNo', models.CharField(max_length=300, null=True, verbose_name='银行卡')),
                ('param_ppwd', models.CharField(max_length=300, null=True, verbose_name='支付密码')),
            ],
            options={
                'verbose_name': '即有生活参数',
                'verbose_name_plural': '即有生活参数',
            },
        ),
    ]