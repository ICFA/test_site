from django import forms
from site_app.models import Cpu_Utilization

class CpuForm(forms.ModelForm):
    class Meta:
        model = Cpu_Utilization
        fields = ["curr_util"]