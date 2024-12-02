from wtforms import Form, SelectField, StringField, DateTimeField, TextAreaField, SubmitField, validators, ValidationError
import datetime

class TaskForm(Form):
    name = StringField('Name', [validators.length(min=4, max=80), validators.DataRequired()])
    description = TextAreaField('Description',[validators.Optional()])
    due_date = DateTimeField('Due Date',[validators.Optional()], format='%Y-%m-%d %H:%M:%S')
    category_id = SelectField('Category', [validators.DataRequired()], choices=[], coerce=int)
    submit = SubmitField('Save')

    def validate_due_date(form, field):
        if field.data < datetime.datetime.now():
            raise ValidationError('Datetime can not be previous to rigth now')
 