from django.core.management import BaseCommand
from faker import Faker
from headcount.models import Headcount
from turnover.models import Turnover

class Command(BaseCommand):

    def handle(self, *args, **options):
        faker = Faker()

        for _ in range(1000):
            fake_data = {
                'id_employee': faker.unique.random_number(digits=8),
                'ds_category_1': faker.random_element(elements=("Alexanderton", "Cookfurt", "East Calvinfurt", "East Jenniferview")),
                'ds_category_2': faker.random_element(elements=('Masculino', 'Feminino', 'Outro')),
                'ds_category_3': faker.random_int(min=1, max=4),
                'ds_category_4': faker.company(),
                'ds_category_5': faker.random_element(elements=('TI', 'Vendas', 'RH', 'Marketing')),
                'fg_status': faker.random_element(elements=(1, 0)),
                'fg_dismissal_on_month': faker.random_element(elements=(1, 0)),
                'dt_reference_month': faker.random_element(elements=('2022-01-01', '2022-02-01',
                                                                    '2022-03-01', '2022-04-01',
                                                                    '2022-05-01', '2022-06-01',
                                                                    '2022-07-01', '2022-08-01',
                                                                    '2022-09-01', '2022-10-01',
                                                                    '2022-11-01', '2022-12-01',
                                                                    )),
        }

            # Crie objetos Headcount
            Headcount.objects.create(**fake_data)

            # Crie objetos Turnover
            Turnover.objects.create(**fake_data)