# Automated Testing Project for DaciaPlant.ro Website


## Introduction

This project is dedicated to automated testing of the Dacia Plant website using Selenium in the Python programming language. It was created to apply and enhance the knowledge gained from a course on automated testing. The objective is to demonstrate practical skills in testing web applications by focusing on a real-world e-commerce site. The project involves simulating user interactions such as product searches, adding items to the shopping cart, subscribing to newsletters, and managing the login/logout processes.

## Technical Information

**Selenium WebDriver**: This is a powerful automation tool that allows for programmatic control and interaction with web browsers. With Selenium WebDriver, we can emulate user actions such as clicks, form submissions, and data input to automate the testing process. To use Selenium, we import the library and the webdriver class.

**PyCharm**: Serving as the primary Integrated Development Environment (IDE) for this project, PyCharm provides a robust environment for Python development, offering features that significantly enhance coding efficiency and productivity.

**XPATH Selectors**: XPATH is a versatile selector strategy that helps navigate the HTML structure of a web page. Using XPATH selectors, we can locate elements based on their hierarchical position in the document object model (DOM), allowing for precise element selection.

**CSS Selectors**: CSS selectors are strings used to identify elements within HTML code, enabling interaction and functionality testing. While generally faster than XPATH, CSS selectors are limited to traversing from parent to child elements.

**Unittest**: This Python standard library module provides a framework for writing and executing unit tests. It includes a set of classes and methods for organizing test cases, running tests, and asserting expected outcomes.

**HtmlTestRunner**:  HtmlTestRunner is a valuable tool for generating HTML reports from unit tests. It facilitates better communication of test results within teams and stakeholders, making it easier to share and review testing outcomes.


## Project Structure

**Test Suite**

The test suite integrates various test cases to ensure comprehensive testing of the Dacia Plant website. 

## Test Cases

**Login Tests**
1. Test Login with Valid Credentials - Verified successful login with valid email and password.

2. Test Login with Invalid Credentials - Verified that login fails with incorrect email and/or password.

3. Test Logout Functionality - Ensured proper session termination and redirection to the homepage after logout.

**Product Search. Cart and Wishlist Operations**

4. Test Search for Product - Searched for "Calmotusin" and verified that search results are displayed.

5. Test Add Product to Cart - Added "Biseptol Spray Propolis" to the cart and checked that the mini cart counter increased.

6. Test Remove Product from Cart - Added "Calmotusin comprimate" to the cart, then removed it, ensuring the mini cart counter updated correctly.

7. Test Add Product to Wishlist - Logged in, searched for "Belène Collagen beauty drink 28buc", added it to the wishlist, and verified redirection to the wishlist page.

**Newsletter Subscription**

8. Test Newsletter Subscription with Invalid Email - Attempted to subscribe with an invalid email and verified that the appropriate error message was displayed.

9. Test Newsletter Subscription with Valid Email - Subscribed with a valid email and verified the success message indicating the confirmation request was sent.

**Button Click Tests**

10. Test Contact Button Click - Clicked on the "Contact" button and verified redirection to the page with the title "Contactati-ne".

11. Test “Cum Comand” Button Click - Clicked on the "Cum Comand" button and verified redirection to the page with the title "Cum comand".


## Report
After running the tests, the results show that a total of 11 tests were executed, and all of them passed successfully. This indicates that the automated testing suite is robust and the functionalities of the Dacia Plant website are performing as expected. Below is a detailed overview of the tests and their outcomes:

**Test Summary**

Total Tests Executed: 11

Tests Passed: 11

Tests Failed: 0

Tests Skipped: 0

## Conclusion
This project demonstrates a comprehensive approach to automated testing of a web application. By focusing on the Dacia Plant website, it showcases practical skills in using Selenium WebDriver, CSS selectors, XPATH selectors, and the Unittest framework in Python. The project aims to provide a robust testing suite that ensures the reliability and functionality of the Dacia Plant webshop, contributing to a smoother user experience.

