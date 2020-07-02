from django.utils.six import BytesIO
from rest_framework.renders import JSONRenderer
from rest_framework.parsers import JSONParser

from status.api.serializers import StatusSerializer
from status.models import Status

obj = Status.objects.first()
serializer = StatusSerializer()
print(serializer.data)
json_data = JSONRenderer().render(serializer.data)
print(json_data)

stream = BytesIO(json_data)
data = JSONParser().parse(stream)
print(data)

qs = Status.objects.all()
serializer2 = StatusSerializer(qs, many = True)
print(serializer2.data)
json_data2 = JSONRenderer().render(serializer2.data)
print(json_data2)

stream2 = BytesIO(json_data2)
data2 = JSONParser().parse(stream2)
print(data2)


'''
create obj
'''
data = {'user': 1 }
serializer = StatusSerializer(data = data)
serializer.is_valid()
serializer.save()
serializer.data

#if serializer.is_valid():
#	serializer.save()


'''
update object
'''
obj = Status.objects.first()
data = {'content': "some thing 4", 'user': 1}
update_serializer = StatusSerializer(obj, data = data)
update_serializer.is_valid()
update_serializer.save()  

'''
delete obj
'''
obj = Status.objects.first()
data = {'user': 1, 'content': "please delete"}
create_obj_serializer = StatusSerializer(data=data)
create_obj_serializer.is_valid()
create_obj = create_obj_serializer.save()
print(create_obj)


#data = {'id': 4}
obj = Status.objects.last()
get_data_serializer = StatusSerializer(obj)
#update_serializer.is_valid()
#update_serializer.save()  
obj.delete()