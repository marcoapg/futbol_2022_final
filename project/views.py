from calendar import c
from django.shortcuts import render
from appArbitro.models import arbitro
from appContrato.models import contrato, persona, tipo_persona
from appEquipo.models import equipo, alineacion_equipo
from appCompeticion.models import competicion,deporte,tipo_competicion,detalle_grupo,fase,grupo
from appPartido.models import encuentro,evento_persona
from appCompeticion.models import deporte
from user.models import User

def contextoNav():
    
    deportes = deporte.objects.all()
    
    data ={
        'deportes' : deportes
    }

    return render ('nav.html', data)

def contadoresAdmin(request):
    arbitros = arbitro.objects.count()
    entrenadores = persona.objects.filter(tipo_persona_id=2).count()
    jugadores = persona.objects.filter(tipo_persona_id=1).count()
    equipos = equipo.objects.count()
    usuarios = User.objects.all()
    data = {
        'arbitros' : arbitros,
        'entrenadores' : entrenadores,
        'jugadores' : jugadores,
        'equipos' : equipos,
        'usuarios': usuarios
    }
    return render(request, 'admin/index.html', data)


def contextoCompetencias(request, nombre_deporte):

    deportes = deporte.objects.get(nombre=nombre_deporte.upper() ,estado=True)
    
    nombre_seleccion = tipo_competicion.objects.get(nombre='SELECCION')
    competencia_seleccion = competicion.objects.filter(deporte_id=deportes.deporte_id,tipo_competicion_id=nombre_seleccion, estado=True)

    nombre_club = tipo_competicion.objects.get(nombre='CLUB')
    competencia_club = competicion.objects.filter(deporte_id=deportes.deporte_id,tipo_competicion_id=nombre_club, estado=True)

    data= {
        'deporte' : deportes,
        'competencia_seleccion' : competencia_seleccion,
        'competencia_club' : competencia_club
    }

    return render(request, 'competencias.html', data)


def contextoCompetenciasFutbol(request, nombre_competicion):

    competencia_seleccionada = competicion.objects.get(nombre=nombre_competicion.upper(),estado=True)   
    fase_seleccionada = fase.objects.get(nombre='FASE DE GRUPOS')

    grupos = detalle_grupo.objects.filter(competicion_id=competencia_seleccionada.competicion_id, fase_id=fase_seleccionada.fase_id).order_by('grupo_id')

    filtro_grupos = detalle_grupo.objects.filter(competicion_id=competencia_seleccionada.competicion_id, fase_id=fase_seleccionada.fase_id).values_list('grupo_id', flat=True).distinct().order_by('grupo_id')

    nombre_grupos = []
    for f in filtro_grupos:
        busqueda_grupos = grupo.objects.get(grupo_id=f)
        nombre_grupos.append(busqueda_grupos)
    
    data={
        'competencia_seleccionada' : competencia_seleccionada,
        'grupos' : grupos,
        'nombre_grupos' : nombre_grupos
    }
    
    return render(request, 'teams.html', data)

def contextoJugador(request, alias):
    
    jugador=persona.objects.get(alias=alias.upper())

    contrato_jugador = contrato.objects.get(persona_id=jugador.persona_id, estado=True, tipo_contrato='S')

    lista_contratos_club=[]
    contratos_club= contrato.objects.filter(persona_id= jugador, tipo_contrato='C')
    for cc in contratos_club:
          lista_contratos_club.append(cc)
    
    lista_contratos_seleccion=[]
    contratos_seleccion= contrato.objects.filter(persona_id= jugador,tipo_contrato='S')
    for cs in contratos_seleccion:
          lista_contratos_seleccion.append(cs)

    data={          
        'jugador': jugador,
        'contrato': contrato_jugador,
        'contratos_club':lista_contratos_club,
        'contratos_seleccion':lista_contratos_seleccion
    }

    return render(request, 'jugador.html', data)

def contextoEncuentros(request,nombre_competicion):
    competencia_seleccionada = competicion.objects.get(nombre=nombre_competicion.upper())   
    encuentros_por_jugar = encuentro.objects.filter(competicion_id=competencia_seleccionada,estado_jugado=False)    
    encuentros_jugados = encuentro.objects.filter(competicion_id=competencia_seleccionada,estado_jugado=True)
    data={
        'encuentros_jugados' : encuentros_jugados,
        'encuentros_por_jugar': encuentros_por_jugar
    }
    return render(request,'encuentros_jugados.html',data)

def contextoEquipo(request, nombre_equipo):
    equipos = equipo.objects.get(nombre=nombre_equipo.upper())
    tipo_persona_entrenador = tipo_persona.objects.get(descripcion='ENTRENADOR')
    persona_entrenador = persona.objects.filter(tipo_persona_id=tipo_persona_entrenador.tipo_persona_id)

    entrenadoractual = []
    for p_e in persona_entrenador:
        contratosentrenadores = contrato.objects.filter(persona_id= p_e.persona_id,nuevo_club=equipos.equipo_id, estado=True)
        for ce in contratosentrenadores:
            if(ce.estado == True):
                entrenadoractual = ce

    tipo_persona_jugador = tipo_persona.objects.get(descripcion='JUGADOR')
    persona_jugador = persona.objects.filter(tipo_persona_id=tipo_persona_jugador.tipo_persona_id)

    jugadores_equipo = []
    for p_j in persona_jugador:
        contratosjugadores = contrato.objects.filter(persona_id= p_j.persona_id, nuevo_club=equipos.equipo_id, estado=True)
        for cj in contratosjugadores:
            if(cj.estado == True):
                jugadores_equipo.append(cj)

    # alineacion_equipo_final = []

    # for j in jugadores:
    #     alineacionequipo = alineacion_equipo.objects.filter(contrato_id=j.contrato_id)
    #     for ae in alineacionequipo:
    #         if(ae.estado == True or ae.estado == False):
    #             alineacion_equipo_final.append(ae)
    encuentro_local_jugar = []
    encuentros_local = encuentro.objects.filter(equipo_local=equipos.equipo_id,estado_jugado=False)
    for ejl in encuentros_local:
        encuentro_local_jugar.append(ejl)

    encuentro_visita_jugar = []
    encuentros_visita = encuentro.objects.filter(equipo_visita=equipos.equipo_id,estado_jugado=False)
    for ejv in encuentros_visita:
        encuentro_visita_jugar.append(ejv)

    data = {
        'equipo' : equipos,
        'entrenador': entrenadoractual,
        'jugadores_equipo': jugadores_equipo,
        'encuentro_local_jugar':encuentro_local_jugar,
        'encuentro_visita_jugar':encuentro_visita_jugar
    }

    return render(request, 'equipo.html', data)

def contextoFixtureCompetencia(request, nombre_competicion):
    
    competencia_seleccionada = competicion.objects.get(nombre=nombre_competicion.upper())   

    filtro_encuentros_competencia = encuentro.objects.filter(competicion_id=competencia_seleccionada.competicion_id)


    #total_detalles_encuentros = detalle_encuentro.objects.all()

    # for de in detalles_encuentros:
    #     for e in filtrar_encuentros_competencias:
    #         if (de.encuentro_id == e.encuentro_id):
    #             lista_detalles_encuentros_competencia.append(de)

    # for f in filtrar_encuentros_competencias:
    #     detalles_encuentros = detalle_encuentro.objects.filter(encuentro_id=f.encuentro_id)
    #     for de in detalles_encuentros:
    #         lista_detalles_encuentros_competencias.append(de)

    data={
        'competencia': competencia_seleccionada,
        'encuentros': filtro_encuentros_competencia
    }

    return render(request, 'fixtures.html', data)

def contextoListaJugadoresPorGoles(request,nombre_competicion):
    competencia_seleccionada = competicion.objects.get(nombre=nombre_competicion.upper()) 
    filtro_encuentros_competencia = encuentro.objects.filter(competicion_id=competencia_seleccionada.competicion_id)
    # persona_jugador = persona.objects.get(tipo_persona_id=1)
    lista_goles_persona = []
    goles_persona=evento_persona.objects.filter(evento_id=9)
    # goles=evento_persona.objects.filter(evento_id=9,persona_id=persona_jugador).count()
    for gp in goles_persona:
        lista_goles_persona.append(gp)        
    data={
        'lista_goles_persona': lista_goles_persona  
        # 'goles': goles
    }
    return render(request, 'lista_jugadores_goles.html', data)

def contextoTablaPosiciones(request,competencia,grupos):

    data={

    }    
    return render(request, 'tabla_posiciones.html', data)

def contextoContacto(request):
    data={

    }
    
    return render(request, 'contact.html', data)

def index(request):
    data={
        
    }
    return render(request, 'index.html', data)
