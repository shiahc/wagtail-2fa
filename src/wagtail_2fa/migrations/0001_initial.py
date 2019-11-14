# Generated by Django 2.2.7 on 2019-11-14 15:01

from django.db import migrations


def create_2fa_permissions(apps, schema_editor):
    ContentType = apps.get_model('contenttypes.ContentType')
    Permission = apps.get_model('auth.Permission')
    Group = apps.get_model('auth.Group')

    wagtailadmin_content_type, created = ContentType.objects.get_or_create(
        app_label='wagtailadmin',
        model='admin'
    )

    # Create 2FA permission
    disable_2fa_permission, created = Permission.objects.get_or_create(
        content_type=wagtailadmin_content_type,
        codename='disable_2fa',
        name='Disable 2FA'
    )

    # Assign it to Editors and Moderators groups
    for group in Group.objects.filter(name__in=['Editors', 'Moderators']):
        group.permissions.add(disable_2fa_permission)


def remove_2fa_permissions(apps, schema_editor):
    """Reverse the above additions of permissions."""
    ContentType = apps.get_model('contenttypes.ContentType')
    Permission = apps.get_model('auth.Permission')
    wagtailadmin_content_type = ContentType.objects.get(
        app_label='wagtailadmin',
        model='admin',
    )
    # This cascades to Group
    Permission.objects.filter(
        content_type=wagtailadmin_content_type,
        codename='disable_2fa',
    ).delete()


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.RunPython(create_2fa_permissions, remove_2fa_permissions),
    ]
