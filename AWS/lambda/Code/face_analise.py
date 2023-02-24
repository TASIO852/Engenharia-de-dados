import boto3
import json

s3 = boto3.resource('s3')
client = boto3.client('rekognition')


def detecta_faces():

    faces_detectadas = client.index_faces(
        CollectionId='faces',
        DetectionAttributes=['DEFAULT'],
        ExternalImageId='TEMPORARIA',
        Image={
            'S3Object': {
                'Bucket': 'faces-lambda',
                'Name': 'teste.jpeg',
            },
        },
    )
    print(json.dumps(faces_detectadas, indent=4))
    return faces_detectadas


def criar_lista_faceId_detectadas(faces_detectadas):
    faceId = []
    for i in range(len(faces_detectadas['FaceRecords'])):
        faceId.append(faces_detectadas['FaceRecords'][i]['Face']['FaceId'])
    return faceId

# para subir o codigo tem que colocar no formato zip
# aws lambda update-function-code \
#     --function-name faceAnalise \
#     --zip-file fileb://face_analise.zip
# opcional para subir o code (update-function-code)
# depois so verificar no console
# se tiver bibliotecas a mais tem que subir elas tbm (provavelmente no requeriments)
# depois tem que configura um evento(trigger) e
# tem que ter autorizaçao para usar as parada
# configurar permisionamento do bucket


def main(event, context):
    detectado = detecta_faces()
    facesId = criar_lista_faceId_detectadas(detectado)
    print(facesId)


# aws rekognition list-faces --collection-id faces | grep ExternalImageId
