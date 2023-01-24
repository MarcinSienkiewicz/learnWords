from django import forms

class SelectionForm(forms.Form):
    level_options = (
        ('A1', 'A1'), ('A2', 'A2'),
        ('B1', 'B1'), ('B2', 'B2'),
        ('C1', 'C1'), ('C2', 'C2'),
        ('przysłowie', 'przysłowie'),
        ('wymieszane', 'wymieszane'),
    )
    level_choices = forms.ChoiceField(choices= level_options, initial='B2',
        label='Choose words type')
    tries = forms.IntegerField(label='How many:', min_value=1, max_value=10, initial=5)