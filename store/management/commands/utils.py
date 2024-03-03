"""
    Create fake data.
"""

import random

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from store.models import EquipmentType, Equipment, Allocation


class Command(BaseCommand):
    """
    Command class to create fake data.
    """

    help = "Generate random data for Department, EquipmentType, Equipment."

    def handle(self, *args, **options):
        """
        Overriding handle().
        """
        first_names = ["John", "Micheal", "David", "Maria", "Stephen"]
        last_names = ["Watson", "Pointing", "Dsouza", "Beckham", "Stark"]
        user_list = []

        for i in range(5):
            first_name = first_names[i]
            last_name = last_names[i]
            username = first_name + last_name + "@123"
            email = first_name + last_name + "@example.com"

            user = User(
                username=username,
                email=email,
                first_name=first_name,
                last_name=last_name,
            )

            user.set_password(first_name + "@123")
            user_list.append(user)

        User.objects.bulk_create(user_list)

        EquipmentType.create_random_equipment_types()
        Equipment.create_random_equipments()
        Allocation.create_random_allocations()

        self.stdout.write(self.style.SUCCESS("Random data created."))
