from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from sklearn.preprocessing import StandardScaler
import numpy as np

from rest_framework_simplejwt.views import TokenObtainPairView
from api.serializers import CustomTokenObtainPairSerializer, StandarizeSerializer


class StandarizeView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        json_data = request.data

        serializer = StandarizeSerializer(data=json_data)
        if serializer.is_valid():
            # Get the data as a numpy array
            data = np.array(list(serializer.validated_data.values())).T

            # Compute the standardization using scikit learn StandardScaler
            scaler = StandardScaler()
            standardized_data = scaler.fit_transform(data)

            # Create a dictionary with the standardized data
            result = {key.replace('_', ''): list(val) for key, val in zip(json_data.keys(), standardized_data.T)}

            return Response({'success': True, 'result': result}, status=status.HTTP_200_OK)

        response_data = {"success": False, "errors": serializer.errors}
        return Response(response_data, status=status.HTTP_400_BAD_REQUEST)


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


