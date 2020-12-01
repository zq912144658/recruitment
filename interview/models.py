from django.db import models

# Create your models here.
DEGREE_TYPE = ()
class Candidate(models.Model):
	#基础信息
	userid = models.IntegerField(unique=True,blank=True,verbose_name=u'应聘者ID')
	username = models.CharField(max_length=135,verbose_name=u'姓名')
	city = mels.CharField(max_length=135,verbose_name=u'城市')
	phone = models.CharField(max_length=135,verbose_name=u'手机号码')
	email = models.EmailField(max_length=135,blank=135,verbose_name=u'邮箱')
	apply_position = models.CharField(max_length=135,blank=True,verbose_name=u'应聘职位')
	born_address = models.CharField(max_length=135,blank=True,verbose_name=u'生源地')
	gender = models.CharField(max_length=135,blank=True,verbose_name=u'性别')
	candidate = models.CharField(max_length=135,blank=True,verbose_name=u'候选人信息备注')
	
	#学校与学历信息
	bachelor_school = models.CharField(max_length=135,blank=True,verbose_name=u'本科学校')
	master_school = models.CharField(max_length=135,blank=True,verbose_name=u'研究生学校')
	doctor_school = models.CharField(max_length=135,blank=True,verbose_name=u'博士生学校')
	major = models.CharField(max_length=135,blank=True,verbose_name=u'专业')
	degree = models.CharField(max_length=135,choices=DEGREE_TYPE,blank=True,verbose_name=u'学历')
	
	#综合能力测评成绩,笔试测评成绩
	_score_of_general_ability = models.DecimalField()
	paper_score = models.DecimalField()
	#第一轮面试记录
	first_score = models.DecimalField()
	first_learning_ability = models.DecimalField()
	first_professional_competency = models.DecimalField()
	
	first_advantage = models.TextField()
	first_disadvantage = models.TextField()
	first_remark = models.CharField()
	
	#第二轮面试记录
	cond_score = models.CharField()
	second_learing_adility = models.CharField()
	
	second_professional_conptetency = models.DecimalField()
	second_pursue_of_excellence = models.DecimalField()
	second_communication_abillty = models.DecimalField()
	second_pressure_score = models.DecimalField()
	second_advantage = models.DecimalField()
	second_disadvantage = models.TextField()
	second_result = models.CharField()
	second_recommend_position = models.CharField()
	second_interviewer = models.CharField()
	second_remark = models.CharField()
	
	#HR终面
	hr_score = models.CharField()
	hr_responsibility = models.CharField()
	hr_communication_ability = models.CharField()
	
	hr_logic_ability = models.CharField()
	hr_potential = models.CharField()
	hr_stability = models.CharField()
	hr_advantage = models.TextField()
	hr_disadvantage = models.TextField()
	hr_result = models.CharField()
	hr_interviewer = models.CharField()
	hr_remark = models.CharField()
	
	creator = models.CharField()
	created_date = models.DateTimeField()
	modified_date = models.DateTimeField()
	last_editor = models.CharField()
	
	class Meta:
		ab_table = u''
		verbose_name = u''
		verbose_name_plural = u''
	
	def __unicode__(self):
		return self.username
	
	def __str__(self):
		return self.username