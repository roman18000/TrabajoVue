from app.models.configuration import Configuration


class FormConfigValidator():
    
    @staticmethod
    def color_is_valid(bg_color):
        return ( bg_color in Configuration.get_valid_colors() )
        
    @staticmethod
    def validate_issue_values(column, type):
        if( (column in Configuration.get_valid_issues_column()) and (type in Configuration.get_valid_sort_types()) ):
            return True
        return False

    @staticmethod
    def validate_point_values(column, type):
        if( (column in Configuration.get_valid_point_columns()) and (type in Configuration.get_valid_sort_types()) ):
            return True
        return False