# coding:utf-8
__author__ = 'fang'
__date__ = '2017/6/5 0005 15:08'

import xadmin
from xadmin.views import BaseAdminPlugin, ListAdminView
from django.template import loader


#excel 导入
class ListImportExcelPlugin(BaseAdminPlugin):
    import_excel = False

    def init_request(self, *args, **kwargs):
        return bool(self.import_excel)

    def block_top_toolbar(self, context, nodes):
        nodes.append(loader.render_to_string('xadmin/excel/model_list.top_toolbar.import.html', context_instance=context))


xadmin.site.register_plugin(ListImportExcelPlugin, ListAdminView)