from django.db import migrations


def create_teams(apps, _):
    """Creates the default teams in the Team model."""
    Team = apps.get_model("accounts", "Team")

    teams = [
        {"name": "alpha", "description": "The A team"},
        {"name": "bravo", "description": "The B team"},
        {"name": "charlie", "description": "The C team"},
    ]

    for team in teams:
        Team.objects.get_or_create(name=team["name"], defaults={"description": team["description"]})


def delete_teams(apps, _):
    """Removes the created teams if the migration is rolled back."""
    Team = apps.get_model("accounts", "Team")
    Team.objects.filter(name__in=["alpha", "bravo", "charlie"]).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20250301_1852'),  # Ensures this runs after the Role migration
    ]

    operations = [
        migrations.RunPython(create_teams),
        migrations.RunPython(delete_teams)  # Adds the team entries
    ]
