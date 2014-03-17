from django import forms

from surveys.models import TrueFalseAnswer, DropDownAnswer, \
    OrderingAnswer, ExplanationAnswer, RadioButtonAnswer, \
    MultipleChoiceAnswer

class SurveyForm(forms.Form):
    question_count = forms.CharField(widget=forms.HiddenInput(), required=False)
    def __init__(self, *args, **kwargs):
        questions = kwargs.pop('questions', [])

        super(SurveyForm, self).__init__(*args, **kwargs)
        self.fields['question_count'].initial = questions.count()

        for question in questions:
            if hasattr(question, 'dropdownquestion'):
                self.fields['question_{index}'.format(index=question.id)] = \
                    DropDownField(question=question.dropdownquestion)
            elif hasattr(question, 'truefalsequestion'):
                self.fields['question_{index}'.format(index=question.id)] = \
                    TrueFalseField(question=question.truefalsequestion)
            elif hasattr(question, 'orderingquestion'):
                self.fields['question_{index}'.format(index=question.id)] = \
                    OrderingField(question=question.orderingquestion)
            elif hasattr(question, 'explanationquestion'):
                self.fields['question_{index}'.format(index=question.id)] = \
                    ExplanationField(question=question.explanationquestion)
            elif hasattr(question, 'radiobuttonquestion'):
                self.fields['question_{index}'.format(index=question.id)] = \
                    RadioButtonField(question=question.radiobuttonquestion)
            elif hasattr(question, 'multiplechoicequestion'):
                self.fields['question_{index}'.format(index=question.id)] = \
                    MultipleChoiceField(question=question.multiplechoicequestion)

class TrueFalseField(forms.BooleanField):
    def __init__(self, *args, **kwargs):
        question = kwargs.pop('question')

        super(TrueFalseField, self).__init__(*args, **kwargs)

        self.label = question.question_text
        self.required = False

class ExplanationField(forms.CharField):
    def __init__(self, *args, **kwargs):
        question = kwargs.pop('question')

        self.widget = forms.Textarea()
        super(ExplanationField, self).__init__(*args, **kwargs)

        self.label = question.question_text
        self.required = False

class DropDownField(forms.ChoiceField):
    def __init__(self, *args, **kwargs):
        question = kwargs.pop('question')

        super(DropDownField, self).__init__(*args, **kwargs)

        raw_choices = question.dropdownchoice_set.all()
        choices = []
        for raw_choice in raw_choices:
            choices.append((raw_choice.id, raw_choice.text))
        self.required = False
        self.label = question.question_text
        self.choices = choices

class OrderingWidget(forms.MultiWidget):
    def __init__(self, *args, **kwargs):
        self.question = kwargs.pop('question')

        widgets = []
        raw_choices = self.question.orderingchoice_set.order_by('id').all()
        for raw_choice in raw_choices:
            widgets.append(forms.TextInput())
        super(OrderingWidget, self).__init__(widgets, *args, **kwargs)

    def decompress(self, value):
        if value:
            return value
        return [None for i, widget in enumerate(self.widgets)]

    def format_output(self, rendered_widgets):
        raw_choices = self.question.orderingchoice_set.order_by('id').all()
        output = '<br>'

        for i in range(len(rendered_widgets)):
            output = "<span class='ordering_choice'>%s %s %s</span><br>" % (output, raw_choices[i].text, rendered_widgets[i])
        return output

#    def value_from_datadict(self, data, files, names):
#        valuelist = [
#            widget,value_from_datadict(data, files, name + '_%s' % i)
#            for i, widget in enumerate(self.widgets)
#        ]

class OrderingField(forms.MultiValueField):
    def __init__(self, *args, **kwargs):
        question = kwargs.pop('question')

        list_fields = []
        raw_choices = question.orderingchoice_set.order_by('id').all()
        for raw_choice in raw_choices:
            list_fields.append(forms.IntegerField(label=raw_choice.text))

        super(OrderingField, self).__init__(*args, **kwargs)

        self.label = question.question_text
        self.require_all_fields = False
        self.fields = list_fields
        self.widget = OrderingWidget(question=question)

    def compress(self, data_list):
        return data_list

class RadioButtonField(forms.ChoiceField):
    def __init__(self, *args, **kwargs):
        question = kwargs.pop('question')

        super(RadioButtonField, self).__init__(*args, **kwargs)

        self.widget = forms.RadioSelect()
        raw_choices = question.radiobuttonchoice_set.all()
        choices = []
        for raw_choice in raw_choices:
            choices.append((raw_choice.id, raw_choice.text))
        self.required = False
        self.label = question.question_text
        self.choices = choices

class MultipleChoiceField(forms.MultipleChoiceField):
    def __init__(self, *args, **kwargs):
        question = kwargs.pop('question')

        super(MultipleChoiceField, self).__init__(*args, **kwargs)

        raw_choices = question.multiplechoicechoice_set.all()
        choices = []
        for raw_choice in raw_choices:
            choices.append((raw_choice.id, raw_choice.text))
        self.required = False
        self.label = question.question_text
        self.choices = choices
