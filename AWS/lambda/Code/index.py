#! so executa 1 vez esse codigo para poder indexar as imagens
import boto3

s3 = boto3.resource('s3')
client = boto3.client('rekognition')


def lista_imagen():
    imagens = []
    for i in s3.Bucket('faces-lambda').objects.all():
        imagens.append(i.key)
    return imagens


def index_collection(imagens):
    # tem que criar a collection primeiro antes de configurar
    # client.create_collection(CollectionId='faces')
    for a in imagens:
        response = client.index_faces(
            CollectionId='faces',
            Image={
                'S3Object': {
                    'Bucket': 'faces-lambda',
                    'Name': a,
                },
            },
        )
    return response


imagens = lista_imagen()
index_collection(imagens)

# aws rekognition list-faces --collection-id faces | grep ExternalImageId
