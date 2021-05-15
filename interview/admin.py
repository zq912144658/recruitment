from django.contrib import admin
from interview.models import Candidate
# Register your models here.
from datetime import datetime
from django.http import HttpResponse
import logging
import csv
logger = logging.getLogger(__name__)
exportable_fields = ('username','city','phone','bachelor_school','master_school','degree','first_result',
                     'first_interviewer','second_result','second_interviewer','hr_result','hr_score','hr_remark','hr_interviewer')
def export_model_as_csv(modeladmin,request,queryset):
    response = HttpResponse(content_type='text/csv')
    field_list = exportable_fields
    response['Content-Disposition'] = 'attachment;filename=recruitment-candidates-list-%s.csv' % (
        datetime.now().strftime('%Y-%m-%d-%H-%M-%S'),
    )
    ### 写入表头
    writer = csv.writer(response)
    writer.writerow(
        [queryset.model._meta.get_field(f).verbose_name.title() for f in field_list]
    )
    for obj in queryset:
        ### 单行的记录 （各个字段的值），写入到csv文件
        csv_line_values = []
        for field in field_list:
            field_object = queryset.model._meta.get_field(field)
            field_values = field_object.value_from_object(obj)
            csv_line_values.append(field_values)
        writer.writerow(csv_line_values)
        logger.info("%s exported %s candidate records"% (request.user,len(queryset)))
    return response
export_model_as_csv.short_description = u'导出为csv文件'

# 候选人管理类
class CandidateAdmin(admin.ModelAdmin):
    exclude = ('creator','created_date','modified_date')
    actions = [export_model_as_csv,]
    list_display = ("username","city","bachelor_school","first_score","first_result","first_interviewer",
                    "second_result","second_interviewer","hr_score","hr_result","last_editor")
    # 筛选条件
    list_filter = ('city','first_result','second_result','hr_result','first_interviewer','second_interviewer','hr_interviewer')
    # 查询条件
    search_fields = ('username','phone','email','bachelor_school')

    fieldsets = (
        (None,{'fields':("userid", ("username", "city", "phone"), ("email", "apply_position", "born_address"), ("gender", "candidate_remark"),("bachelor_school","master_school", "doctor_school"),("major","degree"),("test_score_of_general_ability","paper_score"), "last_editor")}),
        ('第一轮面试记录',{'fields':(("first_score", "first_learning_ability", "first_professional_competency"), "first_advantage", "first_disadvantage", "first_result", "first_recommend_position", "first_interviewer", "first_remark")}),
        ('第二轮面试记录',{'fields':(("second_score", "second_learing_adility", "second_professional_conptetency"),("second_pursue_of_excellence", "second_communication_abillty", "second_pressure_score"), "second_advantage", "second_disadvantage", "second_result", "second_recommend_position", "second_interviewer", "second_remark")}),
        ('hr复试记录',{'fields':("hr_score",("hr_responsibility", "hr_communication_ability", "hr_logic_ability"),("hr_potential", "hr_stability"),"hr_advantage", "hr_disadvantage", "hr_result", "hr_interviewer", "hr_remark")})
    )
admin.site.register(Candidate,CandidateAdmin)

