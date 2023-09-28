from django.db import models

class vehicle(models.Model):
  centre = models.CharField(max_length=255)
  tripid = models.CharField(max_length=255) # TRIP_ID
  seqid = models.CharField(max_length=255) #SEQ_ID
  vehicleplate = models.CharField(max_length=255) #Vehicle Plate
  vehicletype = models.CharField(max_length=255)
  # vehicleid = models.CharField(max_length=255)
  vehiclecapacity = models.CharField(max_length=255)
  maxwheelchairelder = models.CharField(max_length=255)
  maxambulantelder = models.CharField(max_length=255)
  maxcaregiver = models.CharField(max_length=255)

class centre(models.Model):
  centre = models.CharField(max_length=255)
  # centreid = models.CharField(max_length=255)
  cluster = models.CharField(max_length=255)
  centrepostalcode = models.CharField(max_length=255)
    

class elder(models.Model):
  elder = models.CharField(max_length=255)
  eldergender = models.CharField(max_length=255)
  nricorfin = models.CharField(max_length=255)
  postalcode1 = models.CharField(max_length=255)
  postalcode2 = models.CharField(max_length=255)
  centre = models.CharField(max_length=255)
  tofromcentre = models.CharField(max_length=255)
  weekday = models.CharField(max_length=255)
  etaetd = models.CharField(max_length=255)
  timepickupdeliver = models.CharField(max_length=255)
  eldertype = models.CharField(max_length=255)
  elderservicetype = models.CharField(max_length=255)
  caregiver = models.CharField(max_length=255)
  loadingtime = models.CharField(max_length=255)
  rowid = models.CharField(max_length=255) # row_id : (extra info added so keeping them NULL)
  fromtopostal =models.CharField(max_length=255) #  FromToPostal : null
  distancekm = models.CharField(max_length=255) # distance_km null
  minn = models.CharField(max_length=255) # min_n : null
  min = models.CharField(max_length=255) # min (+svc time): null

 
class MapTripData(models.Model):
    centre_n = models.CharField(max_length=100)
    to_from_centre_i = models.CharField(max_length=100)
    week_day = models.CharField(max_length=100)
    time_range = models.CharField(max_length=100)
    Trip_Start_Time = models.CharField(max_length=100)
    Trip_End_Time = models.CharField(max_length=100)
    vehicle_plate = models.CharField(max_length=100)
    duration_min = models.DecimalField(max_digits=10, decimal_places=2)
    svc_type = models.CharField(max_length=100)
    nric_fin = models.CharField(max_length=100)
    name_surname = models.CharField(max_length=100)
    trans_cap_sub_type_n = models.CharField(max_length=100)
    client_seq_n = models.IntegerField()
    client_postal_code = models.CharField(max_length=100)
    centr_postal_code = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    Trip_ID = models.IntegerField()
    Loading_Time = models.CharField(max_length=100)
    FromToPostal = models.CharField(max_length=100)
    distance_km = models.DecimalField(max_digits=10, decimal_places=3)
    min_n = models.DecimalField(max_digits=10, decimal_places=5)
    min_plus_svc_time = models.DecimalField(max_digits=10, decimal_places=5)
    Caregiver = models.CharField(max_length=100)
    Pick_up_Time_Format = models.CharField(max_length=100)
    Pick_up_Time_Delivery = models.CharField(max_length=100)
    IH_OS = models.CharField(max_length=100)
    Cluster = models.CharField(max_length=100)

    
