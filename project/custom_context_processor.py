from appCompeticion.models import deporte,competicion

def listar_deportes(request):

    return {
       'deportes_nav': deporte.objects.all(),
       'competencias_nav': competicion.objects.all(),
    }