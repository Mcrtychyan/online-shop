from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, DeleteView, UpdateView, ListView, DetailView
from django.urls import reverse_lazy
from .models import Category, Products
from .forms import CategoryForm, ProductForm

def category_list(request):
    context = {
        'categories': Category.objects.all()
    }
    return render(request, "myapp/categories_list.html", context)

class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category_form.html'
    success_url = reverse_lazy('category_list')

class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'myapp/category_confirm_delete.html'
    success_url = reverse_lazy('category_list')

class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category_form.html'
    success_url = reverse_lazy('category_list')

def category_detail(request, pk):
    category = Category.objects.get(pk=pk)
    products = category.products.all()
    context = {
        'category': category,
        'products': products
    }
    return render(request, 'myapp/category_detail.html', context)

class ProductListView(ListView):
    model = Products
    template_name = 'myapp/product_list.html'
    context_object_name = 'products'
    paginate_by = 12

    def get_queryset(self):
        queryset = Products.objects.filter(is_active=True)
        category_slug = self.kwargs.get('category_slug')
        if category_slug:
            queryset = queryset.filter(category_id__slug=category_slug)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.filter(is_active=True)
        context['category'] = None
        category_slug = self.kwargs.get('category_slug')
        if category_slug:
            context['category'] = get_object_or_404(Category, slug=category_slug, is_active=True)
        return context

class ProductCreateView(CreateView):
    model = Products
    form_class = ProductForm  # Создайте форму
    template_name = 'myapp/product_form.html'
    success_url = reverse_lazy('product_list')

class ProductUpdateView(UpdateView):
    model = Products
    form_class = ProductForm
    template_name = 'myapp/product_form.html'
    success_url = reverse_lazy('product_list')

class ProductDeleteView(DeleteView):
    model = Products
    template_name = 'myapp/product_confirm_delete.html'
    success_url = reverse_lazy('product_list')

class ProductDetailView(DetailView):
    model = Products
    template_name = 'myapp/product_detail.html'
    context_object_name = 'product'

    def get_queryset(self):
        return Products.objects.filter(is_active=True)