from django.contrib import admin
from surveys.models import Survey, Question, TrueFalseQuestion, \
    DropDownQuestion, DropDownChoice, OrderingQuestion, OrderingChoice, \
    ExplanationQuestion, RadioButtonQuestion, RadioButtonChoice, \
    MultipleChoiceQuestion, MultipleChoiceChoice

class QuestionInline(admin.TabularInline):
    model = Question
    def has_add_permission(self, request):
        return False

class SurveyAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]

class TrueFalseQuestionAdmin(admin.ModelAdmin):
    pass

class DropDownInline(admin.TabularInline):
    model = DropDownChoice
    extra = 3

class DropDownQuestionAdmin(admin.ModelAdmin):
    inlines = [DropDownInline]

class OrderingInline(admin.TabularInline):
    model = OrderingChoice
    extra = 3

class OrderingQuestionAdmin(admin.ModelAdmin):
    inlines = [OrderingInline]

class ExplanationQuestionAdmin(admin.ModelAdmin):
    pass

class RadioButtonInline(admin.TabularInline):
    model = RadioButtonChoice
    extra = 3

class RadioButtonQuestionAdmin(admin.ModelAdmin):
    inlines = [RadioButtonInline]

class MultipleChoiceInline(admin.TabularInline):
    model = MultipleChoiceChoice
    extra = 3

class MultipleChoiceQuestionAdmin(admin.ModelAdmin):
    inlines = [MultipleChoiceInline]

admin.site.register(Survey, SurveyAdmin)
admin.site.register(TrueFalseQuestion, TrueFalseQuestionAdmin)
admin.site.register(DropDownQuestion, DropDownQuestionAdmin)
admin.site.register(OrderingQuestion, OrderingQuestionAdmin)
admin.site.register(ExplanationQuestion, ExplanationQuestionAdmin)
admin.site.register(RadioButtonQuestion, RadioButtonQuestionAdmin)
admin.site.register(MultipleChoiceQuestion, MultipleChoiceQuestionAdmin)
#class ChoiceInline(admin.TabularInline):
#    model = Choice
#    extra = 3
#
#class QuestionAdmin(admin.ModelAdmin):
#    fieldsets = [
#        (None,               {'fields':['question_text']}),
#        ('Date information', {'fields':['pub_date'],
#                              'classes':['collapse']}),
#    ]
#    inlines = [ChoiceInline]
#    list_display = ('question_text', 'pub_date', 'was_published_recently')
#    list_filter = ['pub_date']
#    search_fields = ['question_text']
#
#admin.site.register(Question, QuestionAdmin)
#admin.site.register(Choice)
