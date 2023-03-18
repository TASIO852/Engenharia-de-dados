import boto3

"""s3 = boto3.resource('s3')

for bucket in s3.buckets.all():

    print(bucket.name) #mostrar o nome dos buckets aws pra confirmar que esta logado

"""

caminho = "C:/Users/tarsi/OneDrive/Documentos/Data Science/Engenharia-de-dados/AWS/S3/Code/SaveData.py"

bucket = "bucket-by-tf"

arquivo = "SaveData.py"

s3 = boto3.client('s3')

s3.upload_file(caminho, bucket, arquivo)