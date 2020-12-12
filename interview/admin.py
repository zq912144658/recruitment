from django.contrib import admin
from interview.models import Candidate
# Register your models here.

# 候选人管理类
class CandidateAdmin(admin.ModelAdmin):
    exclude = ('creator','created_date','modified_date')
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

