from django.shortcuts import render
from django.db.models import Q
from .models import *


def index(request):
    print(Categoria.objects.all())
    moda_caballeros = Producto.objects.filter(genero__nombre="Caballeros")
    moda_damas = Producto.objects.filter(genero__nombre="Damas")
    promociones = Producto.objects.filter(promocion=True)

    return render(request, 'Home.html', {
        'caballeros': moda_caballeros,
        'damas': moda_damas,
        'promociones': promociones
    })


def categorias(request, categoriaUsuario):
    try:
        print(categoriaUsuario)
        producto = Producto.objects.filter(genero__nombre__icontains=categoriaUsuario)
        print(producto)

        return render(request, 'Generos.html', {
            'productos': producto
        })
    except:
        return render(request, 'Generos.html')


def producto(request, id):
    producto = Producto.objects.get(id=id)
    print(producto)
    return render(request, 'Producto.html', {
        'producto': producto
    })


def buscar_producto(request):
    busqueda = request.GET["search"]
    print(busqueda)

    try:
        productos = Producto.objects.filter(Q(nombre__icontains=busqueda) | Q(categoria__nombre__icontains=busqueda))
        print(productos)
        return render(request, 'Generos.html', {
            'mensaje': f"Producto: {busqueda}",
            'productos': productos,
            'encontrado': True
        })
    except:
        print("No se pudo encontrar")
        return render(request, 'Generos.html', {
            'mensaje': f"No se encontraron resultados para {busqueda}",
            'encontrado': False
        })
