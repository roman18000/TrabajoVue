from app.models.permission import Role, Permission
class RoleDAO():
    """ Esta clase se encarga de toda las consultas a la base de datos
                correspondiente a los roles de los usuarios"""
    @staticmethod
    def _inicializate_permission_with(functions):
        """Recibe una lista la cual contiene 2 lista, la 1ra con los permisos
                    para las funciones, y la 2da con la funciones permitidas"""
        permisos = []
        if (not functions[0] == []) and  (not functions[1] == []):
            values = functions[0]
            dar_permiso = functions[1]
            admin = functions[2]
            for type in values:
                for dar in dar_permiso:
                    perm = f"{dar}_{type}"
                    permisos.append(Permission(perm))
        if admin:
            #Se agrega permisos especiales extras del admin
            permisos.append(Permission("configuracion_index"))
            permisos.append(Permission("denuncia_open"))
            permisos.append(Permission("denuncia_resolved"))
            permisos.append(Permission("denuncia_close"))
            permisos.append(Permission("denuncia_add_monitoring"))
            permisos.append(Permission("denuncia_show"))
        return permisos

    @classmethod
    def inicializate_role_with(cls,role,permisos):
        """Recibe un rol y una lista con los funciones sobre que asignar y
                    devuelve al rol con sus permisos asignados"""
        values = ["index","new","update","show"]
        if role == "administrador":
            values.append("destroy")
            functions = [values,permisos,True]
        else:
            functions = [values,permisos,False]
        functions_update = cls._inicializate_permission_with(functions)
        role_update = Role(role)
        for f in functions_update:
            role_update.permission.append(f)
        return role_update

    def recover_role(name_role):
        return Role.query.filter_by(name = name_role).first()

    @staticmethod
    #Devuelve booleano indicando si ya tiene rol asignado
    def has_rol(user,name_role):
        for role in user.role:
            if role.name == name_role:
                return True
        return False

    @staticmethod
    def recover_roles_of(user):
        roles_name = []
        for role in user.role:
            roles_name.append(role.name)
        return roles_name
