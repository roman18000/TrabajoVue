from sqlalchemy.sql.expression import _True
from app.models.coordinate import Coordinate
from app.models.permission import Role, Permission
from app.models.user import User
from app.db import db
from app.models.point import Point
from app.models.configuration import Configuration
from app.models.views_sort import View
from app.models.issue import Issue

from app.dao.route_of_evacuation import Route_of_evacuationDAO

from app.dao.report import ReportDAO

#Creo y agregago la configuraicon

config = Configuration("Amarillo",5)
db.session.add(config)
db.session.commit()


#Creo y agrego las issues de prueba


issue1 = Issue('fede@mail.com', 'No puedo iniciar sesion correctamente', 1, 1)
issue2 = Issue('jose@mail.com', 'El sistema de dice que hay un error', 1, 2)
issue3 = Issue('maria@mail.com', 'No tengo acceso al sistema', 1, 1)
issue4 = Issue('Josue@mail.com', 'No tengo acceso al sistema', 1, 1)
issue5 = Issue('Pedrinio@mail.com', 'No tengo acceso a mi cuenta', 1, 2)
issue6 = Issue('Luisa@mail.com', 'No tengo me acuerdo mi contraseña', 1, 2)

db.session.add(issue1)
db.session.add(issue2)
db.session.add(issue3)
db.session.add(issue4)
db.session.add(issue5)
db.session.add(issue6)
db.session.commit()

#Creo y agrego las vistas de prueba


view_user = View("user","last_name","asc")
view_issue = View("issue","email","desc")
view_meeting_point = View("point","name","asc")

db.session.add(view_user)
db.session.add(view_issue)
db.session.add(view_meeting_point)
db.session.commit()



zonas_inundables_index = Permission("zonas_inundables_index")
zona_inundable_show = Permission("zona_inundable_show")
zona_inundable_destroy = Permission("zona_inundable_destroy")

usuario_index = Permission("usuario_index")

usuario_new = Permission("usuario_new")
usuario_update = Permission("usuario_update")
usuario_destroy = Permission("usuario_destroy")


#Configuracion_index permite a un admin y solo a un admin ingresar a la seccion de configuracin y a todas las acciones
configuracion_index = Permission("configuracion_index")

#Punto_encuentro_index: Permite acceder al index (listado) del modulo
punto_encuentro_index = Permission("puntos_encuentro_index")

#puntos_encuentro_update: Permite actualizar una zona inundable-
puntos_encuentro_update = Permission("puntos_encuentro_update")


#puntos_encuentro_destroy: Permite borrar una zona inundable
puntos_encuentro_destroy = Permission("puntos_encuentro_destroy")

#puntos_encuentro_new: Permite cargar una sona inundable:
puntos_encuentro_new = Permission("puntos_encuentro_new")





#Punto_encuentro_index: Permite acceder al index (listado) del modulo
denuncia_index = Permission("denuncia_index")

#puntos_encuentro_update: Permite actualizar una zona inundable-
denuncia_update = Permission("denuncia_update")


#puntos_encuentro_destroy: Permite borrar una zona inundable
denuncia_destroy = Permission("denuncia_destroy")

#puntos_encuentro_new: Permite cargar una sona inundable:
denuncia_new = Permission("denuncia_new")


denuncia_open = Permission("denuncia_open")
denuncia_resolved = Permission("denuncia_resolved")
denuncia_close = Permission("denuncia_close")
denuncia_add_monitoring = Permission("denuncia_add_monitoring")
denuncia_show = Permission("denuncia_show")


route_of_evacuation_index = Permission("route_of_evacuation_index")
route_of_evacuation_new = Permission("route_of_evacuation_new")
route_of_evacuation_update = Permission("route_of_evacuation_update")
route_of_evacuation_destroy = Permission("route_of_evacuation_destroy")


zonas_inundables_index = Permission("zonas_inundables_index")
zonas_inundables_update = Permission("zonas_inundables_update")
zonas_inundables_destroy = Permission("zonas_inundables_destroy")



#Agrego los permisos a la base de datos
db.session.add(zona_inundable_destroy)
db.session.add(zonas_inundables_index)
db.session.add(zona_inundable_show)

db.session.add(usuario_index)
db.session.add(configuracion_index)
db.session.add(puntos_encuentro_update)
db.session.add(punto_encuentro_index)
db.session.add(puntos_encuentro_destroy)
db.session.add(puntos_encuentro_new)

db.session.add(usuario_new)
db.session.add(usuario_update)
db.session.add(usuario_destroy)

db.session.add(denuncia_index)
db.session.add(denuncia_update)
db.session.add(denuncia_destroy)
db.session.add(denuncia_new)
db.session.add(denuncia_open)
db.session.add(denuncia_resolved)
db.session.add(denuncia_close)
db.session.add(denuncia_add_monitoring)
db.session.add(denuncia_show)

db.session.add(route_of_evacuation_destroy)
db.session.add(route_of_evacuation_new)
db.session.add(route_of_evacuation_update)
db.session.add(route_of_evacuation_index)

db.session.add(zonas_inundables_index)
db.session.add(zonas_inundables_update)
db.session.add(zonas_inundables_destroy)
db.session.commit()

#Creo roles

#Defino rol administrador
rol_administrador = Role("administrador")

#Relacion del rol administrador con sus permisos
rol_administrador.permission.append(zona_inundable_destroy)
rol_administrador.permission.append(zonas_inundables_index)
rol_administrador.permission.append(zona_inundable_show)

rol_administrador.permission.append(usuario_index)
rol_administrador.permission.append(configuracion_index)
rol_administrador.permission.append(punto_encuentro_index)
rol_administrador.permission.append(puntos_encuentro_new)
rol_administrador.permission.append(puntos_encuentro_destroy)
rol_administrador.permission.append(puntos_encuentro_update)

rol_administrador.permission.append(usuario_new)
rol_administrador.permission.append(usuario_update)
rol_administrador.permission.append(usuario_destroy)


rol_administrador.permission.append(denuncia_index)
rol_administrador.permission.append(denuncia_new)
rol_administrador.permission.append(denuncia_update)
rol_administrador.permission.append(denuncia_destroy)

rol_administrador.permission.append(denuncia_open)
rol_administrador.permission.append(denuncia_resolved)
rol_administrador.permission.append(denuncia_close)
rol_administrador.permission.append(denuncia_add_monitoring)
rol_administrador.permission.append(denuncia_show)


rol_administrador.permission.append(route_of_evacuation_destroy)
rol_administrador.permission.append(route_of_evacuation_update)
rol_administrador.permission.append(route_of_evacuation_new)
rol_administrador.permission.append(route_of_evacuation_index)

rol_administrador.permission.append(zonas_inundables_index)
rol_administrador.permission.append(zonas_inundables_update)
rol_administrador.permission.append(zonas_inundables_destroy)
db.session.commit()



# Defino el rol operador
rol_operador = Role("operador")

#Relacion del rol operador con sus permisos
rol_administrador.permission.append(zonas_inundables_index)
rol_administrador.permission.append(zona_inundable_show)

rol_operador.permission.append(usuario_index)
rol_operador.permission.append(usuario_update)
rol_operador.permission.append(configuracion_index)
rol_operador.permission.append(punto_encuentro_index)
rol_operador.permission.append(puntos_encuentro_new)
rol_operador.permission.append(puntos_encuentro_update)

rol_operador.permission.append(denuncia_index)
rol_operador.permission.append(denuncia_new)
rol_operador.permission.append(denuncia_update)

rol_operador.permission.append(denuncia_open)
rol_operador.permission.append(denuncia_resolved)
rol_operador.permission.append(denuncia_close)
rol_operador.permission.append(denuncia_add_monitoring)
rol_operador.permission.append(denuncia_show)

rol_operador.permission.append(route_of_evacuation_update)
rol_operador.permission.append(route_of_evacuation_new)
rol_operador.permission.append(route_of_evacuation_index)

rol_operador.permission.append(zonas_inundables_index)
rol_operador.permission.append(zonas_inundables_update)
db.session.commit()




#Creo usuario de prueba
usuario1 = User('Juan', 'Rodriguez','juancito@gmail.com', 'user1' , '21883')
usuario2 = User('Pedro', 'Rodriguez','ElRodri@unMail.com', 'rodri12' , 'libro23')
usuario3 = User('Pedro Luis', 'Juanpe','auris@unMail.com', 'ElJuanpe' , 'tomaco')
usuario4 = User('Jose Luis', 'sabili','sabilis@unMail.com', 'sabi23' , 'contra12')
usuario5 = User('Ignacio', 'linbilis','linbilis@unMail.com', 'limbis56' , 'tomaAAAc54')
usuario6 = User('Marcelo', 'umbrale','umb@unMail.com', 'usuario6' , 'Jose12')
usuario7 = User('Pedro', 'peresoso','peres@unMail.com', 'unPeresoso' , '454856458')

#Agrego los usuarios a la base
db.session.add(usuario7)
db.session.add(usuario6)
db.session.add(usuario5)
db.session.add(usuario4)
db.session.add(usuario3)
db.session.add(usuario2)
db.session.add(usuario1)
db.session.commit()


usuario_admin = User('cosme', 'Fulanito', 'admin', 'admin', '123123')
usuario_admin.role.append(rol_administrador)
db.session.commit()

#Creo los puntos de encuentro de prueba
puntos_encuentro1 = Point('punto2','46 entre 26 y 27', '2546 545', '2332 323', '2213645852','point1@unEmail.com', 'Publicado')
puntos_encuentro2 = Point('punto13','46 entre 55 y 56', '122 545','232 2323', '2156485745','point1@unEmail.com', 'Despublicado')
puntos_encuentro3 = Point('punto14','524 entre 12 y 13', '32 545','14533', '4564579656','point2@unEmail.com', 'Publicado')
puntos_encuentro4 = Point('punto15','centenario entre 26 y 27', '23 54565','549165', '656686','point4@unEmail.com', 'Publicado')
puntos_encuentro5 = Point('punto133','belgrano entre 26 y 27', '65 545','125456', '2213654215','point5@unEmail.com', 'Publicado')
puntos_encuentro6 = Point('punto3','66 entre 26 y 27', '253246 65', '3254698','5454455454','poin61@unEmail.com', 'Despublicado')
puntos_encuentro7 = Point('punto4','55 entre 11 y 12', '158 545','4694597', '5454546525','point7@unEmail.com', 'Publicado')
puntos_encuentro8 = Point('punto5','14 esquina 22', '2546 65', '45589655','4546838547','point10@unEmail.com', 'Despublicado')
puntos_encuentro9 = Point('punto6','100 entre 10 y 11', '2325 32','6584352', '54668975678','point11@unEmail.com', 'Publicado')
puntos_encuentro10 = Point('punto7','calle falsa 123', '256546 87','5698234', '5648684883','point21@unEmail.com', 'Despublicado')
puntos_encuentro11 = Point('punto8','Belgrano 1800', '568 1', '154265', '456469838','point13@unEmail.com', 'Publicado')
puntos_encuentro12 = Point('punto9','55 entre 12 y 13', '34 65','1584562', '4457866546','point13@unEmail.com', 'Despublicado')
puntos_encuentro13 = Point('punto10','44 esquina 10', '875 5415', '20651561','569454768','point12@unEmail.com', 'Publicado')

#Agrego los puntos de encuentro a la base de datos
db.session.add(puntos_encuentro1)
db.session.add(puntos_encuentro2)
db.session.add(puntos_encuentro3)
db.session.add(puntos_encuentro4)
db.session.add(puntos_encuentro5)
db.session.add(puntos_encuentro6)
db.session.add(puntos_encuentro7)
db.session.add(puntos_encuentro8)
db.session.add(puntos_encuentro9)
db.session.add(puntos_encuentro10)
db.session.add(puntos_encuentro11)
db.session.add(puntos_encuentro12)
db.session.add(puntos_encuentro13)
db.session.commit()


#Agrego los report de prueba

ReportDAO.create_report('Alcantarilla tapada',2, 'La alcantarilla esta tapada no sabemos porque ', 45454, 555555,  'Juan', 'De los palotes', 2213641585, 'juan@email.com',)
ReportDAO.create_report('Alcantarilla Sucia',1, 'La alcantarilla esta SUCIA no sabemos porque ', 11111, 22222, 'Pedro', 'Primo', 22236548, 'Pedro@email.com' )
ReportDAO.create_report('Basural',1, 'Hay un basural en la puerta de mi casa ', 222222, 111111, 'Santiago', 'De los palotes', 236568985, 'Santiago@email.com' )
ReportDAO.create_report('Sin desagotar',2, 'No desagota la alcantarilla de la puerta de mi casa', 1112311, 2332233232, 'Pedrito', 'Clavito', 222365263, 'Pedrito@email.com',1)

ReportDAO.create_report('Alcantarillas rotas',2, 'Las alcantarillas de la cuadra estas todas rotas y se mete la basura ', 4522454, 52255555,  'Nacho', 'Marti', 222123232323, 'nacho@email.com',2)
ReportDAO.create_report('Inundacion de caño',1, 'Hay una inundacion de un caño en la puerta de mi casa y se inunda todo ', 2222, 1111, 'Camila', 'Pini', 22222222, 'Cami@email.com' )
ReportDAO.create_report('Cloaca se inunda ',2, 'Hay una cloaca tapada y se inunda mi casa', 233232, 232323, 'Juanita', 'Clavito', 2232323, 'Juanita@email.com',1)


# ruta1 = Route_of_evacuationDAO.create_route('Ruta1',True,'Es una ruta larga')
# ruta2 = Route_of_evacuationDAO.create_route('Ruta3',True,'Es una ruta de salida')


# db.session.add(ruta1)
# db.session.add(ruta2)


# coordenada1 = Coordinate(-34.55551212, -58.12323912)
# coordenada2 = Coordinate(-36.12332123, -55.21312313)
# coordenada3 = Coordinate(-37.12332123, -56.21312313)
# coordenada4 = Coordinate(-38.12332123, -57.21312313)
# coordenada5 = Coordinate(-39.12332123, -58.21312313)
# coordenada6 = Coordinate(-40.12332123, -60.21312313)
# coordenada7 = Coordinate(-41.12332123, -61.21312313)
# coordenada8 = Coordinate(-42.12332123, -62.21312313)

# db.session.add(coordenada1)
# db.session.add(coordenada2)
# db.session.add(coordenada3)
# db.session.add(coordenada4)
# db.session.add(coordenada5)
# db.session.add(coordenada6)
# db.session.add(coordenada7)
# db.session.add(coordenada8)

# ruta1.coordinates.append(coordenada1)
# ruta1.coordinates.append(coordenada2)
# ruta1.coordinates.append(coordenada3)
# ruta1.coordinates.append(coordenada4)
# ruta1.coordinates.append(coordenada5)

# ruta2.coordinates.append(coordenada6)
# ruta2.coordinates.append(coordenada7)
# ruta2.coordinates.append(coordenada8)
