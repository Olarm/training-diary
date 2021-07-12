from django import forms

from crispy_forms.layout import Layout, ButtonHolder, Submit, Div, Field, Row, Column
from crispy_forms.bootstrap import InlineCheckboxes, PrependedText
from crispy_forms.helper import FormHelper

from .models import *


class WorkoutForm(forms.ModelForm):
    helper = FormHelper()

    helper.layout = Layout(
        Row(
            Div(
                "name",
                "type",
                css_class="col",
            ),
        )
    )

    class Meta:
        model = Workout
        fields = [
            "name",
            "type",
        ]


class ExcerciseDetailForm(forms.ModelForm):
    helper = FormHelper()

    helper.layout = Layout(
        Row(
            Div(
                "excercise",
                "magnitude",
                "repetitions",
                css_class="col",
            ),
        )
    )

    class Meta:
        model = ExcerciseDetails
        fields = [
            "excercise",
            "magnitude",
            "repetitions",
        ]


class ExcerciseForm(forms.ModelForm):
    helper = FormHelper()

    helper.layout = Layout(
        Row(
            Div(
                "name",
                css_class="col",
            ),
        )
    )

    helper.add_input(Submit('submit', 'Submit', css_class='btn-primary'))

    class Meta:
        model = Workout
        fields = [
            "name",
        ]
