from app.dao.configuration import ConfigurationDAO


def format_background(background='Gris'):
    values = { "Gris" : "bg-light",
               "Celeste" : "bg-info",
               "Amarillo" : "bg-warning"
       }
    dao = ConfigurationDAO()
    
    return values[dao.background]