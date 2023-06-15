from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from utils import computervision_client

def read_local_image(filepath: str) -> object:
    with open(filepath, 'rb') as local_image:
        yield local_image

def analyze_local_image(local_image: object, language: str='en') -> object:
    # remote_image_features = [VisualFeatureTypes.categories,VisualFeatureTypes.brands,VisualFeatureTypes.adult,VisualFeatureTypes.color,VisualFeatureTypes.description,VisualFeatureTypes.faces,VisualFeatureTypes.image_type,VisualFeatureTypes.objects,VisualFeatureTypes.tags]
    remote_image_features = [VisualFeatureTypes.categories, VisualFeatureTypes.objects, VisualFeatureTypes.tags]
    results_local = computervision_client.analyze_image_in_stream(local_image , remote_image_features, language=language)
    return results_local

def get_local_tags(results: object):
    tags = []
    for tag in results.tags:
        tags.append(tag.name)
    
    return tags

def get_detect_objects(results: object) -> tuple:
    for object in results.objects:
        x = object.rectangle.x
        y = object.rectangle.y
        w = object.rectangle.w
        h = object.rectangle.h
        caption = object.object_property
        yield x, y, w, h, caption
