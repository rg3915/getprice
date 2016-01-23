from django.conf.urls import url
from django.contrib import admin
import myproject.core.views as v

urlpatterns = [
    url(r'^$', v.home, name='home'),
    url(r'^products/$', v.ProductList.as_view(), name='product_list'),
    url(r'^quotations/$', v.quotation_list, name='quotation_list'),
    url(r'^quotations/2/$', v.quotation_list2, name='quotation_list2'),
    # url(r'^quotations/pivottable/$', v.pivottable, name='pivottable'),
    url(r'^quotations/min/$', v.quotation_list_min, name='quotation_list_min'),

    url(r'^quotations/add/$', v.QuotationCreate.as_view(), name='quotation_add'),
    url(r'^admin/', admin.site.urls),
]
