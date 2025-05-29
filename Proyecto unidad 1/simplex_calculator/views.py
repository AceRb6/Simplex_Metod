# simplex_calculator/views.py

import json
from django.http import JsonResponse
from django.shortcuts import render

def calculator(request):
    return render(request, 'calculator.html')

def solve_simplex(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            # Aquí irá la lógica para resolver Simplex
            print("Datos recibidos:", data)

            # Ejemplo de respuesta (simulada)
            result = {
                "status": "success",
                "solution": {
                    "x1": 3,
                    "x2": 2,
                    "z": 23
                },
                "steps": ["Paso 1...", "Paso 2..."]
            }

            return JsonResponse(result)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    else:
        return JsonResponse({"error": "Método no permitido"}, status=405)
    
def resultado(request):
    return render(request, 'resultado.html')