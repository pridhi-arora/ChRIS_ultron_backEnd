# Generated by Django 2.1.4 on 2019-01-16 19:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import plugins.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('feeds', '0008_auto_20190114_1437'),
        ('plugins', '0024_auto_20190116_1917'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BoolParameter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.BooleanField(blank=True, default=False)),
            ],
        ),
        migrations.CreateModel(
            name='FloatParameter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='IntParameter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PathParameter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='PluginInstance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100)),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('end_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(default='started', max_length=30)),
                ('cpu_limit', plugins.fields.CPUField(null=True)),
                ('memory_limit', plugins.fields.MemoryField(null=True)),
                ('number_of_workers', models.IntegerField(null=True)),
                ('gpu_limit', models.IntegerField(null=True)),
                ('compute_resource', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plugin_instances', to='plugins.ComputeResource')),
                ('feed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plugin_instances', to='feeds.Feed')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('plugin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='instances', to='plugins.Plugin')),
                ('previous', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='next', to='plugininstances.PluginInstance')),
            ],
            options={
                'ordering': ('-start_date',),
            },
        ),
        migrations.CreateModel(
            name='PluginInstanceFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('fname', models.FileField(max_length=2048, upload_to='')),
                ('plugin_inst', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='plugininstances.PluginInstance')),
            ],
            options={
                'ordering': ('fname',),
            },
        ),
        migrations.CreateModel(
            name='StringParameter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(blank=True, max_length=200)),
                ('plugin_inst', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='string_param', to='plugininstances.PluginInstance')),
                ('plugin_param', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='string_inst', to='plugins.PluginParameter')),
            ],
        ),
        migrations.AddField(
            model_name='pathparameter',
            name='plugin_inst',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='path_param', to='plugininstances.PluginInstance'),
        ),
        migrations.AddField(
            model_name='pathparameter',
            name='plugin_param',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='path_inst', to='plugins.PluginParameter'),
        ),
        migrations.AddField(
            model_name='intparameter',
            name='plugin_inst',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='integer_param', to='plugininstances.PluginInstance'),
        ),
        migrations.AddField(
            model_name='intparameter',
            name='plugin_param',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='integer_inst', to='plugins.PluginParameter'),
        ),
        migrations.AddField(
            model_name='floatparameter',
            name='plugin_inst',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='float_param', to='plugininstances.PluginInstance'),
        ),
        migrations.AddField(
            model_name='floatparameter',
            name='plugin_param',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='float_inst', to='plugins.PluginParameter'),
        ),
        migrations.AddField(
            model_name='boolparameter',
            name='plugin_inst',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='boolean_param', to='plugininstances.PluginInstance'),
        ),
        migrations.AddField(
            model_name='boolparameter',
            name='plugin_param',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='boolean_inst', to='plugins.PluginParameter'),
        ),
    ]
