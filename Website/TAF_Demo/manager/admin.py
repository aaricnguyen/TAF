from django.contrib import admin
from django.contrib.admin import AdminSite
from . import models
# Register your models here.

class TestSuiteAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'date_create', 'author', 'testcase_names']
    list_display_links = ['name', 'description', 'date_create', 'author']
    date_hierarchy = 'date_create'
    ordering = ('date_create',)
    filter_horizontal = ['test_case']
    list_per_page = 10
    list_filter = ['date_create', 'author']
    search_fields = ['name', 'description']

    def testcase_names(self, obj):
        return ", ".join([tc.name for tc in obj.test_case.all()])


class TestCaseAdmin(admin.ModelAdmin):
    list_display = ['name','description','date_create', 'author', 'steps',]
    list_display_links = ['name', 'description', 'date_create', 'author', 'steps']
    date_hierarchy = 'date_create'
    ordering = ('date_create',)
    list_per_page = 10


class TestLibAdmin(admin.ModelAdmin):
    list_display = ['name', 'path', 'default_param']
    list_display_links = ['name', 'path', 'default_param']
    list_per_page = 15
    search_fields = ['name']


class TestBatchAdmin(admin.ModelAdmin):
    list_display = ['id' , 'name', 'start_time', 'end_time', 'result']
    list_display_links = None   
    list_per_page = 15
    search_fields = ['name']

    def has_add_permission(self, request, obj=None):
        return False
    
    def has_change_permission(self, request, obj=None):
        return False
    

class TestExecutionAdmin(admin.ModelAdmin):
    list_display = ['test_batch_id', 'tc_name','start_time', 'end_time', 'result']
    list_display_links = None    
    list_per_page = 15
    list_filter = ['result']

    def has_change_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False

    def tc_name(self, instance):
        return instance.tc_name.name
    
    def test_batch_id(self, instance):
        return instance.tb.id


admin.site.register(models.TestSuite, TestSuiteAdmin)
admin.site.register(models.TestCase, TestCaseAdmin)
admin.site.register(models.TestLib, TestLibAdmin)
admin.site.register(models.TestBatch, TestBatchAdmin)
admin.site.register(models.TestExecution, TestExecutionAdmin)


admin.site.site_header = "TAF Administration"
admin.site.site_title = "TAF Administration"
admin.site.index_title = "TAF Administration"
admin.site.site_url = 'https://www.terralogic.com/'
admin.site.index_title = ''
admin.empty_value_display = '**Empty**'