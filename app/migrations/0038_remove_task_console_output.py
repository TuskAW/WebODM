# Generated by Django 2.2.27 on 2023-09-11 19:11
import os
from django.db import migrations
from webodm import settings

def data_path(project_id, task_id, *args):
    return os.path.join(settings.MEDIA_ROOT,
                        "project",
                        str(project_id),
                        "task",
                        str(task_id),
                        "data",
                        *args)

def dump_console_outputs(apps, schema_editor):
    Task = apps.get_model('app', 'Task')

    for t in Task.objects.all():
        if t.console_output is not None and len(t.console_output) > 0:
            dp = data_path(t.project.id, t.id)
            os.makedirs(dp, exist_ok=True)
            outfile = os.path.join(dp, "console_output.txt")

            with open(outfile, "w") as f:
                f.write(t.console_output)
            print("Wrote console output for %s to %s" % (t, outfile))
        else:
            print("No task output for %s" % t)

class Migration(migrations.Migration):

    dependencies = [
        ('app', '0037_profile'),
    ]

    operations = [
        migrations.RunPython(dump_console_outputs),
        migrations.RemoveField(
            model_name='task',
            name='console_output',
        ),
    ]
