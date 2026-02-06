from django.contrib import admin
from .models import Category, Products

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'is_active', 'created_at')
    list_filter = ('is_active', 'created_at')
    search_fields = ('name', 'slug')
    list_editable = ('is_active',)
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name', 'category_id', 'price', 'stock', 'is_active', 'created_at')
    list_filter = ('category_id', 'is_active', 'created_at')
    search_fields = ('name', 'description')
    list_editable = ('price', 'stock', 'is_active')
    list_per_page = 25
    prepopulated_fields = {'slug': ('name',)}
