# pip install minio
from minio import Minio
import os, re, json

_minio_host_port = 'minio-service.services.svc:9000' 
_minio_username = 'kaapanaminio'
_minio_password = ''

bucket_name = 'slicer-tests'
fn_remote = 'tasklist-test1.json'
fn_local = 't.json'

minioClient = Minio(_minio_host_port, _minio_username, _minio_password, secure = False)

minioClient.fget_object( bucket_name, fn_remote, fn_local) 

objs = minioClient.list_objects(bucket_name)

print(objs)

for x in objs:
  #print(x.__dir__())
  print(x._object_name)
 

  
