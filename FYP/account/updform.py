from django import forms

class upd_form(forms.Form):
    name = forms.CharField(label='Name',
                           max_length=100,
                           widget=forms.TextInput(attrs={'class': 'form-control'}))
    challanid = forms.CharField(label='Challan ID',
                           max_length=100,
                           widget=forms.TextInput(attrs={'class': 'form-control'}))
    citizenid = forms.CharField(label='Citizen ID',
                           max_length=100,
                           widget=forms.TextInput(attrs={'class': 'form-control'}))
    challanamount = forms.CharField(label='Challan Amount',
                           max_length=100,
                           widget=forms.TextInput(attrs={'class': 'form-control'}))
    cnic = forms.CharField(label='CNIC',
                           max_length=100,
                           widget=forms.TextInput(attrs={'class': 'form-control'}))
    address = forms.CharField(label='Address',
                           max_length=100,
                           widget=forms.TextInput(attrs={'class': 'form-control'}))
    mobile = forms.CharField(label='Mobile',
                           max_length=100,
                           widget=forms.TextInput(attrs={'class': 'form-control'}))
    duedate = forms.CharField(label='Due Date',
                           max_length=100,
                           widget=forms.TextInput(attrs={'class': 'form-control'}))
    issuedate = forms.CharField(label='Issue Date',
                           max_length=100,
                           widget=forms.TextInput(attrs={'class': 'form-control'}))
    liceneseno = forms.CharField(label='License No',
                           max_length=100,
                           widget=forms.TextInput(attrs={'class': 'form-control'}))
    chasis = forms.CharField(label='Chasis',
                           max_length=100,
                           widget=forms.TextInput(attrs={'class': 'form-control'}))
    color = forms.CharField(label='Color',
                           max_length=100,
                           widget=forms.TextInput(attrs={'class': 'form-control'}))
    make = forms.CharField(label='Make',
                           max_length=100,
                           widget=forms.TextInput(attrs={'class': 'form-control'}))
    paidchallan = forms.CharField(label='Paid Challan',
                           max_length=100,
                           widget=forms.TextInput(attrs={'class': 'form-control'}))
    unpaidchallan = forms.CharField(label='Unpaid Challan',
                           max_length=100,
                           widget=forms.TextInput(attrs={'class': 'form-control'}))
    penaltypoint = forms.CharField(label='Penalty Point',
                           max_length=100,
                           widget=forms.TextInput(attrs={'class': 'form-control'}))
            
