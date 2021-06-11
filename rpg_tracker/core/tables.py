import django_tables2 as tables

class BaseTable(tables.Table):
    
    class Meta:
        attrs = {
            "class" : "table table-hover",
            "thead" : {
                "class" : "thead-dark"
            }
        }
        row_attrs = {
            "style": "transform: rotate(0);"
        }