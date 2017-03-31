from django.shortcuts import render,HttpResponse
from django.db.models import Count
# Create your views here.
import  models
def repost(request):
    data=""
    for key in request.POST:
        data= key
    data_list=data.split('|')
    time  = data_list[0]
    hotelname  = data_list[1]
    accounts  = data_list[2]
    monitor_data=data_list[3]
    monitor_url=data_list[4]
    monitor_time=data_list[5]
    obj=models.tests(time=time,hotelname=hotelname,accounts=accounts,mintor_data=monitor_data,url=monitor_url,timestamp=monitor_time)
    obj.save()
    return HttpResponse("xx")


def monitor(request):
    #data=request.POST['data'];
    return render(request,'monitor.html')

def monitorlist(request):
    #data=request.POST['data'];
    p=models.tests.objects.values('mintor_data','url').annotate(bcount=Count('mintor_data'))
    list=[]
    for i in xrange(len(p)):
        datas={'mintor_data':p[i]['mintor_data'],
                'bcount':p[i]['bcount']
               }
        list.append(datas)
    #objs = models.tests.raw('SELECT * from myapp_person')[0]
    return render(request,'monitorlist.html',{"datas":list})