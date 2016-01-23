from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.db.models import F, Min, FloatField
from django.views.generic import CreateView, ListView
from myproject.core.models import Product, Quotation, Store, Exam


def home(request):
    return render(request, 'index.html')


class ProductList(ListView):
    template_name = 'core/product_list.html'
    model = Product
    context_object_name = 'products'


def soma_tuplas(a, b):
    return (a[0] + b[0], a[1] + b[1], a[2] + b[2], a[3], a[4])


def quotation_list(request):
    stores = Store.objects.all()
    products = Product.objects.all()
    # indice
    index_store = {store.id: index for index, store in enumerate(stores)}
    index_product = {product.id: index for index,
                     product in enumerate(products)}
    # dados para o template
    cabecalho = ["Lojas"] + [store.store for store in stores]
    linhas = [([product.product] + [None for store in stores] + [(0, 0, 0, None, product.product)])
              for product in products] + [["Subtotal"] + [(0, 0, 0, store.store, None) for store in stores]
                                          + [(0, 0, 0, None, None)]]

    for pev in Quotation.objects.all():
        total = pev.price * pev.quantity

        i0 = index_product[pev.product_id]
        i1 = index_store[pev.store_id] + 1
        valor = (pev.price, pev.quantity, total, pev.store, pev.product)

        linhas[i0][i1] = valor

        # Subtotal da linha
        linhas[i0][len(stores) + 1] = soma_tuplas(
            linhas[i0][len(stores) + 1], valor)

        # Subtotal da coluna
        linhas[len(products)][i1] = soma_tuplas(
            linhas[len(products)][i1], valor)

        # Total da tabela
        linhas[len(products)][len(stores) + 1] = soma_tuplas(
            linhas[len(products)][len(stores) + 1], valor)

    # retorna o menor preço de cada produto
    # a quantidade, total e loja também estão nesta lista
    mais_barato = []
    for linha in linhas:
        mais_barato.append(min(linha[1:]))

    # print(linhas[i0][len(stores) + 1])

    # destaca os menores preços no template
    mb = 0
    if request.GET.get('mais_barato', False):
        mb = 1

    # mostra somente os menores preços
    smb = 0
    if request.GET.get('somente_mais_barato', False):
        smb = 1

    linhas_mais_barato = zip(linhas, mais_barato)

    # mostra os produtos mais baratos, a quantidade e o total
    bqt = 0
    if request.GET.get('quantidade_e_total', False):
        # linhas_mais_barato = sorted(linhas_mais_barato,
        # key=lambda store: str(store[1][3]))  # sort by store
        bqt = 1

    context = {
        'cabecalho': cabecalho,
        'linhas_mais_barato': linhas_mais_barato,
        'mb': mb,
        'smb': smb,
        'bqt': bqt,
    }
    return render(request, 'core/quotation_list.html', context)


def quotation_list_min(request):
    pega_total = F('price') * F('quantity')
    pega_total.output_field = FloatField()

    qs = Quotation.objects.all().\
        annotate(menor=Min('product__quotation__price'), total=pega_total).\
        filter(price=F('menor')).\
        order_by('store__store').\
        values('product__product', 'price',
               'quantity', 'total', 'store__store')

    context = {'linhas': list(qs)}

    subtotal = 0
    total = 0
    ultima_loja = None

    linhas = []
    for linha in qs:
        if ultima_loja is not None and ultima_loja != linha['store__store']:
            linhas.append({'subtotal': subtotal})
            subtotal = 0
        linhas.append(linha)
        ultima_loja = linha['store__store']
        subtotal += linha['total']
        total += linha['total']

    if ultima_loja is not None:
        linhas.append({'subtotal': subtotal})
    linhas.append({'total': total})

    context = {'linhas': linhas}

    return render(request, 'core/quotation_list_min.html', context)


def quotation_list2(request):
    stores = Store.objects.all()
    products = Product.objects.all()
    # indice
    index_store = {store.id: index for index, store in enumerate(stores)}
    index_product = {product.id: index for index,
                     product in enumerate(products)}
    # dados para o template
    cabecalho = ["Lojas"] + [store.store for store in stores]
    linhas = [([product.product] + [None for store in stores] + [(0, 0, 0, None, product.product)])
              for product in products] + [["Subtotal"] + [(0, 0, 0, store.store, None) for store in stores]
                                          + [(0, 0, 0, None, None)]]

    for pev in Quotation.objects.all():
        total = pev.price * pev.quantity

        i0 = index_product[pev.product_id]
        i1 = index_store[pev.store_id] + 1
        valor = (pev.price, pev.quantity, total, pev.store, pev.product)

        linhas[i0][i1] = valor

        # Subtotal da linha
        linhas[i0][len(stores) + 1] = soma_tuplas(
            linhas[i0][len(stores) + 1], valor)

        # Subtotal da coluna
        linhas[len(products)][i1] = soma_tuplas(
            linhas[len(products)][i1], valor)

        # Total da tabela
        linhas[len(products)][len(stores) + 1] = soma_tuplas(
            linhas[len(products)][len(stores) + 1], valor)

    # retorna o menor preço de cada produto
    # a quantidade, total e loja também estão nesta lista
    mais_barato = []
    for linha in linhas:
        mais_barato.append(min(linha[1:]))

    # loja mais barata
    loja_mais_barata = min(linhas[-1][1:])[3]

    # destaca os menores preços no template
    mb = 0
    if request.GET.get('mais_barato', False):
        mb = 1

    # mostra somente os menores preços
    smb = 0
    if request.GET.get('somente_mais_barato', False):
        smb = 1

    linhas_mais_barato = zip(linhas, mais_barato)

    # mostra os produtos mais baratos, a quantidade e o total
    bqt = 0
    if request.GET.get('quantidade_e_total', False):
        # linhas_mais_barato = sorted(linhas_mais_barato,
        # key=lambda store: str(store[1][3]))  # sort by store
        bqt = 1

    context = {
        'cabecalho': cabecalho,
        'linhas_mais_barato': linhas_mais_barato,
        'loja_mais_barata': loja_mais_barata,
        'mb': mb,
        'smb': smb,
        'bqt': bqt,
    }
    return render(request, 'core/quotation_list2.html', context)


class QuotationCreate(CreateView):
    template_name = 'core/quotation_form.html'
    model = Quotation
    fields = '__all__'
    success_url = reverse_lazy('quotation_list')


'''
def pivottable(request):
    exams = Exam.objects.all()
    transposed = {}

    for exam in exams:
        transposed['name'] = exam.name
    print(transposed)
    # transposed.setdefault(exam['name'], {}).update({'exam%s' % exam['exam']: exam['score']})

    return render(request, 'core/pivottable.html', {'transposed': transposed})
'''
