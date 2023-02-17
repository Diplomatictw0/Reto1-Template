"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import selectionsort as se
from DISClib.Algorithms.Sorting import mergesort as merg
from DISClib.Algorithms.Sorting import quicksort as quk
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá
dos listas, una para los videos, otra para las categorias de los mismos.
"""

# Construccion de modelos


def new_data_structs():
    """
    Inicializa las estructuras de datos del modelo. Las crea de
    manera vacía para posteriormente almacenar la información.
    """
    data_structs = {
        "data": None,
    }

    data_structs["data"] = lt.newList(datastructure="ARRAY_LIST",
                                     cmpfunction=compare)

    return data_structs


# Funciones para agregar informacion al modelo

def add_data(data_structs, data):
    """
    Función para agregar nuevos elementos a la lista
    """
    d = new_data(data["id"], data["info"])
    lt.addLast(data_structs["data"], d)

    return data_structs


# Funciones para creacion de datos

"""def new_data(id, info):
Crea una nueva estructura para modelar los datos
   data = {'id': 0, "info": ""}
    data["id"] = id
    data["info"] = info

    return data"""

def new_data(Anio,Codigo_actividad_económica,Nombre_actividad_economica,Codigo_sector_economico,Nombre_sector_economico,Codigo_subsector_economico,Nombre_subsector_economico,Costos_y_gastos_nomina,Aportes_seguridad,Aportes_a_entidades,Efectivo_y_equivalentes,Inversiones_e_instrumentos,Cuentas_y_otros_por_cobrar,Inventarios,Propiedades,Otros_activos,Total_patrimonio_bruto,Pasivos,Total_patrimonio_liquido,Ingresos_ordinarios,Ingresos_financieros,Otros_ingresos,Total_ingresos_brutos,Devoluciones_rebajas,Ingresos_no_renta,Total_ingresos_netos,Costos,Gastos_administracion,Gastos_distribucion,Gastos_financieros,Otros_gastos,Total_costos_y_gastos,Renta_liquida_ordinaria,Perdida_liquida,Compensaciones,Renta_liquida,Renta_presuntiva,Renta_exenta,Rentas_gravables,Renta_liquida_gravable,Ingresos_ganancias_ocasionales,Costos_ganancias_ocasionales,Ganancias_ocasionales_no_gravadas,Ganancias_ocasionales_gravables,Impuesto_RLG,Descuentos_tributarios,Impuesto_neto_de_renta,Impuesto_ganancias_ocasionales,Total_Impuesto_a_cargo,Anticipo_renta_anio_anterior,Saldo_a_favor_anio_anterior,Autorretenciones,Otras_retenciones,Total_retenciones, Anticipo_renta_siguiente_anio,Saldo_a_pagar_por_impuesto,Sanciones,Total_saldo_a_pagar,Total_saldo_a_favor):
    data= {"Año":Anio,"Código actividad económica":Codigo_actividad_económica,"Nombre actividad económica":Nombre_actividad_economica,"Código sector económico":Codigo_sector_economico,"Nombre sector económico":Nombre_sector_economico,"Código subsector económico":Codigo_subsector_economico,"Nombre subsector económico":Nombre_subsector_economico,"Costos y gastos nómina":Costos_y_gastos_nomina,"Aportes seguridad":Aportes_seguridad,"Aportes a entidades":Aportes_a_entidades,"Efectivo y equivalentes":Efectivo_y_equivalentes,"Inversiones e instrumentos":Inversiones_e_instrumentos,"Cuentas y otros por cobrar":Cuentas_y_otros_por_cobrar,"Inventarios":Inventarios,"Propiedades":Propiedades,"Otros activos":Otros_activos,"Total patrimonio bruto":Total_patrimonio_bruto,"Pasivos":Pasivos,"Total patrimonio líquido":Total_patrimonio_liquido,"Ingresos ordinarios":Ingresos_ordinarios,"Ingresos financieros":Ingresos_financieros,"Otros ingresos":Otros_ingresos,"Total ingresos brutos":Total_ingresos_brutos,"Devoluciones , rebajas":Devoluciones_rebajas,"Ingresos no renta":Ingresos_no_renta,"Total ingresos netos":Total_ingresos_netos,"Costos":Costos,"Gastos administración":Gastos_administracion,"Gastos distribución":Gastos_distribucion,"Gastos financieros":Gastos_financieros,"Otros gastos":Otros_gastos,"Total costos y gastos":Total_costos_y_gastos,"Renta líquida ordinaria":Renta_liquida_ordinaria,"Pérdida líquida":Perdida_liquida,"Compensaciones":Compensaciones,"Renta líquida":Renta_liquida,"Renta presuntiva":Renta_presuntiva,"Renta exenta":Renta_exenta,"Rentas gravables":Rentas_gravables,"Renta líquida gravable":Renta_liquida_gravable,"Ingresos ganancias ocasionales":Ingresos_ganancias_ocasionales,"Costos ganancias ocasionales":Costos_ganancias_ocasionales,"Ganancias ocasionales no gravadas":Ganancias_ocasionales_no_gravadas,"Ganancias ocasionales gravables":Ganancias_ocasionales_gravables,"Impuesto RLG":Impuesto_RLG,"Descuentos tributarios":Descuentos_tributarios,"Impuesto neto de renta":Impuesto_neto_de_renta,"Impuesto ganancias ocasionales":Impuesto_ganancias_ocasionales,"Total Impuesto a cargo":Total_Impuesto_a_cargo,"Anticipo renta año anterior":Anticipo_renta_anio_anterior,"Saldo a favor año anterior":Saldo_a_favor_anio_anterior,"Autorretenciones":Autorretenciones,"Otras retenciones":Otras_retenciones,"Total retenciones":Total_retenciones,"Anticipo renta siguiente año":Anticipo_renta_siguiente_anio,"Saldo a pagar por impuesto":Saldo_a_pagar_por_impuesto,"Sanciones":Sanciones,"Total saldo a pagar":Total_saldo_a_pagar,"Total saldo a favor":Total_saldo_a_favor}
    return data

# Las tres funciones anteriores no funcionan al revisar los documentos su funcionamien va a conducir a un error por sintaxis.

# Funciones de consulta

def get_data(data_structs, id):
    """
    Retorna un dato a partir de su ID
    """
    pos_data = lt.isPresent(data_structs["data"], id)
    if pos_data > 0:
        data = lt.getElement(data_structs["data"], pos_data)
        return data
    return None


def data_size(data_structs):
    """
    Retorna el tamaño de la lista de datos
    """
    return lt.size(data_structs["data"])


def req_1(data_structs):
    """
    Función que soluciona el requerimiento 1
    """
    # TODO: Realizar el requerimiento 1
    pass


def req_2(data_structs):
    """
    Función que soluciona el requerimiento 2
    """
    # TODO: Realizar el requerimiento 2
    pass


def req_3(data_structs):
    """
    Función que soluciona el requerimiento 3
    """
    # TODO: Realizar el requerimiento 3
    pass


def req_4(data_structs):
    """
    Función que soluciona el requerimiento 4
    """
    # TODO: Realizar el requerimiento 4
    pass


def req_5(data_structs):
    """
    Función que soluciona el requerimiento 5
    """
    # TODO: Realizar el requerimiento 5
    pass


def req_6(data_structs):
    """
    Función que soluciona el requerimiento 6
    """
    # TODO: Realizar el requerimiento 6
    pass


def req_7(data_structs):
    """
    Función que soluciona el requerimiento 7
    """
    # TODO: Realizar el requerimiento 7
    pass


def req_8(data_structs):
    """
    Función que soluciona el requerimiento 8
    """
    # TODO: Realizar el requerimiento 8
    pass


# Funciones utilizadas para comparar elementos dentro de una lista

def compare(data_1, data_2):
    """
    Función encargada de comparar dos datos
    """
    if data_1["id"] > data_2["id"]:
        return 1
    elif data_1["id"] < data_2["id"]:
        return -1
    else:
        return 0

# Funciones de ordenamiento


def sort_criteria(data_1, data_2):
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento

    Args:
        data1 (_type_): _description_
        data2 (_type_): _description_

    Returns:
        _type_: _description_
    """
    return data_1["id"] > data_2["id"]


def sort(data_structs):
    """
    Función encargada de ordenar la lista con los datos
    """
    sa.sort(data_structs["data"], sort_criteria)
