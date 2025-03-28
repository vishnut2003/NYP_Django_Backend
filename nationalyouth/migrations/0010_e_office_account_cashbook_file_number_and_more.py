# Generated by Django 4.2.16 on 2024-12-26 08:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nationalyouth', '0009_alter_application_for_affliation_pincode'),
    ]

    operations = [
        migrations.AddField(
            model_name='e_office_account',
            name='cashbook_file_number',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='e_office_account',
            name='cashbook_registration_page_number',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='e_office_account',
            name='finance_registration_book_number',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='e_office_account',
            name='gst',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='e_office_account',
            name='payment_type',
            field=models.CharField(choices=[('online', 'Online'), ('offline', 'Offline')], default='online', max_length=25),
        ),
        migrations.AddField(
            model_name='e_office_account',
            name='purpose',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='e_office_account',
            name='remitter_name',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='e_office_account',
            name='address',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='e_office_account',
            name='amount_detail',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='e_office_account',
            name='bank_name',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='e_office_account',
            name='file_referral_number',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='e_office_account',
            name='name',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='e_office_account',
            name='office_registration_number',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='e_office_account',
            name='pan_card_number',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='e_office_account',
            name='remark',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='e_office_account',
            name='transaction_number',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.CreateModel(
            name='Application_for_Affliation_Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('application', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='nationalyouth.application_for_affliation')),
                ('course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='nationalyouth.course_name')),
            ],
        ),
    ]
