from django.db import migrations


def create_roles(apps, _):
    """Creates the default roles in the Role model."""
    Role = apps.get_model("accounts", "Role")

    roles = [
        {"name": "developer", "description": "The person on the team who does the work"},
        {"name": "scrum master", "description": "The team's coach"},
        {"name": "product owner", "description": "The person who defines the work"},
    ]

    for role in roles:
        Role.objects.get_or_create(name=role["name"], defaults={"description": role["description"]})


def delete_roles(apps, _):
    """Removes the created roles if the migration is rolled back."""
    Role = apps.get_model("accounts", "Role")
    Role.objects.filter(name__in=["developer", "scrum master", "product owner"]).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),  # This ensures roles are added AFTER the model is created
    ]

    operations = [
        migrations.RunPython(create_roles, delete_roles),  # Adds the role entries
    ]
