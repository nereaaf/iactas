from models import Familias, FamiliasSchema, UsuariosSchema,Ciclos, CiclosSchema, Regimen, RegimenSchema
from __init__ import app, bd
from flask import request, jsonify
from models import *

#USUARIOS
usuario_schema= UsuariosSchema()
usuarios_schema= UsuariosSchema(many=True)
    
@app.route('/usuarios/ver', methods=['GET'])
def ver_usuario():
    usuarios = Usuarios.query.all()
    result = usuarios_schema.dump(usuarios)
    return jsonify(result)

@app.route('/usuarios/insertar', methods=['POST'])
def insertar_usuario():
    dni = request.json['dni']
    nombre = request.json['nombre']
    apellido1 = request.json['apellido1']
    apellido2 = request.json['apellido2']
    email = request.json['email']
    password = request.json['password']

    nuevo_usuario = Usuarios(dni, nombre, apellido1, apellido2,
    email, password)

    bd.session.add(nuevo_usuario)
    bd.session.commit()

    return usuario_schema.jsonify(nuevo_usuario)

@app.route('/usuarios/borrar/<id>', methods=['DELETE'])
def borrar_usuario(id):
    usuario = Usuarios.query.get(id)
    bd.session.delete(usuario)
    bd.session.commit()

    return usuario_schema.jsonify(usuario)

@app.route('/usuarios/actualizar/<id>', methods=['PUT'])
def actualizar_usuario(id):
    
    usuario = Usuarios.query.get(id)
    dni = request.json['dni']
    usuario.dni = dni
    nombre = request.json['nombre']
    usuario.nombre = nombre
    apellido1 = request.json['apellido1']
    usuario.apellido1 = apellido1
    apellido2 = request.json['apellido2']
    usuario.apellido2 = apellido2
    email = request.json['email']
    usuario.email = email
    password = request.json['password']
    usuario.password = password
    bd.session.commit()

    return usuario_schema.jsonify(usuario)

# ----------------------------------------------------------------------------------

#ADMINISTRADORES
administrador_schema= AdministradoresSchema()
administradores_schema= AdministradoresSchema(many=True)
    
@app.route('/administradores/ver', methods=['GET'])
def ver_administrador():
    administradores = Administradores.query.all()
    result = administradores_schema.dump(administradores)
    return jsonify(result)

# ----------------------------------------------------------------------------------

#FAMILIAS
familia_schema = FamiliasSchema()
familias_schema = FamiliasSchema(many=True)

@app.route('/familias/ver', methods=['GET'])
def ver_familia():
    familias = Familias.query.all()
    result = familias_schema.dump(familias)
    return jsonify(result)

@app.route('/familias/insertar', methods=['POST'])
def insertar_familia():
    nombre = request.json['nombre']

    nueva_familia = Familias(nombre)

    bd.session.add(nueva_familia)
    bd.session.commit()

    return familia_schema.jsonify(nueva_familia)

@app.route('/familias/borrar/<id>', methods=['DELETE'])
def borrar_familia(id):
    familia = Familias.query.get(id)
    bd.session.delete(familia)
    bd.session.commit()

    return familia_schema.jsonify(familia)

@app.route('/familias/actualizar/<id>', methods=['PUT'])
def actualizar_familia(id):
    familia = Familias.query.get(id)
    nombre = request.json['nombre']
    familia.nombre = nombre
    bd.session.commit()

    return familia_schema.jsonify(familia)

# ----------------------------------------------------------------------------------

#CICLOS
ciclo_schema = CiclosSchema()
ciclos_schema = CiclosSchema(many=True)

@app.route('/ciclos/ver', methods=['GET'])
def ver_ciclo():
    ciclos = Ciclos.query.all()
    result = ciclos_schema.dump(ciclos)
    return jsonify(result)

@app.route('/ciclos/insertar', methods=['POST'])
def insertar_ciclo():
    id_ciclo = request.json['id_ciclo']
    nombre = request.json['nombre']
    real_decreto = request.json['real_decreto']
    decreto = request.json['decreto']
    id_familia = request.json['id_familia']

    nuevo_ciclo = Ciclos(id_ciclo, nombre, real_decreto, decreto, id_familia)

    bd.session.add(nuevo_ciclo)
    bd.session.commit()

    return ciclo_schema.jsonify(nuevo_ciclo)

@app.route('/ciclos/borrar/<id>', methods=['DELETE'])
def borrar_ciclo(id):
    ciclo = Ciclos.query.get(id)
    bd.session.delete(ciclo)
    bd.session.commit()

    return ciclo_schema.jsonify(ciclo)

@app.route('/ciclos/actualizar/<id>', methods=['PUT'])
def actualizar_ciclo(id):
    ciclo = Ciclos.query.get(id)

    id_ciclo = request.json['id_ciclo']
    ciclo.id_ciclo = id_ciclo
    nombre = request.json['nombre']
    ciclo.nombre = nombre
    real_decreto = request.json['real_decreto']
    ciclo.real_decreto = real_decreto
    decreto = request.json['decreto']
    ciclo.decreto = decreto
    id_familia = request.json['id_familia']
    ciclo.id_familia = id_familia
    
    bd.session.commit()

    return ciclo_schema.jsonify(ciclo)

# ----------------------------------------------------------------------------------

#CURSOS
curso_schema = CursosSchema()
cursos_schema = CursosSchema(many=True)

@app.route('/cursos/ver', methods=['GET'])
def ver_curso():
    cursos = Cursos.query.all()
    result = cursos_schema.dump(cursos)
    return jsonify(result)

@app.route('/cursos/insertar', methods=['POST'])
def insertar_curso():
    num_curso = request.json['num_curso']
    id_ciclo = request.json['id_ciclo']

    nuevo_curso = Cursos(num_curso, id_ciclo)

    bd.session.add(nuevo_curso)
    bd.session.commit()

    return ciclo_schema.jsonify(nuevo_curso)

@app.route('/cursos/borrar/<id>', methods=['DELETE'])
def borrar_curso(id):
    curso = Cursos.query.get(id)
    bd.session.delete(curso)
    bd.session.commit()

    return curso_schema.jsonify(curso)

@app.route('/cursos/actualizar/<id>', methods=['PUT'])
def actualizar_curso(id):
    curso = Cursos.query.get(id)

    num_curso = request.json['num_curso']
    curso.num_curso = num_curso
    id_ciclo = request.json['id_ciclo']
    curso.id_ciclo = id_ciclo
    
    bd.session.commit()

    return ciclo_schema.jsonify(curso)

# ----------------------------------------------------------------------------------

#CENTROS
centro_schema = CentrosSchema()
centros_schema = CentrosSchema(many=True)

@app.route('/centros/ver', methods=['GET'])
def ver_centro():
    centros = Centros.query.all()
    result = centros_schema.dump(centros)
    return jsonify(result)

@app.route('/centros/insertar', methods=['POST'])
def insertar_centro():
    cod_centro = request.json['cod_centro']
    nombre = request.json['nombre']
    titularidad = request.json['titularidad']
    direccion = request.json['direccion']
    cp = request.json['cp']
    localidad = request.json['localidad']
    concejo = request.json['concejo']
    provincia = request.json['provincia']
    tlfno = request.json['tlfno']
    fax = request.json['fax']
    correo = request.json['correo']

    nuevo_centro = Centros(cod_centro, nombre, titularidad, direccion, cp, localidad, concejo, provincia, tlfno, fax, correo)

    bd.session.add(nuevo_centro)
    bd.session.commit()

    return centro_schema.jsonify(nuevo_centro)

@app.route('/centros/borrar/<id>', methods=['DELETE'])
def borrar_centro(id):
    centro = Centros.query.get(id)
    bd.session.delete(centro)
    bd.session.commit()

    return centro_schema.jsonify(centro)

@app.route('/centros/actualizar/<id>', methods=['PUT'])
def actualizar_centro(id):
    centro = Centros.query.get(id)

    cod_centro = request.json['cod_centro']
    centro.cod_centro = cod_centro
    nombre = request.json['nombre']
    centro.nombre = nombre
    titularidad = request.json['titularidad']
    centro.titularidad = titularidad
    direccion = request.json['direccion']
    centro.direccion = direccion
    cp = request.json['cp']
    centro.cp = cp
    localidad = request.json['localidad']
    centro.localidad = localidad
    concejo = request.json['concejo']
    centro.concejo = concejo
    provincia = request.json['provincia']
    centro.provincia = provincia
    tlfno = request.json['tlfno']
    centro.tlfno = tlfno
    fax = request.json['fax']
    centro.fax = fax
    correo = request.json['correo']
    centro.correo = correo
    
    bd.session.commit()

    return centro_schema.jsonify(centro)

# ----------------------------------------------------------------------------------

#CURSOS_HAS_CENTROS
curso_has_centro_schema = Cursos_has_centrosSchema()
cursos_has_centros_schema = Cursos_has_centrosSchema(many=True)

@app.route('/cursos_has_centros/ver', methods=['GET'])
def ver_cursos_has_centros():
    cursos_has_centros = Cursos_has_centros.query.all()
    result = cursos_has_centros_schema.dump(cursos_has_centros)
    return jsonify(result)

@app.route('/cursos_has_centros/insertar', methods=['POST'])
def insertar_cursos_has_centros():
    id_curso = request.json['id_curso']
    cod_centro = request.json['cod_centro']

    nuevo_curso_has_centro = Cursos_has_centros(id_curso, cod_centro)

    bd.session.add(nuevo_curso_has_centro)
    bd.session.commit()

    return curso_has_centro_schema.jsonify(nuevo_curso_has_centro)

#@app.route('/cursos_has_centros/borrar', methods=['DELETE'])
#def borrar_cursos_has_centros():
    id_curso = request.json['id_curso']
    cod_centro = request.json['cod_centro']
    print(id_curso, cod_centro)
    cursos_has_centros = Cursos_has_centros.query(Cursos_has_centros).filter(Cursos_has_centros.id_curso == id_curso and Cursos_has_centros.cod_centro == cod_centro)
    bd.session.delete(cursos_has_centros)
    bd.session.commit()

    return curso_has_centro_schema.jsonify(cursos_has_centros)

#@app.route('/cursos_has_centros/actualizar/<id>', methods=['PUT'])
#def actualizar_cursos_has_centros(id):
    curso_has_centro = Cursos_has_centros.query.get(id)

    id_curso = request.json['id_curso']
    curso_has_centro.id_curso = id_curso
    cod_centro = request.json['cod_centro']
    curso_has_centro.cod_centro = cod_centro
    
    bd.session.commit()

    return curso_has_centro_schema.jsonify(curso_has_centro)

# ----------------------------------------------------------------------------------

#MODULOS
modulo_schema = ModulosSchema()
modulos_schema = ModulosSchema(many=True)

@app.route('/modulos/ver', methods=['GET'])
def ver_modulo():
    modulos = Modulos.query.all()
    result = modulos_schema.dump(modulos)
    return jsonify(result)

@app.route('/modulos/insertar', methods=['POST'])
def insertar_modulo():
    cod_mod = request.json['cod_mod']
    nombre = request.json['nombre']
    nombre_abrev = request.json['nombre_abrev']
    id_curso = request.json['id_curso']

    nuevo_modulo = Modulos(cod_mod, nombre, nombre_abrev, id_curso)

    bd.session.add(nuevo_modulo)
    bd.session.commit()

    return modulo_schema.jsonify(nuevo_modulo)

@app.route('/modulos/borrar/<id>', methods=['DELETE'])
def borrar_modulo(id):
    modulo = Modulos.query.get(id)
    bd.session.delete(modulo)
    bd.session.commit()

    return modulo_schema.jsonify(modulo)

@app.route('/modulos/actualizar/<id>', methods=['PUT'])
def actualizar_modulo(id):
    modulo = Modulos.query.get(id)

    cod_mod = request.json['cod_mod']
    modulo.cod_mod = cod_mod
    nombre = request.json['nombre']
    modulo.nombre = nombre
    nombre_abrev = request.json['nombre_abrev']
    modulo.nombre_abrev = nombre_abrev
    id_curso = request.json['id_curso']
    modulo.id_curso = id_curso
    
    bd.session.commit()

    return modulo_schema.jsonify(modulo)

# ----------------------------------------------------------------------------------

#REGIMENES
regimen_schema = RegimenSchema()
regimenes_schema = RegimenSchema(many=True)

@app.route('/regimenes/ver', methods=['GET'])
def ver_regimen():
    regimenes = Regimen.query.all()
    result = regimenes_schema.dump(regimenes)
    return jsonify(result)
    
# ----------------------------------------------------------------------------------

#VIAS ACCESO
via_acceso_schema = Vias_accesoSchema()
vias_acceso_schema = Vias_accesoSchema(many=True)

@app.route('/vias_acceso/ver', methods=['GET'])
def ver_via_acceso():
    vias_acceso = Vias_acceso.query.all()
    result = vias_acceso_schema.dump(vias_acceso)
    return jsonify(result)

# ----------------------------------------------------------------------------------

#SESIONES
sesion_schema = SesionesSchema()
sesiones_schema = SesionesSchema(many=True)

#@app.route('/sesiones/ver', methods=['GET'])
#def ver_sesiones():
    #sesiones = Sesiones.query.all()
    #result = sesiones_schema.dump(sesiones)
    #return jsonify(result)

# ----------------------------------------------------------------------------------

#FECHAS EVALUACIÓN
fecha_evaluacion_schema = Fechas_evaluacionSchema()
fechas_evaluacion_schema = Fechas_evaluacionSchema(many=True)

@app.route('/fechas_evaluacion/ver', methods=['GET'])
def ver_fechas_evaluacion():
    fechas_evaluacion = Fechas_evaluacion.query.all()
    result = fechas_evaluacion_schema.dump(fechas_evaluacion)
    return jsonify(result)

@app.route('/fechas_evaluacion/insertar', methods=['POST'])
def insertar_fecha_evaluacion():
    cod_sesion = request.json['cod_sesion']
    fecha_curso = request.json['fecha_curso']
    fecha_eval = request.json['fecha_eval']
    id_sesion = request.json['id_sesion']

    nueva_fecha_evaluacion = Fechas_evaluacion(cod_sesion, fecha_curso, fecha_eval, id_sesion)

    bd.session.add(nueva_fecha_evaluacion)
    bd.session.commit()

    return fecha_evaluacion_schema.jsonify(nueva_fecha_evaluacion)

@app.route('/fechas_evaluacion/borrar/<id>', methods=['DELETE'])
def borrar_fecha_evaluacion(id):
    fecha_evaluacion = Fechas_evaluacion.query.get(id)
    bd.session.delete(fecha_evaluacion)
    bd.session.commit()

    return fecha_evaluacion_schema.jsonify(fecha_evaluacion)

@app.route('/fechas_evaluacion/actualizar/<id>', methods=['PUT'])
def actualizar_fecha_evaluacion(id):
    fecha_evaluacion = Fechas_evaluacion.query.get(id)

    cod_sesion = request.json['cod_sesion']
    fecha_evaluacion.cod_sesion = cod_sesion
    fecha_curso = request.json['fecha_curso']
    fecha_evaluacion.fecha_curso = fecha_curso
    fecha_eval = request.json['fecha_eval']
    fecha_evaluacion.fecha_eval = fecha_eval
    id_sesion = request.json['id_sesion']
    fecha_evaluacion.id_sesion = id_sesion
    
    bd.session.commit()

    return fecha_evaluacion_schema.jsonify(fecha_evaluacion)

# ----------------------------------------------------------------------------------

#MATRICULACIONES
matricula_schema = MatriculacionesSchema()
matriculaciones_schema = MatriculacionesSchema(many=True)

#@app.route('/matriculaciones/ver', methods=['GET'])
#def ver_matriculaciones():
    #matriculaciones = Matriculaciones.query.all()
    #result = matriculaciones_schema.dump(matriculaciones)
    #return jsonify(result)












@app.route('/')
def hello():
    return 'Hola holita vecinitos'

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)