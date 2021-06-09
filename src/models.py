from __init__ import bd, ma

# MODELOS DE TABLAS
class Usuarios(bd.Model):
    __tablename__ = 'usuarios'
    dni = bd.Column(bd.String(9), primary_key=True, nullable=False)
    nombre = bd.Column(bd.String(45), nullable=False)
    apellido1 = bd.Column(bd.String(45), nullable=False)
    apellido2 = bd.Column(bd.String(45), nullable=False)
    email = bd.Column(bd.String(100), nullable=False)
    password = bd.Column(bd.String(20), nullable=False)
   
    def __init__(self, dni, nombre, apellido1, apellido2, email, password):
        self.dni = dni
        self.nombre = nombre
        self.apellido1 = apellido1
        self.apellido2 = apellido2
        self.email = email
        self.password = password

class UsuariosSchema(ma.Schema):
    class Meta:
        fields = ('dni', 'nombre', 'apellido1', 'apellido2', 'email', 'password') # hereda todos los campos del modelo Usuarios

# ----------------------------------------------------------------------------------

class Administradores(bd.Model):
    __tablename__ = 'administradores'
    # foreign key Usuarios --> dni
    dni_admin = bd.Column(bd.String(9), bd.ForeignKey('usuarios.dni'), primary_key=True, nullable=False)

    def __init__(self, dni_admin):
        self.dni_admin = dni_admin

class AdministradoresSchema(ma.Schema):
    class Meta:
        fields=['dni_admin']

# ----------------------------------------------------------------------------------

class Profesores(bd.Model):
    __tablename__ = 'profesores'
    # foreign key Usuarios --> dni
    dni_profesor = bd.Column(bd.String(9), bd.ForeignKey('usuarios.dni'), primary_key=True, nullable=False)

    def __init__(self, dni_profesor):
        self.dni_profesor = dni_profesor

class ProfesoresSchema(ma.Schema):
    class Meta:
        fields=['dni_profesor']

# ----------------------------------------------------------------------------------

class Alumnos(bd.Model):
    __tablename__ = 'alumnos'
    # foreign key Usuarios --> dni
    dni_alumno = bd.Column(bd.String(9), bd.ForeignKey('usuarios.dni'), primary_key=True, nullable=False)
    tlfno = bd.Column(bd.String(9), nullable=False)
    fechanac = bd.Column(bd.String(10), nullable=False)
    lugarnac = bd.Column(bd.String(30), nullable=False)
    nacionalidad = bd.Column(bd.String(30), nullable=False)
    domicilio = bd.Column(bd.String(100), nullable=False)
    localidad = bd.Column(bd.String(30), nullable=False)
    cp = bd.Column(bd.String(5), nullable=False)
    municipio = bd.Column(bd.String(45), nullable=False)
    provincia = bd.Column(bd.String(45), nullable=False)
    pais = bd.Column(bd.String(45), nullable=False)

    def __init__(self, dni_alumno, tlfno, fechanac, lugarnac, nacionalidad, domicilio, localidad, cp, municipio, provincia, pais):
        self.dni_alumno = dni_alumno
        self.tlfno = tlfno
        self.fechanac = fechanac
        self.lugarnac = lugarnac
        self.nacionalidad = nacionalidad
        self.domicilio = domicilio
        self.localidad = localidad
        self.cp = cp
        self.municipio = municipio
        self.provincia = provincia
        self.pais = pais

class AlumnosSchema(ma.Schema):
    class Meta:
        fields=('dni_alumno', 'tlfno', 'fechanac', 'lugarnac', 'nacionalidad', 'domicilio', 'localidad', 'cp', 'municipio', 'provincia', 'pais')

# ----------------------------------------------------------------------------------

class Familias(bd.Model):
    __tablename__ = 'familias'
    id_familia = bd.Column(bd.Integer, primary_key=True, nullable=False)
    nombre = bd.Column(bd.String(45), nullable=False)
    # referencia a model Ciclos

    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return self.nombre

class FamiliasSchema(ma.Schema):
    class Meta:
        fields=('id_familia','nombre')

# ----------------------------------------------------------------------------------

class Ciclos(bd.Model):
    __tablename__ = 'ciclos'
    id_ciclo = bd.Column(bd.String(7), primary_key=True, nullable=False)
    nombre = bd.Column(bd.String(60), nullable=False)
    real_decreto = bd.Column(bd.String(100), nullable=False)
    decreto = bd.Column(bd.String(100), nullable=False)
    id_familia = bd.Column(bd.Integer, bd.ForeignKey('familias.id_familia'), nullable=False)

    def __init__(self, id_ciclo, nombre, real_decreto, decreto, id_familia):
        self.id_ciclo = id_ciclo
        self.nombre = nombre
        self.real_decreto = real_decreto
        self.decreto = decreto
        self.id_familia = id_familia

class CiclosSchema(ma.Schema):
    class Meta:
        fields=('id_ciclo', 'nombre', 'real_decreto', 'decreto', 'id_familia')

# ----------------------------------------------------------------------------------

class Cursos(bd.Model):
    __tablename__ = 'cursos'
    id_curso = bd.Column(bd.Integer, primary_key=True, nullable=False)
    num_curso = bd.Column(bd.String(2), nullable=False)
    id_ciclo = bd.Column(bd.String(7), bd.ForeignKey('ciclos.id_ciclo'), nullable=False)

    def __init__(self, num_curso, id_ciclo):
        self.num_curso = num_curso
        self.id_ciclo = id_ciclo

class CursosSchema(ma.Schema):
    class Meta:
        fields=('num_curso', 'id_ciclo')

# ----------------------------------------------------------------------------------

class Centros(bd.Model):
    __tablename__ = 'centros'
    cod_centro = bd.Column(bd.String(8), primary_key=True, nullable=False)
    nombre = bd.Column(bd.String(100), nullable=False)
    titularidad = bd.Column(bd.String(45), nullable=False)
    direccion = bd.Column(bd.String(100), nullable=False)
    cp = bd.Column(bd.String(5), nullable=False)
    localidad = bd.Column(bd.String(30), nullable=False)
    concejo = bd.Column(bd.String(30), nullable=False)
    provincia = bd.Column(bd.String(45), nullable=False)
    tlfno = bd.Column(bd.String(9), nullable=False)
    fax = bd.Column(bd.String(50), nullable=True)
    correo = bd.Column(bd.String(45), nullable=False)

    def __init__(self, cod_centro, nombre, titularidad, direccion, cp, localidad, concejo, provincia, tlfno, fax, correo):
        self.cod_centro = cod_centro
        self.nombre = nombre
        self.titularidad = titularidad
        self.direccion = direccion
        self.cp = cp
        self.localidad = localidad
        self.concejo = concejo
        self.provincia = provincia
        self.tlfno = tlfno
        self.fax = fax
        self.correo = correo

class CentrosSchema(ma.Schema):
    class Meta:
        fields=('cod_centro', 'nombre', 'titularidad', 'direccion', 'cp', 'localidad', 'concejo', 'provincia', 'tlfno', 'fax', 'correo')

# ----------------------------------------------------------------------------------

class Cursos_has_centros(bd.Model):
    __tablename__ = 'cursos_has_centros'
    id_curso = bd.Column(bd.Integer, bd.ForeignKey('cursos.id_curso'), primary_key=True, nullable=False)
    cod_centro = bd.Column(bd.String(8), bd.ForeignKey('centros.cod_centro'), primary_key=True, nullable=False)

    def __init__(self, id_curso, cod_centro):
        self.id_curso = id_curso
        self.cod_centro = cod_centro

class Cursos_has_centrosSchema(ma.Schema):
    class Meta:
        fields=('id_curso', 'cod_centro')

# ----------------------------------------------------------------------------------

class Modulos(bd.Model):
    __tablename__ = 'modulos'
    cod_mod = bd.Column(bd.String(5), primary_key=True, nullable=False)
    nombre = bd.Column(bd.String(45), nullable=False)
    nombre_abrev = bd.Column(bd.String(7), nullable=False)
    id_curso = bd.Column(bd.Integer, bd.ForeignKey('cursos.id_curso'), nullable=False)

    def __init__(self, cod_mod, nombre, nombre_abrev, id_curso):
        self.cod_mod = cod_mod
        self.nombre = nombre
        self.nombre_abrev = nombre_abrev
        self.id_curso = id_curso

class ModulosSchema(ma.Schema):
    class Meta:
        fields=('cod_mod', 'nombre', 'nombre_abrev', 'id_curso') 

# ----------------------------------------------------------------------------------

class Regimen(bd.Model):
    __tablename__ = 'regimen'
    id_regimen = bd.Column(bd.Integer, primary_key=True, nullable=False)
    nombre_regimen = bd.Column(bd.String(15), nullable=False)

    def __init__(self, id_regimen, nombre_regimen):
        self.id_regimen = id_regimen
        self.nombre_regimen = nombre_regimen

class RegimenSchema(ma.Schema):
    class Meta:
        fields=('id_regimen', 'nombre_regimen')

# ----------------------------------------------------------------------------------

class Vias_acceso(bd.Model):
    __tablename__ = 'vias_acceso'
    id_via = bd.Column(bd.Integer, primary_key=True, nullable=False)
    nombre = bd.Column(bd.String(45), nullable=False)

    def __init__(self, id_via, nombre):
        self.id_via = id_via
        self.nombre = nombre

class Vias_accesoSchema(ma.Schema):
    class Meta:
        fields=('id_via', 'nombre')

# ----------------------------------------------------------------------------------

class Sesiones(bd.Model):
    __tablename__ = 'sesiones'
    id_sesion = bd.Column(bd.Integer, primary_key=True, nullable=False)
    tipo_sesion = bd.Column(bd.String(50), nullable=False)
    tipo_sesion_abr = bd.Column(bd.String(20), nullable=False)
    curso = bd.Column(bd.String(2), nullable=False)

    def __init__(self, id_sesion, tipo_sesion, tipo_sesion_abr, curso):
        self.id_sesion = id_sesion
        self.tipo_sesion = tipo_sesion
        self.tipo_sesion_abr = tipo_sesion_abr
        self.curso = curso

class SesionesSchema(ma.Schema):
    class Meta:
        fields=('id_sesion', 'tipo_sesion', 'tipo_sesion_abr', 'curso')

# ----------------------------------------------------------------------------------

class Fechas_evaluacion(bd.Model):
    __tablename__ = 'fechas_evaluacion'
    cod_sesion = bd.Column(bd.String(30), primary_key=True, nullable=False)
    fecha_curso = bd.Column(bd.String(9), nullable=False)
    fecha_eval = bd.Column(bd.Date, nullable=True)
    id_sesion = bd.Column(bd.Integer, bd.ForeignKey('sesiones.id_sesion'), nullable=False)

    def __init__(self, cod_sesion, fecha_curso, fecha_eval, id_sesion):
        self.cod_sesion = cod_sesion
        self.fecha_curso = fecha_curso
        self.fecha_eval = fecha_eval
        self.id_sesion = id_sesion

class Fechas_evaluacionSchema(ma.Schema):
    class Meta:
        fields=('cod_sesion', 'fecha_curso', 'fecha_eval', 'id_sesion')

# ----------------------------------------------------------------------------------

class Matriculaciones(bd.Model):
    __tablename__ = 'matriculaciones'
    n_expediente = bd.Column(bd.String(12), primary_key=True, nullable=False)
    alumno_dni = bd.Column(bd.String(9), bd.ForeignKey('alumnos.dni_alumno'), nullable=False)
    anio_academico = bd.Column(bd.String(9), nullable=False)
    via_acceso = bd.Column(bd.Integer, bd.ForeignKey('vias_acceso.id_via'), nullable=False)
    regimen = bd.Column(bd.Integer, bd.ForeignKey('regimen.id_regimen'), nullable=False)
    cod_mod = bd.Column(bd.String(5), bd.ForeignKey('modulos.cod_mod'), nullable=False)
    nota = bd.Column(bd.Integer, nullable=True)
    n_convocatoria = bd.Column(bd.Integer, nullable=True)
    cod_sesion = bd.Column(bd.String(30), bd.ForeignKey('fechas_evaluacion.cod_sesion'), nullable=True)
    cv_o_aa = bd.Column(bd.String(2), nullable=True)
    apto_noapto = bd.Column(bd.String(10), nullable=True)
    superada = bd.Column(bd.Boolean,default=False) #¿? TINYINT(1)
    

    def __init__(self, n_expediente, alumno_dni, anio_academico, via_acceso, regimen, cod_mod, nota, n_convocatoria, cod_sesion, cv_o_aa, apto_noapto, superada):
        self.n_expediente = n_expediente
        self.alumno_dni = alumno_dni
        self.anio_academico = anio_academico
        self.via_acceso = via_acceso
        self.regimen = regimen
        self.cod_mod = cod_mod
        self.nota = nota
        self.n_convocatoria = n_convocatoria
        self.cod_sesion = cod_sesion
        self.cv_o_aa = cv_o_aa
        self.apto_noapto = apto_noapto
        self.superada = superada

class MatriculacionesSchema(ma.Schema):
    class Meta:
        fields=('n_expediente', 'alumno_dni', 'anio_academico', 'via_acceso', 'regimen', 'cod_mod', 'nota', 'n_convocatoria', 'cod_sesion', 'cv_o_aa', 'apto_noapto', 'superada')



