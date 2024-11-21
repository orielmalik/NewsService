from marshmallow import Schema, fields

def create_dynamic_schema(content_dict):
    # יצירת מחלקת Schema דינמית
    class DynamicSchema(Schema):
        pass

    # הוספת שדות לכל מפתח במילון כ-Field
    for key, value in content_dict.items():
        field_type = fields.Str()  # או כל סוג שדה אחר שתצטרך בהתאם לנתונים
        setattr(DynamicSchema, key, field_type)

    print(DynamicSchema.__dict__)
    return DynamicSchema

def dy(content_dict):
    class DynamicContentSchema(Schema):
        for key, value in content_dict.items():
            locals()[key] = fields.String()
    return DynamicContentSchema