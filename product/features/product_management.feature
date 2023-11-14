Feature: Product Management

    Scenario: Add A Product
    Given I have a product named "Teh Javana" and priced "3000"
    When I add the product to the product list
    Then the product "Teh Javana" should be listed in the product list

    Scenario: Search For A Product
    Given I have a product named "Teh Javana" and priced "3000"
    When I search for products named "Teh Javana"
    Then I should see the product named "Teh Javana" in the search result

    Scenario: View All Product
    Given there are products in the product lists
    When I view the list of the products
    Then I should see the product named "Teh Javana" in the products list