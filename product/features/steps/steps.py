from behave import given, when, then
from product.models import Product

@given('I have a product named "{name}" and priced "{price}"')
def step_given_have_a_product(context, name, price):
    context.product = Product.objects.create(name = name, price = price)

@when('I add the product to the product lists')
def step_when_add_product_to_product_list(context):
    #Product already created in the previous step
    pass

@then('The product named "{name}" should be in the products list')
def step_then_product_should_be_in_the_list(context, name):
    product = Product.objects.filter(name=name)
    assert product is not None

@given('There are products in the products list')
def step_given_products_in_products_list(context):
    Product.objects.create(name="Teh Javana", price=3000)
    Product.objects.create(name="Teh Pucuk", price=4000)

@when('I search the product with the name "{name}"')
def step_when_search_for_a_product(context, name):
    context.search_results = Product.objects.filter(name=name)

@then('I should see the product named "{name}" in the products list')
def step_when_view_list_of_products(context, name):
    assert context.search_results.filter(name=name).exists()

@when('I view the list of the products')
def step_when_view_list_of_products(context):
    context.products_list = Product.objects.all()

@then('I should see the product named "{name}" in the list')
def step_then_should_see_book_in_list(context, name):
    assert context.products_list.filter(name=name).exists()

