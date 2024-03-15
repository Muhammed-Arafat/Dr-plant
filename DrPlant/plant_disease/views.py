from django.shortcuts import render
import numpy as np
import keras
from django.conf import settings
from django.core.files.storage import default_storage,FileSystemStorage
from keras.applications.imagenet_utils import decode_predictions
from keras.utils import load_img, img_to_array
from tensorflow.python.keras.backend import set_session
import os
from PIL import Image
from .forms import CityForm,ImagesForm,PlantsForm
from .models import *
from django.http import JsonResponse
import cv2
import sys
import glob
from tensorflow.lite.python.interpreter import Interpreter
#التجهيز لجميع نماذج الذكاء المستخدمة في المشروع وتضمينها
#أولاً نموذج الاكتشاف
PATH_TO_MODEL='detect.tflite'
PATH_TO_LABELS='labelmap.txt'
interpreter = Interpreter(model_path=PATH_TO_MODEL)
interpreter.allocate_tensors()
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()
# ثانيا نموذج التصنيف
IMAGE_MODEL = keras.models.load_model("vgg15_model.h5")
IMAGE_MODEL.load_weights("vgg16_1.h5")
pepper_Model=keras.models.load_model("22135modelpepper.h5")
#Strawberry_Model=keras.models.load_model("128modelpepperstrow.h5")
Grape_Model=keras.models.load_model("128modelpotatoGrape.h5")
#Potato_Model=keras.models.load_model("22136modelpotato.h5")
pepper_Model.load_weights("pepper_vgg16_with_droup223(1).h5")
#Strawberry_Model.load_weights("strowberry_vgg16_with_droup30.h5")
Grape_Model.load_weights("Grape_vgg16_with_droup30.h5")
#Potato_Model.load_weights("potato_vgg16_with_droup30.h5")

def prepare_predict_img_for_vgg(imurl,model,w):
    img=Image.open(imurl)
    img_d = img.resize((w,w))
    if len(np.array(img_d).shape)<4:
        rgb_img=Image.new("RGB",img_d.size)
        rgb_img.paste(img_d)
    else:
        rgb_img=img_d
    rgb_img=np.array(rgb_img,dtype=np.float64)
    rgb_img=rgb_img.reshape(1,w,w,3)
    precictions=model.predict(rgb_img)
    for i in precictions:
        n=max(i)
        print(n)
    max_idx = np.argmax(precictions)

    return precictions,max_idx

def prepare_detect_img_for_efficient_and_save(PATH_TO_IMAGES,file_url):
    min_conf_threshold=0.6
    images = glob.glob(PATH_TO_IMAGES + '/*.jpg') + glob.glob(PATH_TO_IMAGES + '/*.JPG') + glob.glob(PATH_TO_IMAGES + '/*.png') + glob.glob(PATH_TO_IMAGES + '/*.bmp')

    with open(PATH_TO_LABELS, 'r') as f:
        labels = [line.strip() for line in f.readlines()]
    height = input_details[0]['shape'][1]
    width = input_details[0]['shape'][2]
    float_input = (input_details[0]['dtype'] == np.float32)
    input_mean = 127.5
    input_std = 127.5
    image = cv2.imread(PATH_TO_IMAGES)


    print(image.shape)
    imH, imW, _ = image.shape
    image_resized = cv2.resize(image, (width, height))
    input_data = np.expand_dims(image_resized, axis=0)

    if float_input:
        input_data = (np.float32(input_data) - input_mean) / input_std

    interpreter.set_tensor(input_details[0]['index'],input_data)
    interpreter.invoke()

    boxes = interpreter.get_tensor(output_details[1]['index'])[0] # Bounding box coordinates of detected objects
    classes = interpreter.get_tensor(output_details[3]['index'])[0] # Class index of detected objects
    scores = interpreter.get_tensor(output_details[0]['index'])[0] # Confidence of detected objects
    detections = []
    c=0

    for i in range(len(scores)):

        if ((scores[i] > min_conf_threshold) and (scores[i] <= 1.0)):
            c+=1

            ymin = int(max(1,(boxes[i][0] * imH)))
            xmin = int(max(1,(boxes[i][1] * imW)))
            ymax = int(min(imH,(boxes[i][2] * imH)))
            xmax = int(min(imW,(boxes[i][3] * imW)))

            g=cv2.rectangle(image, (xmin,ymin), (xmax,ymax), (0, 255, 0), 2)
            print(xmax-xmin)
            print(ymax-ymin)
            print(height)
            print(width)
            print("x for vgg16:")
            XX=int((xmax-xmin)*224/512)
            print(XX)
            print("y for vgg16:")
            YY=int((ymax-ymin)*224/512)
            print(YY)
            SS=XX*YY
            print(SS)
               # Draw label
            object_name = labels[int(classes[i])] # Look up object name from "labels" array using class index
            label = '%s: %d%%' % (object_name, int(scores[i]*100)) # Example: 'person: 72%'
                   # Get font size
            label_ymin = max(ymin,1) # Make sure not to draw label too close to top of window
                   # Draw white box to put label text in
            cv2.putText(image, label, (xmin+8, label_ymin+20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (10, 255, 0), 2) # Draw label text
            print(int(scores[i]*100))

            detections.append([object_name, scores[i], xmin, ymin, xmax, ymax])
            if(SS < 8500):
                event="surry the leaf looks small!"
                plant="x"
                print("surry its too small leaf !")
            else:
                plant=str(object_name)
                event="Successful detection!"
    if (c==0):
        event="can't detect any thing!"
        plant="x"
        print("can't detect any thing!")

    index = file_url.find("media")
    if index != -1:
        index += len("media")
        index +=1
        filename = file_url[:index] + "Detect" + file_url[index:]

    image=cv2.imwrite(filename,image)
    add_image=MyMedia.objects.create(image=filename)

    return add_image.image,event,plant

def plant_disease_def(request):# الدالة المسؤولة عن استقبال البيانات
    if request.method == 'POST':
        form = CityForm(request.POST)
        print("ready to get values")
        #استقبال البيانات من الفورم
        print(request.POST['country'])
        print(request.POST['city'])
        print(request.POST['time'])
        print(request.POST['plant'])
        upload = request.FILES['imageFile']
        #تجهيز الروابط
        file_name = default_storage.save(upload.name,upload)
        file_url=default_storage.path(file_name)
        print(file_url)
        vgg16_img_url=file_url
        PATH_TO_IMAGES=file_url
        print(PATH_TO_IMAGES)
        print(vgg16_img_url)
        country_form=request.POST['country']
        city_form=request.POST['city']
        time_form=request.POST['time']
        plant_form=request.POST['plant']


        event2=prepare_detect_img_for_efficient_and_save(PATH_TO_IMAGES,file_url)[1]
        plant2=prepare_detect_img_for_efficient_and_save(PATH_TO_IMAGES,file_url)[2]
        detectimage=prepare_detect_img_for_efficient_and_save(PATH_TO_IMAGES,file_url)[0]
        if (event2=="Successful detection!"):
            if(request.POST['plant']=="Grape" and plant2=="Grape"):
                num=prepare_predict_img_for_vgg(vgg16_img_url,Grape_Model,224)[1]
                if (num == 0):
                    case_form ='17'
                elif (num == 1):
                    case_form ='18'
                else:
                    case_form ='19'
                if form.is_valid():
                    add_img=news4.objects.create(img=vgg16_img_url,time=time_form,case_id=case_form,city_id=city_form,country_id=country_form,plant=plant_form)
                    add_img.save()
                    news=news4.objects.filter(case=case_form)

                countries = Country4.objects.all()
                cities = City4.objects.all()
                plants = Plants4.objects.all()




                context = {
                    'event':event2,

                    'url':prepare_detect_img_for_efficient_and_save(PATH_TO_IMAGES,file_url)[0],
                    'news':news,
                    'form': form,
                    'date':ImagesForm(),
                    'plant':PlantsForm(),
                    'countries': countries,
                    'cities': cities,
                    'plants': plants

                }

                return render(request, 'plant_disease.html', context)


            elif(request.POST['plant']=="Potato" and plant2=="Potato"):
                num=prepare_predict_img_for_vgg(vgg16_img_url,IMAGE_MODEL,112)[1]
                if (num == 0):
                    case_form ='20'
                elif (num == 1):
                    case_form ='21'
                else:
                    case_form ='22'
                    if form.is_valid():
                        add_img=news4.objects.create(img=vgg16_img_url,time=time_form,case_id=case_form,city_id=city_form,country_id=country_form,plant=plant_form)
                        add_img.save()
                        news=news4.objects.filter(case=case_form)

                countries = Country4.objects.all()
                cities = City4.objects.all()
                plants = Plants4.objects.all()





                context = {
                    'event':event2,

                    'url':prepare_detect_img_for_efficient_and_save(PATH_TO_IMAGES,file_url)[0],
                    'news':news,
                    'form': form,
                    'date':ImagesForm(),
                    'plant':PlantsForm(),
                    'countries': countries,
                    'cities': cities,
                    'plants': plants

                }
                return render(request, 'plant_disease.html', context)


            #elif(request.POST['plant']=="Tomato" and plant2=="Tomato"):
            #    print(prepare_predict_img_for_vgg(vgg16_img_url,IMAGE_MODEL,112))
            #    if form.is_valid():
            #        add_img=news4.objects.create(img=vgg16_img_url,time=time_form,case_id=case_form,city_id=city_form,country_id=country_form,plant=plant_form)
            #        add_img.save()
            #        news=news4.objects.filter(case=case_form)

            #    countries = Country4.objects.all()
            #    cities = City4.objects.all()
            #    plants = Plants4.objects.all()




            #    context = {
            #        'event':event2,

            #        'url':prepare_detect_img_for_efficient_and_save(PATH_TO_IMAGES,file_url)[0],
            #        'news':news,
            #        'form': form,
            #        'date':ImagesForm(),
            #        'plant':PlantsForm(),
            #        'countries': countries,
            #        'cities': cities,
            #        'plants': plants

            #    }

            #    return render(request, 'plant_disease.html', context)

            elif(request.POST['plant']=="pepper bell" and plant2=="Pepper"):

                num=prepare_predict_img_for_vgg(vgg16_img_url,pepper_Model,224)[1]
                if (num == 0):
                    case_form ='15'

                else:
                    case_form ='16'
                if form.is_valid():
                    add_img=news4.objects.create(img=vgg16_img_url,time=time_form,case_id=case_form,city_id=city_form,country_id=country_form,plant=plant_form)
                    add_img.save()
                    news=news4.objects.filter(case=case_form)

                countries = Country4.objects.all()
                cities = City4.objects.all()
                plants = Plants4.objects.all()




                context = {
                    'event':event2,

                    'url':prepare_detect_img_for_efficient_and_save(PATH_TO_IMAGES,file_url)[0],
                    'news':news,
                    'form': form,
                    'date':ImagesForm(),
                    'plant':PlantsForm(),
                    'countries': countries,
                    'cities': cities,
                    'plants': plants

                }

                return render(request, 'plant_disease.html', context)


            else:
                news=None
                event2="sorry !! some thing wrong check your input"
                countries = Country4.objects.all()
                cities = City4.objects.all()
                plants = Plants4.objects.all()
                context = {
                    'event':event2,

                    'url':detectimage,
                    'news':news,
                    'form': form,
                    'date':ImagesForm(),
                    'plant':PlantsForm(),
                    'countries': countries,
                    'cities': cities,
                    'plants': plants

                }

                return render(request, 'plant_disease.html', context)

            case_form = '14'
        else:
            news=None
            countries = Country4.objects.all()
            cities = City4.objects.all()
            plants = Plants4.objects.all()
            context = {
                'event':event2,

                'url':prepare_detect_img_for_efficient_and_save(PATH_TO_IMAGES,file_url)[0],
                'news':news,
                'form': form,
                'date':ImagesForm(),
                'plant':PlantsForm(),
                'countries': countries,
                'cities': cities,
                'plants': plants

            }

            return render(request, 'plant_disease.html', context)

        # التحقق من صحة البيانات ومن ثم القيام بتخزينها


    else:
        form = CityForm()

    countries = Country4.objects.all()
    cities = City4.objects.all()
    plants = Plants4.objects.all()

    context = {
        'form': form,
        'date':ImagesForm(),
        'plant':PlantsForm(),
        'countries': countries,
        'cities': cities,
        'plants': plants
    }
    return render(request, 'plant_disease.html', context)
