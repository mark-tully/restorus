from django import forms


class SearchForm(forms.Form):
    q = forms.CharField(
        label='Type your query...',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Search...'})
    )