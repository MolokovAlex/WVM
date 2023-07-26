# Generated by Django 4.2 on 2023-07-24 14:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('WebViewMercury', '0004_alter_dbc_datetime_alter_dbc_datetime_adr0_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dbgc',
            name='counter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WebViewMercury.dbc'),
        ),
        migrations.AlterField(
            model_name='dbgc',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WebViewMercury.dbg'),
        ),
        migrations.AlterField(
            model_name='dbic',
            name='counter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WebViewMercury.dbc'),
        ),
        migrations.AlterField(
            model_name='dbpp',
            name='counter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WebViewMercury.dbc'),
        ),
        migrations.AlterField(
            model_name='ldpp',
            name='counter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WebViewMercury.dbc'),
        ),
    ]
