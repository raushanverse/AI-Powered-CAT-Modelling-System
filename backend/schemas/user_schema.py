from marshmallow import Schema, fields, validate


class UserSchema(Schema):
    full_name = fields.Str(
        required=True,
        validate=validate.Length(min=3, max=100)
    )

    employee_id = fields.Str(
        required=True,
        validate=validate.Length(min=3, max=20)
    )

    email = fields.Email(required=True)

    phone = fields.Str(
        required=True,
        validate=validate.Length(min=10, max=15)
    )

    password = fields.Str(
        required=True,
        validate=validate.Length(min=8)
    )

    role = fields.Str(
        required=True,
        validate=validate.OneOf([
            "Admin",
            "CAT Analyst",
            "Underwriter",
            "Claims Officer"
        ])
    )

    office_location = fields.Str(
        required=True,
        validate=validate.Length(min=2, max=100)
    )