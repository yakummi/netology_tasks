from django.shortcuts import render

def handler_omlet(request):
    try:
        quantity = int(request.GET.get('servings', 1))
        context = {
          'recipe': {
            'яйца, шт': 2*quantity,
            'молоко, л': round(0.1*quantity, 1),
            'соль, ч.л.': round(0.5*quantity, 1),
          }
        }
        return render(request, 'index.html', context)
    except Exception as ex:
        context = {
            'recipe': {
                'яйца, шт': 2,
                'молоко, л': 0.1,
                'соль, ч.л.': 0.5
            }
        }
        return render(request, 'index.html', context)

def handler_pasta(request):
    try:
        quantity = int(request.GET.get('servings', 1))
        context = {
          'recipe': {
            'макароны, г': round(0.3*quantity, 1),
            'сыр, г': round(0.05*quantity, 1),
          }
        }
        return render(request, 'index.html', context)
    except Exception as ex:
        context = {
            'recipe': {
                'макароны, г': 0.3,
                'сыр, г': 0.05
            }
        }
        return render(request, 'index.html', context)

def handler_buter(request):
    try:
        quantity = int(request.GET.get('servings', 1))
        context = {
          'recipe': {
            'хлеб, ломтик': round(1*quantity, 1),
            'колбаса, ломтик': round(1*quantity, 1),
            'сыр, ломтик': round(1*quantity, 1),
            'помидор, ломтик': round(1*quantity, 1)
          }
        }
        return render(request, 'index.html', context)

    except Exception as ex:
        context = {
            'recipe': {
                'хлеб, ломтик': 1,
                'колбаса, ломтик': 1,
                'сыр, ломтик': 1,
                'помидор, ломтик': 1,
            }
        }
        return render(request, 'index.html', context)
