# PyTest with Browserstack

PyTest Integration with BrowserStack.

![BrowserStack Logo](https://d98b8t1nnulk5.cloudfront.net/production/images/layout/logo-header.png?1469004780)
## Prerequisite
* Python3

## Setup

* Clone the repo
* Install dependencies `pip install -r requirements.txt`
* To run your automated tests using BrowserStack, you must provide a valid username and access key. This can be done either by using a .browserstack configuration file in the working directory or your home directory, by setting the BROWSERSTACK_USERNAME and BROWSERSTACK_ACCESS_KEY environment variables, or by adding user & key to config file.

## About the tests in this repository

This repository contains the following Cucumber tests:

| Module  | Test name                           | Description                                                                                                                                                                                                                                                                       | Tag     |
| ------- | ----------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| E2E     | End to End Scenario                 | This test scenario verifies successful product purchase lifecycle end-to-end. It demonstrates the [Page Object Model design pattern](https://www.browserstack.com/guide/page-object-model-in-selenium-python) and is also the default test executed in all the single test run profiles. | e2e     |
| Login   | Login with given username           | This test verifies the login workflow with different types of valid login users.                                                                                                                                                                                                  | login   |
| Login   | Login as Locked User                | This test verifies the login workflow error for a locked user.                                                                                                                                                                                                                    | login   |
| Offers  | Offers for Mumbai location          | This test mocks the GPS location for Mumbai and verifies that the product offers applicable for the Mumbai location are shown.                                                                                                                                                    | offers  |
| Product | Apply Apple & Samsung Vendor Filter | This test verifies that only Apple and Samsung products shown if the Apple and Samsung vendor filter option is applied.                                                                                                                                                           | product |
| Product | Apply Lowest to Highest Order By    | This test verifies that the product prices are in ascending order when the product sort "Lowest to Highest" is applied.                                                                                                                                                           | product |
| User    | Login as User with no image loaded  | This test verifies that the product images load for user: "image_not_loading_user" on the e-commerce application. Since the images do not load, the test case assertion fails.                                                                                                    | user    |
| User    | Login as User with existing Orders  | This test verifies that existing orders are shown for user: "existing_orders_user"                                                                                                                                                                                                | user    |

---

# On Premise

This infrastructure points to running the tests on your own machine using a browser (e.g. Chrome) using the browser's driver executables (e.g. ChromeDriver for Chrome). Selenium enables this functionality using WebDriver for many popular browsers.

## Om-Prem Prerequisites

-   For this infrastructure configuration (i.e on-premise), ensure that the ChromeDriver is downloaded and added to the [driver](src/driver) directory.

Note: The ChromeDriver version must match the Chrome browser version on your machine.

## Running Your Tests

### Run the entire test suite on your own machine

-   How to run the test?

    To run the entire test suite on your own machine, use the following command:

    ```sh
    paver run single on-prem
    ```

-   Output

    This run profile executes the entire test suite sequentially on a single browser, on your own machine.

---
# BrowserStack

[BrowserStack](https://browserstack.com) provides instant access to 3,000+ real mobile devices and browsers on a highly reliable cloud infrastructure that effortlessly scales as testing needs grow.

## BrowserStack Prerequisites

-   Create a new [BrowserStack account](https://www.browserstack.com/users/sign_up) or use an existing one.
-   Identify your BrowserStack username and access key from the [BrowserStack Automate Dashboard](https://automate.browserstack.com/) and export them as environment variables using the below commands.

    -   For \*nix based and Mac machines:

    ```sh
    export BROWSERSTACK_USERNAME=<browserstack-username> &&
    export BROWSERSTACK_ACCESS_KEY=<browserstack-access-key>
    ```

    -   For Windows:

    ```shell
    set BROWSERSTACK_USERNAME=<browserstack-username>
    set BROWSERSTACK_ACCESS_KEY=<browserstack-access-key>
    ```

    Alternatively, you can also hardcode username and access_key objects in the [single.json](src/resources/single.json) file, [parallel.json](src/resources/parallel.json) and [local.json](src/resources/local.json).

Note:

-   The exact test capability values can be easily identified using the [Browserstack Capability Generator](https://browserstack.com/automate/capabilities)

## Running Your Tests

### Run the entire test suite in parallel on a single BrowserStack browser

In this section, we will run the tests in parallel on a single browser on Browserstack. 

-   How to run the test?

    To run the entire test suite in parallel on a single BrowserStack browser, use the following command:

    ```sh
    paver run single remote
    ```

-   Output

    This run profile executes the entire test suite in parallel on a single BrowserStack browser. Please refer to your [BrowserStack dashboard](https://automate.browserstack.com/) for test results.

### Run the entire test suite in parallel on multiple BrowserStack browsers

In this section, we will run the tests in parallel on multiple browsers on Browserstack.

-   How to run the test?

    To run the entire test suite in parallel on multiple BrowserStack browsers, use the following command:

    ```sh
    paver run parallel remote
    ```
### [Web application hosted on internal environment] Running your tests on BrowserStack using BrowserStackLocal

#### Prerequisites

-   Clone the [BrowserStack demo application](https://github.com/browserstack/browserstack-demo-app) repository.
    ```sh
    git clone https://github.com/browserstack/browserstack-demo-app
    ```
-   Please follow the README.md on the BrowserStack demo application repository to install and start the dev server on localhost.
-   In this section, we will run a single test case to test the BrowserStack Demo app hosted on your local machine i.e. localhost. Refer to the `browserstack.local` object in `nightwatch-browserstack.conf.js` file to change test capabilities for this configuration.
-   Note: You may need to provide additional BrowserStackLocal arguments to successfully connect your localhost environment with BrowserStack infrastructure. (e.g if you are behind firewalls, proxy or VPN).
-   Further details for successfully creating a BrowserStackLocal connection can be found here:

    -   [Local Testing with Automate](https://www.browserstack.com/local-testing/automate)

## Run tests on locally hosted websites

-   How to run the test?

    -   To run the default test scenario (e.g. End to End Scenario) on a single BrowserStack browser using BrowserStackLocal, use the following command:

    ```sh
    paver run local remote
    ```

-   Output

    This run profile executes a single test on an internally hosted web application on a single browser on BrowserStack. Please refer to your BrowserStack dashboard(https://automate.browserstack.com/) for test results.


 Understand how many parallel sessions you need by using our [Parallel Test Calculator](https://www.browserstack.com/automate/parallel-calculator?ref=github)

## Notes
* You can view your test results on the [BrowserStack Automate dashboard](https://www.browserstack.com/automate)
* To test on a different set of browsers, check out our [platform configurator](https://www.browserstack.com/automate/python#setting-os-and-browser)
