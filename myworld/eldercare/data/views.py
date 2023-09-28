from django.template import loader
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
import pandas as pd
from .models import vehicle, centre, elder, MapTripData
from openpyxl import load_workbook
import json
# from .resources import elderResource
from django.contrib import messages
# from tablib import Dataset
from .forms import VehicleForm, CentreForm, ElderForm, MapTripDataForm
from django.db import transaction
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from urllib.parse import urlencode
from urllib import request
import requests
from django.http import JsonResponse

def home(request):
  template = loader.get_template('home.html')
  return HttpResponse(template.render())
def data(request):
    if request.method == 'POST':
        file = request.FILES['xlsxFile']
        csv = pd.read_csv(file)
        print(csv)

    template = loader.get_template('data.html')
    return HttpResponse(template.render())

def dataimport(request):
    
    template = loader.get_template('dataimport.html')
    return HttpResponse(template.render())

def upload(request):
    if request.method == 'POST' and request.FILES.get('xlsxFile'):
        xlsx_file = request.FILES['xlsxFile']
        df = pd.read_excel(xlsx_file)

        for _, row in df.iterrows():
            centre.objects.create(
                centre=row['centre'],
                cluster=row['cluster'],
                centrepostalcode=row['centrepostalcode']
            )

        for _, row in df.iterrows():
            elder.objects.create(
                elder=row['elder'],
                eldergender=row['eldergender'],
                nricorfin=row['nricorfin'],
                postalcode1=row['postalcode1'],
                postalcode2=row['postalcode2'],
                centre=row['centre'],
                tofromcentre=row['tofromcentre'],
                weekday=row['weekday'],
                etaetd=row['etaetd'],
                timepickupdeliver=row['timepickupdeliver'],
                eldertype=row['eldertype'],
                elderservicetype=row['elderservicetype'],
                caregiver=row['caregiver'],
                loadingtime=row['loadingtime'],
                rowid=row['rowid'],
                fromtopostal=row['fromtopostal'],
                distancekm=row['distancekm'],
                minn=row['minn'],
                min=row['min']
            )
        
        for _, row in df.iterrows():
            vehicle.objects.create(
                centre=row['centre'],
                tripid=row['tripid'],
                seqid=row['seqid'],
                vehicleplate=row['vehicleplate'],
                vehicletype=row['vehicletype'],
                vehiclecapacity=row['vehiclecapacity'],
                maxwheelchairelder=row['maxwheelchairelder'],
                maxambulantelder=row['maxambulantelder'],
                maxcaregiver=row['maxcaregiver']
            )
        
        headers = df.columns.tolist()
        rows = df.values.tolist()
        context = {
            'uploaded_file': True,
            'headers': headers,
            'rows': rows,
        }
    else:
        context = {'uploaded_file': False}

    return render(request, 'upload.html', context)

def database(request):
    if request.method == 'POST' and request.FILES.get('xlsxFile'):
        xlsx_file = request.FILES['xlsxFile']
        df = pd.read_excel(xlsx_file)
        
        for _, row in df.iterrows():
            centre.objects.create(
                centre=row['centre'],
                cluster=row['cluster'],
                centrepostalcode=row['centrepostalcode']
            )
        
        for _, row in df.iterrows():
            elder.objects.create(
                elder=row['elder'],
                eldergender=row['eldergender'],
                nricorfin=row['nricorfin'],
                postalcode1=row['postalcode1'],
                postalcode2=row['postalcode2'],
                centre=row['centre'],
                tofromcentre=row['tofromcentre'],
                weekday=row['weekday'],
                etaetd=row['etaetd'],
                timepickupdeliver=row['timepickupdeliver'],
                eldertype=row['eldertype'],
                elderservicetype=row['elderservicetype'],
                caregiver=row['caregiver'],
                loadingtime=row['loadingtime'],
                rowid=row['rowid'],
                fromtopostal=row['fromtopostal'],
                distancekm=row['distancekm'],
                minn=row['minn'],
                min=row['min']
            )
        
        for _, row in df.iterrows():
            vehicle.objects.create(
                centre=row['centre'],
                tripid=row['tripid'],
                seqid=row['seqid'],
                vehicleplate=row['vehicleplate'],
                vehicletype=row['vehicletype'],
                vehiclecapacity=row['vehiclecapacity'],
                maxwheelchairelder=row['maxwheelchairelder'],
                maxambulantelder=row['maxambulantelder'],
                maxcaregiver=row['maxcaregiver']
            )
        
def uploadmapdata(request):
    if request.method == 'POST' and request.FILES.get('xlsxFile'):
        try:
            xlsx_file = request.FILES['xlsxFile']
            df = pd.read_excel(xlsx_file)

            for _, row in df.iterrows():
                MapTripData.objects.create(
                    centre_n=row['centre_n'],
                    to_from_centre_i=row['to_from_centre_i'],
                    week_day=row['week_day'],
                    time_range=row['time_range'],
                    Trip_Start_Time=row['Trip_Start_Time'],
                    Trip_End_Time=row['Trip_End_Time'],
                    vehicle_plate=row['vehicle_plate'],
                    duration_min=row['duration_min'],
                    svc_type=row['svc_type'],
                    nric_fin=row['nric_fin'],
                    name_surname=row['name_surname'],
                    trans_cap_sub_type_n=row['trans_cap_sub_type_n'],
                    client_seq_n=row['client_seq_n'],
                    client_postal_code=row['client_postal_code'],
                    centr_postal_code=row['centr_postal_code'],
                    gender=row['gender'],
                    Trip_ID=row['Trip_ID'],
                    Loading_Time=row['Loading Time'],
                    FromToPostal=row['FromToPostal'],
                    distance_km=row['distance_km'],
                    min_n=row['min_n'],
                    min_plus_svc_time=row['min (+ Svc time)'],
                    Caregiver=row['Caregiver'],
                    Pick_up_Time_Format=row['Pick up Time_Format'],
                    Pick_up_Time_Delivery=row['Pick up Time/Delivery'],
                    IH_OS=row['IH/OS'],
                    Cluster=row['Cluster'],
                    # Continue populating other fields here
                )

            # Messages for success and error
            messages.success(request, 'Data added successfully.')
            
        except Exception as e:
            messages.error(request, f'An error occurred: {str(e)}')
       

        headers = df.columns.tolist()
        rows = df.values.tolist()
        context = {
            'uploaded_file': True,
            'headers': headers,
            'rows': rows,
        }
    else:
        context = {'uploaded_file': False}

    return render(request, 'map.html', context)


# def upload(request):
#     if request.method == 'POST':
#         elder_resource = elderResource()
#         dataset = Dataset()
#         new_elder = request.FILES['xlsxFile']

#         if not new_elder.name.endswith('xlsx'):
#             messages.info(request,'wrong format')
#             return render(request,'dataimport.html')

#         imported_data = dataset.load(new_elder.read(),format='xlsx')
#         for data in imported_data:
#             value = elder(
#                 data[0],
#                 data[2],
#                 data[3],
#                 data[4],
#                 data[5],
#                 data[6],
#                 data[7],
#                 data[9],
#                 data[10],
#                 data[11],
#                 data[12],
#                 data[13],
#                 data[22],
#                 data[23],
#                 data[24],
#                 data[25],
#                 data[1],
#                 data[26],
#                 data[27],
#                 data[28],
#                 data[29]
#             )
#             value.save()
#         return render(request,'dataimport.html')

    
def dataexport(request):
    template = loader.get_template('dataexport.html')
    return HttpResponse(template.render())

def dataentry(request):
    template = loader.get_template('dataentry.html')
    return HttpResponse(template.render())

def elderinfo(request):
    if request.method == 'POST':
        form = ElderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('data:elderinfo')
    else:
        form = ElderForm()
    return render(request, 'elderinfo.html', {'form': form})

def vehicleinfo(request):
    if request.method == 'POST':
        form = VehicleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('data:vehicleinfo')
    else:
        form = VehicleForm()
    return render(request, 'vehicleinfo.html', {'form': form})

def centreinfo(request):

    form = CentreForm()

    if request.method == 'POST':
        form = CentreForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'centreinfo.html', context)



# def process_file(request):
#     if request.method == 'POST' and 'xlsx_file' in request.FILES:
#         xlsx_file = request.FILES['xlsx_file']
#         df = pd.read_excel(xlsx_file)

#         # Create elder objects
#         for _, row in df.iterrows():
#             elder_object = elder(
#                 elder=row['Elder'],
#                 eldergender=row['Elder Gender'],
#                 nricorfin=row['Elder NRIC or FIN Number'],
#                 postalcode1=row['Elder Postal code 1'],
#                 postalcode2=row['Elder Postal code 2'],
#                 centre=row['Centre'],
#                 tofromcentre=row['To/From Centre'],
#                 weekday=row['Weekday'],
#                 etaetd=row['ETA/ ETD'],
#                 timepickupdeliver=row['Time Pick-Up/ Deliver'],
#                 eldertype=row['Elder Type'],
#                 elderservicetype=row['Elder Service Type'],
#                 caregiver=row['Caregiver'],
#                 loadingtime=row['Loading Time'],
#                 rowid=row['row_id'],
#                 fromtopostal=row['FromToPostal'],
#                 distancekm=row['distance_km'],
#                 minn=row['min_n'],
#                 min=row['min (+svc time)']
#             )
#             elder_object.save()

#         # Create centre objects
#         for _, row in df.iterrows():
#             centre_object = centre(
#                 centre=row['Centre'],
#                 centreid=row['Centre ID'],
#                 cluster=row['Cluster'],
#                 centrepostalcode=row['Centre Postal Code']
#             )
#             centre_object.save()

#         # Create vehicle objects
#         for _, row in df.iterrows():
#             vehicle_object = vehicle(
#                 centre=row['Centre'],
#                 tripid=row['TRIP_ID'],
#                 seqid=row['SEQ_ID'],
#                 vehicleplate=row['Vehicle Plate'],
#                 vehicletype=row['Vehicle Type'],
#                 vehiclecapacity=row['Vehicle Capacity'],
#                 maxwheelchairelder=row['Max Number of Wheelchair Elder Assigned to Vehicle'],
#                 maxambulantelder=row['Max Number of Ambulant Elder Assigned to Vehicle'],
#                 maxcaregiver=row['Max Number of Caregiver Assigned to Vehicle']
#             )
#             vehicle_object.save()

#         return render(request, 'dataimport.html')

        
    
import subprocess
import os
import time
from django.http import HttpResponse, HttpResponseRedirect

def optimize(request):
    if request.method == 'GET':
        try:
            # Start a new Command Prompt subprocess
            subprocess.Popen("cmd", shell=True) 
        except Exception as e:
            print("Error:", e)
        try:
            # Get the path of the current Python file
            current_file_path = os.path.abspath(__file__)

            # Get the base directory path
            base_directory = os.path.dirname(current_file_path)
            print(base_directory)
            print('running')
            # Build the complete path to the batch file'
            batch_file_path = os.path.join(base_directory, 'OR_Project', 'Run.bat')

            # Run the batch file using subprocess
            result = subprocess.run(batch_file_path, shell=True, capture_output=True, text=True)
            # Check the return code to see if the batch file executed successfully
            if result.returncode == 0:
                time.sleep(10)  # Sleep for 10 seconds to allow the batch file to complete
                return HttpResponseRedirect(f"{request.META.get('HTTP_REFERER')}?message=success")
            else:
                # If there was an error, print loading for 10 seconds and then go back to the previous page
                print("Loading...")
                time.sleep(10)
                return HttpResponseRedirect(f"{request.META.get('HTTP_REFERER')}?message=success")
        except Exception as e:
            # Catch any exceptions and print loading for 10 seconds and then go back to the previous page
            print("Error:", e)
            print("Loading...")
            time.sleep(10)
            return HttpResponseRedirect(f"{request.META.get('HTTP_REFERER')}?message=success")
    else:
        return HttpResponse("Invalid request method.", status=405)

def visualize(request):
    if request.method == 'GET':
        try:
            # Get the path of the current Python file
            current_file_path = os.path.abspath(__file__)

            # Get the base directory path
            base_directory = os.path.dirname(current_file_path)
            print(base_directory)
            print('running')
            # Build the complete path to the batch file'
            batch_file_path = os.path.join(base_directory, 'OR_Project', 'Run.bat')

            # Run the batch file using subprocess
            result = subprocess.run(batch_file_path, shell=True, capture_output=True, text=True)
            # Check the return code to see if the batch file executed successfully
            if result.returncode == 0:
                time.sleep(10)  # Sleep for 10 seconds to allow the batch file to complete
                return HttpResponseRedirect(f"{request.META.get('HTTP_REFERER')}?message=success")
            else:
                # If there was an error, print loading for 10 seconds and then go back to the previous page
                print("Loading...")
                time.sleep(10)
                return HttpResponseRedirect(f"{request.META.get('HTTP_REFERER')}?message=success")
        except Exception as e:
            # Catch any exceptions and print loading for 10 seconds and then go back to the previous page
            print("Error:", e)
            print("Loading...")
            time.sleep(10)
            return HttpResponseRedirect(f"{request.META.get('HTTP_REFERER')}?message=success")
    else:
        return HttpResponse("Invalid request method.", status=405)
    


def dataexport(request):
    excel_data = []

    if request.method == 'POST' and request.FILES.get('excel_file'):
        excel_file = request.FILES['excel_file']

        try:
            workbook = load_workbook(excel_file)
            sheet = workbook.active
            excel_data = sheet.values
        except Exception as e:
            error_message = str(e)
        else:
            error_message = None

    return render(request, 'dataexport.html', {'excel_data': excel_data})


def map_view(request):
    data = MapTripData.objects.all()
    context = {'data': data}
    return render(request, 'map.html', context)

def map_trip_data(request):
    # Get data from the MapTripData table
    data = MapTripData.objects.all()

    # Handle filtering and sorting
    filter_value = request.GET.get('filter', None)
    sort_value = request.GET.get('sort', None)

    if filter_value:
        data = data.filter(week_day=filter_value)  # Change this to the appropriate filter field

    if sort_value:
        data = data.order_by(sort_value)  # Change this to the appropriate sort field

    context = {
        'data': data,
    }

    return render(request, 'map_trip_data.html', context)
 

def cleardata(request):
    if request.method == 'POST':
        try:
            with transaction.atomic():
                MapTripData.objects.all().delete()
                messages.success(request, 'Data cleared successfully.')
        except Exception as e:
            messages.error(request, f'An error occurred: {str(e)}')

    return redirect('map')

def refresh_table(request):
    data = MapTripData.objects.all()
    context = {'data': data}
    return render(request, 'map.html', context)


def filter_sort_view(request):
    unique_week_days = MapTripData.objects.order_by('week_day').values_list('week_day', flat=True).distinct()
    unique_trip_ids = MapTripData.objects.order_by('Trip_ID').values_list('Trip_ID', flat=True).distinct()
    unique_centres = MapTripData.objects.order_by('centre_n').values_list('centre_n', flat=True).distinct()
    unique_from_to = MapTripData.objects.order_by('to_from_centre_i').values_list('to_from_centre_i', flat=True).distinct()
    unique_time_ranges = MapTripData.objects.order_by('time_range').values_list('time_range', flat=True).distinct()
    
    filter_week_day = request.GET.get('filter-week-day')
    filter_trip_id = request.GET.get('filter-trip-id')
    centre_filter = request.GET.get('centre-filter')
    from_to_filter = request.GET.get('from-to-filter')
    time_range_filter = request.GET.get('time-range-filter')
   
    
    queryset = MapTripData.objects.all()

    if filter_week_day:
        queryset = queryset.filter(week_day=filter_week_day)
    if filter_trip_id:
        queryset = queryset.filter(Trip_ID=filter_trip_id)
    if centre_filter:
        queryset = queryset.filter(centre_n=centre_filter)
    if from_to_filter:
        queryset = queryset.filter(to_from_centre_i=from_to_filter)
    if time_range_filter:
        queryset = queryset.filter(time_range=time_range_filter)
    
    sort_by = request.GET.get('sort-by')
    if sort_by:
        queryset = queryset.order_by(sort_by)
    
    # Construct the URL with filter parameters
    url_params = {
        'filter-week-day': filter_week_day,
        'filter-trip-id': filter_trip_id,
        'centre-filter': centre_filter,
        'from-to-filter': from_to_filter,
        'time-range-filter': time_range_filter,
        'sort-by': sort_by
    }
    
    # Use the reverse function to generate the URL
    map_url = reverse('map')  # Replace 'map' with the name of your map view
    
    # Append the query parameters to the URL
    map_url_with_params = f"{map_url}?{urlencode(url_params)}"



    context = {
        'unique_week_days': unique_week_days,
        'unique_trip_ids': unique_trip_ids,
        'unique_centres': unique_centres,
        'unique_from_to': unique_from_to,
        'unique_time_ranges': unique_time_ranges,
        'data': MapTripData.objects.all(),  # Original data for map_view
        'filtered_data': queryset,
        'map_url_with_params': map_url_with_params  # Add the generated URL to the context
    }
    

    return render(request, 'map.html', context)



def trip_detail_view(request, trip_id):
    # Get all MapTripData objects with the given Trip_ID
    trip_data = MapTripData.objects.filter(Trip_ID=trip_id)

    print(trip_data)  # Add this line

    if trip_data:
        context = {
            'trip_data': trip_data.first(),
            'client_data': trip_data  # Just pass the queryset directly
        }

        return render(request, 'trip_detail.html', context)
    else:
        return render(request, 'error.html')










