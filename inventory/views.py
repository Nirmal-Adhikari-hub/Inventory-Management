from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views import View
from .models import Product, Category, Supplier, Transaction
from .forms import ProductForm, CategoryForm, SupplierForm, TransactionForm



class ProductListView(View):
    def get(self, request):
        products = Product.objects.all()
        return render(request, 'inventory/product/product_list.html', {'products': products})


class ProductDetailView(View):
    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        return render(request, 'inventory/product/product_detail.html', {'product': product})


class ProductCreateView(View):
    def get(self, request):
        form = ProductForm()
        return render(request, 'inventory/product/product_form.html', {'form': form})

    def post(self, request):
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f"Product created successfully.")
            return redirect('product_list')
        return render(request, 'inventory/product/product_form.html', {'form': form})


class ProductUpdateView(View):
    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        form = ProductForm(instance=product)
        return render(request, 'inventory/product/product_update.html', {'form': form, 'product': product})

    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, f"Product '{product.name}' updated successfully.")
            return redirect('product_list')
        return render(request, 'inventory/product/product_update.html', {'form': form, 'product': product})


class ProductDeleteView(View):
    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        return render(request, 'inventory/product/product_confirm_delete.html', {'product': product})

    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        product.delete()
        messages.success(request, f"Product {product.name} deleted successfully.")
        return redirect('product_list')

# Category Views
class CategoryListView(View):
    def get(self, request):
        categories = Category.objects.all()
        return render(request, 'inventory/category/category_list.html', {'categories': categories})
        

class CategoryCreateView(View):
    def get(self, request):
        form = CategoryForm()
        return render(request, 'inventory/category/category_create.html', {'form': form})
    
    def post(self, request):
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Category created successfully.")
            return redirect('category_list')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"Error in {field}: {error}")
            return render(request, 'inventory/category/category_create.html', {'form': form})

        

class CategoryUpdateView(View):
    def get(self, request, pk):
        category = get_object_or_404(Category, pk=pk)
        form = CategoryForm(instance=category)
        return render(request, 'inventory/category/category_update.html', {'form':form, 'caegory': category})
    
    def post(self, request, pk):
        category = get_object_or_404(Category, pk=pk)
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, "Category updated successfully.")
            return redirect('category_list')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"Error in {field}: {error}")
            return render(request, 'inventory/category/category_update.html', {'form': form, 'category': category})
    


class CategoryDeleteView(View):
    def get(self, request, pk):
        category = get_object_or_404(Category, pk=pk)
        return render(request, 'inventory/Category/category_delete_confirm.html', {'category': category})

    def post(self, request, pk):
        category = get_object_or_404(Category, pk=pk)
        category.delete()
        messages.success(request, "Category deleted successfully.")
        return redirect('category_list')

    


# Supplier Views



class SupplierListView(View):
    def get(self, request):
        suppliers = Supplier.objects.all()
        return render(request, 'inventory/supplier/supplier_list.html', {'suppliers': suppliers})
    

class SupplierCreateView(View):
    def get(self, request):
        form = SupplierForm()
        return render(request, 'inventory/supplier/supplier_create.html', {'form': form})
    
    def post(self, request):
        form = SupplierForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Supplier created successfully.")
            return redirect('supplier_list')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"Error in {field}: {error}")
                return render(request, 'inventory/supplier/supplier_create.html', {'form': form})
            

class SupplierDetailView(View):
    def get(self, request, pk):
        supplier = get_object_or_404(Supplier, pk=pk)
        return render(request, 'inventory/supplier/supplier_detail.html', {'supplier': supplier})
    

class SupplierUpdateView(View):
    def get(self, request, pk):
        supplier = get_object_or_404(Supplier, pk=pk)
        form = SupplierForm(instance=supplier)
        return render(request, 'inventory/supplier/supplier_update.html', {'form': form, 'supplier':supplier})
    
    def post(self, request, pk):
        supplier = get_object_or_404(Supplier, pk=pk)
        form = SupplierForm(request.POST, instance=supplier)
        if form.is_valid():
            form.save()
            messages.success(request, f"Supplier '{supplier.name}' updated successfully.")
            return redirect('supplier_list')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"Error in {field}: {error}")
            return render(request, 'inventory/supplier/supplier_update.html', {'form': form, 'supplier': supplier})

        

class SupplierDeleteView(View):
    def get(self, request, pk):
        supplier = get_object_or_404(Supplier, pk=pk)
        return render(request, 'inventory/supplier/supplier_delete_confirm.html', {'supplier':supplier})
    
    def post(self, request, pk):
        supplier = get_object_or_404(Supplier, pk=pk)
        supplier.delete()
        messages.success(request, f"Supplier '{supplier.name}' deleted successfully.")
        return redirect('supplier_list')
    





# Transaction Views



class TransactionListView(View):
    def get(self, request):
        transactions = Transaction.objects.all()
        return render(request, 'inventory/transaction/transaction_list.html', {'transactions': transactions})
    

class TransactionCreateView(View):
    def get(self, request):
        form = TransactionForm()
        return render(request, 'inventory/transaction/transaction_create.html', {'form': form})
    
    def post(self, request):
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Transaction created successfully.")
            return redirect('transaction_list')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"Error in {field}: {error}")
                return render(request, 'inventory/transaction/transaction_create.html', {'form': form})
            

class TransactionDetailView(View):
    def get(self, request, pk):
        transaction = get_object_or_404(Transaction, pk=pk)
        return render(request, 'inventory/transaction/transaction_detail.html', {'transaction': transaction})
    

class TransactionUpdateView(View):
    def get(self, request, pk):
        transaction = get_object_or_404(Transaction, pk=pk)
        form = TransactionForm(instance=transaction)
        return render(request, 'inventory/transaction/transaction_update.html', {'form': form, 'transaction':transaction})
    
    def post(self, request, pk):
        transaction = get_object_or_404(Transaction, pk=pk)
        form = TransactionForm(request.POST, instance=transaction)
        if form.is_valid():
            form.save()
            messages.success(request, f"Transaction '{transaction.name}' updated successfully.")
            return redirect('transaction_list')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"Error in {field}: {error}")
            return render(request, 'inventory/transaction/transaction_update.html', {'form': form, 'transaction': transaction})

        

class TransactionDeleteView(View):
    def get(self, request, pk):
        transaction = get_object_or_404(Transaction, pk=pk)
        return render(request, 'inventory/transaction/transaction_delete_confirm.html', {'transaction':transaction})
    
    def post(self, request, pk):
        transaction = get_object_or_404(Transaction, pk=pk)
        transaction.delete()
        messages.success(request, f"Transaction '{transaction.name}' deleted successfully.")
        return redirect('transaction_list')