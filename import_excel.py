from django.core.management.base import BaseCommand
import pandas as pd
from bnh.models import Item

class Command(BaseCommand):
    help = 'Import data from Excel file'

    def handle(self, *args, **kwargs):
        excel_file_path = 'item.xlsx'


        try:
            # Read the Excel file
            df = pd.read_excel(excel_file_path)

            # Iterate through rows and save data to YourModel
            for index, row in df.iterrows():
                Item.objects.create(
                    name=row['name'],
                    description=row['name'],
                    rate=row['rate'],
                    # Add more fields as needed
                )

            self.stdout.write(self.style.SUCCESS('Data import successful'))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error during data import: {e}'))
