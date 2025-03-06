
from django.core.management.base import BaseCommand
from doctors.models import Doctor

class Command(BaseCommand):
       help = 'Очистить таблицу doctors_doctor'

       def handle(self, *args, **options):
           Doctor.objects.all().delete()
           self.stdout.write(self.style.SUCCESS('Successfully deleted all doctors'))