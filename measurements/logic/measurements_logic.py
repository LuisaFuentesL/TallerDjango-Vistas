import variables
from ..models import Measurement
from ..models import Variable

def get_measurements():
    measurements = Measurement.objects.all()
    return measurements

def get_measurement(var_pk):
    measurement = Measurement.objects.get(pk=var_pk)
    return measurement

def update_measurement(var_pk, new_var):
    measurement = get_measurement(var_pk)
    vari=Variable.objects.get(pk=new_var["variable"])
    measurement.variable= vari
    measurement.value = new_var["value"]
    measurement.unit = new_var["unit"]
    measurement.place = new_var["place"]
    measurement.save()
    return measurement

def create_measurement(var):
    vari=Variable.objects.get(pk=var["variable"])
    measurement = Measurement(variable=vari, value=var["value"], unit=var["unit"], place=var["place"], dateTime=var["date"])
    measurement.save()
    return measurement

def delete_measurement(var_pk):
    measurement = get_measurement(var_pk)
    measurement.delete()

    return measurement