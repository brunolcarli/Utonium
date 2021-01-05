from django.core.management.base import BaseCommand
from utonium.training.train import train_powerpuff_model


class Command(BaseCommand):
    def __init__(self):
        self.help = 'Train the model.'

    def add_arguments(self, parser):
        parser.add_argument('--model', type=str)

    def handle(self, *args, **options):
        task = options['model']
        if task == 'train':
            print('Training service learning model...')
            train_powerpuff_model()
            print('Done!')

        else:
            print(f"Invalid value for this field: {task}", 'error')
            exit(1)
