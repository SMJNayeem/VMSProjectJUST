
from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='accountant',
            new_name='superuser',
        ),
        migrations.RemoveField(
            model_name='user',
            name='chairman',
        ),
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
        migrations.RemoveField(
            model_name='user',
            name='vadmin',
        ),
        migrations.RemoveField(
            model_name='user',
            name='vsubadmin',
        ),
        migrations.AddField(
            model_name='user',
            name='codename',
            field=models.CharField(max_length=100, null=True, unique=True, verbose_name='Username'),
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
        migrations.AlterField(
            model_name='user',
            name='contact_no',
            field=models.CharField(max_length=11, null=True, unique=True, verbose_name='Contact Number'),
        ),
        migrations.AlterField(
            model_name='user',
            name='dept_sec',
            field=models.CharField(max_length=100, null=True, verbose_name='Department or Section'),
        ),
        migrations.AlterField(
            model_name='user',
            name='designation',
            field=models.CharField(max_length=100, null=True, verbose_name='Designation'),
        ),
        migrations.AlterField(
            model_name='user',
            name='full_name',
            field=models.CharField(max_length=150, null=True, verbose_name='Full Name'),
        ),
    ]
