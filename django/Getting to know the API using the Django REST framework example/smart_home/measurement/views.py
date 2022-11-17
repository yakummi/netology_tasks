from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView, ListCreateAPIView
from .models import Sensor, Measurement
from .serializers import MeasurementSerializer, SensorDetailSerializer

class SensorsView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


class SingleSensorView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


class MeasurementCreateView(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
