from django import forms

g=[['Male','Male'],['Female','Female']]
c=[['PYTHON','PYTHON'],('Django','Django'),['SQL','SQL']]
class NameForm(forms.Form):
    Sname=forms.CharField()
    Sage=forms.IntegerField()
    password=forms.CharField(widget=forms.PasswordInput)
    address=forms.CharField(widget=forms.Textarea(attrs={'cols':12,'rows':2}))
    #gender=forms.ChoiceField(choices=g)
    gender=forms.ChoiceField(choices=g,widget=forms.RadioSelect)
    #course=forms.MultipleChoiceField(choices=c)
    course=forms.MultipleChoiceField(choices=c,widget=forms.CheckboxSelectMultiple)
  