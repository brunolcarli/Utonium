import cv2
import graphene
import numpy as np
from keras.models import model_from_json
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from graphene_file_upload.scalars import Upload
from django.conf import settings

import os
print('----------------')
print(os.getcwd())
print('----------------')

# load json and create model
json_file = open('powerpuff_model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)

# load weights into new model
loaded_model.load_weights("model.h5")
print("Loaded model from disk")


class Query:
    version = graphene.String(description='Service version')

    def resolve_version(self, info, **kwargs):
        return settings.VERSION


class Guess(graphene.relay.ClientIDMutation):
    class Arguments:
        # file = Upload(required=True)
        comment = graphene.String()

    success = graphene.Boolean()
    answer = graphene.String()

    def mutate_and_get_payload(self, info, **kwargs):
        files = info.context.FILES
        image = files['File']

        if not image:
            raise Exception('No file sent.')

        # Saves file as a generic file to manipulate
        path = default_storage.save(
            'utonium/image.jpeg',
            ContentFile(image.read())
        )

        # Loads and resizes the received image
        loaded = cv2.imread(path, 3)
        target = cv2.resize(loaded, (32, 32),  
                   interpolation = cv2.INTER_NEAREST)
        b,g,r = cv2.split(target)
        target = cv2.merge([r,g,b])

        target = np.concatenate([[target]])
        target = target.astype('float32')
        target = target / 255.0

        gate = {
            1: 'blossom',
            2: 'buttercup',
            3: 'bubbles'
        }
        yh = np.argmax(loaded_model.predict(target), axis=1)[0]

        return Guess(success=True, answer=gate[yh])


class Mutation:
    guess = Guess.Field()
