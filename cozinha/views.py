from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import View, ListView, CreateView, UpdateView, DetailView, DeleteView
from cozinha.models import Product, Table
from django.urls import reverse
class ProductListView(ListView):
    """
        View para a listagem de produtos existentes.
    """

    model = Product
    template_name = 'products/list_view.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = Product.objects.filter(is_active=True)
        return context

    def get_queryset(self):
        user_org = self.request.user.selected_organization
        queryset = Product.objects.filter(is_active=True).order_by('name')
        return queryset
class ProductUpdateView(UpdateView):
    """
        View para alteração das informações de um produto existente.
    """

    model = Product
    # form_class = ProductForm
    template_name = 'products/update_view.html'

    def get_form_kwargs(self):
        kwargs = super(ProductUpdateView, self).get_form_kwargs()
        return kwargs

    # def get_success_url(self):
    #     return reverse("hr:sectors")
class ProductDeleteView(DeleteView):
    """
        View para deletar um produto existente.
    """

    model = Product
    template_name = 'products/delete_view.html'

    def get_object(self):
        obj = super(ProductDeleteView, self).get_object()
        if not obj.is_active:
            raise Http404
        return obj

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return redirect(self.get_success_url())

    # def get_success_url(self):
    #     # return reverse("hr:sectors")

class ProductCreateView(CreateView):
    """
        View para criação de um produto.
    """

    model = Product
    # form_class = ProductForm
    template_name = 'products/create_view.html'

    def get_form_kwargs(self):
        kwargs = super(ProductCreateView, self).get_form_kwargs()
        # org_obj = self.request.user.selected_organization
        # kwargs['org_obj'] = org_obj
        return kwargs

    def form_valid(self, form):
        # form.instance.organization = self.request.user.selected_organization
        return super().form_valid(form)

    # def get_success_url(self):
    #     return reverse("hr:sectors")
class ProductDetailView(DetailView):
    """
        View para exibir detalhes de um produto existente.
    """
    model = Product
    template_name = 'products/detail_view.html'

    def get_object(self):
        obj = super(ProductDetailView, self).get_object()
        if not obj.is_finished or not obj.employee.owner == self.request.user.selected_organization:
            raise Http404
        return obj

    def get_success_url(self):
        return reverse("")

class ProductDisableView(UpdateView):
    """
        View para desativar um produto existente.
    """

    model = Product
    template_name = 'product/disable_view.html'

    def get_form_kwargs(self):
        kwargs = super(ProductUpdateView, self).get_form_kwargs()
        return kwargs

    # def get_success_url(self):
    #     return reverse("hr:sectors")


class TableListView(ListView):
    """
        View para a listagem de mesas existentes.
    """

    model = Table
    template_name = 'tables/list_view.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        Tables = Table.objects.filter(is_active=True)
        return context

    def get_queryset(self):
        user_org = self.request.user.selected_organization
        queryset = Table.objects.filter(is_active=True).order_by('number')
        return queryset
class TableUpdateView(UpdateView):
    """
        View para alteração das informações de um produto existente.
    """

    model = Table
    # form_class = TableForm
    template_name = 'tables/update_view.html'

    def get_form_kwargs(self):
        kwargs = super(TableUpdateView, self).get_form_kwargs()
        return kwargs

    # def get_success_url(self):
    #     return reverse("hr:sectors")
class TableDeleteView(DeleteView):
    """
        View para deletar uma mesa existente.
    """

    model = Table
    template_name = 'tables/delete_view.html'

    def get_object(self):
        obj = super(TableDeleteView, self).get_object()
        if not obj.is_active:
            raise Http404
        return obj

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return redirect(self.get_success_url())

    # def get_success_url(self):
    #     # return reverse("hr:sectors")

class TableCreateView(CreateView):
    """
        View para criação de uma mesa.
    """

    model = Table
    # form_class = TableForm
    template_name = 'tables/create_view.html'

    def get_form_kwargs(self):
        kwargs = super(TableCreateView, self).get_form_kwargs()
        # org_obj = self.request.user.selected_organization
        # kwargs['org_obj'] = org_obj
        return kwargs

    def form_valid(self, form):
        # form.instance.organization = self.request.user.selected_organization
        return super().form_valid(form)

    # def get_success_url(self):
    #     return reverse("hr:sectors")
class TableDetailView(DetailView):
    """
        View para exibir detalhes de uma mesa existente.
    """
    model = Table
    template_name = 'tables/detail_view.html'

    def get_object(self):
        obj = super(TableDetailView, self).get_object()
        if not obj.is_finished or not obj.employee.owner == self.request.user.selected_organization:
            raise Http404
        return obj

    def get_success_url(self):
        return reverse("")

class TableDisableView(UpdateView):
    """
        View para desativar um produto existente.
    """

    model = Table
    template_name = 'table/disable_view.html'

    def get_form_kwargs(self):
        kwargs = super(TableUpdateView, self).get_form_kwargs()
        return kwargs

    # def get_success_url(self):
    #     return reverse("hr:sectors")