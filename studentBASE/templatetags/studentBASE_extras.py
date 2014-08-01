from django import template
import datetime

register = template.Library()


#@register.inclusion_tag('studentBASE/edit_link.html')
@register.simple_tag
def edit(obj):
	class_name = (obj.__class__).__qualname__
	way = '/admin/studentBASE/' + class_name.lower() + '/' + obj.id.__str__() + '/'
	return way

@register.filter(name='addcss')
def addcss(field, css):
   return field.as_widget(attrs={"class":css})