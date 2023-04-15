# Puretech Assessment Python

Question 1:

Prepare a code script using Python that will insert all of the items from list “new_customer_id” into list “customer_id”. You need to ensure that the contents of “customer_id” is unique afterwards; no duplicated values. Print the contents of “customer_id” in ascending order. 

customer_id = [77,33,66,22,99]
new_customer_id = [11,22,44,55,66,88,99]

Question 2:

Table below shows items listing where its price will change based on the effective date.

Item	Base price	1 Jan 2020	1 Feb 2020	1 Mar 2020	1 Apr 2020	1 May 2020
A	RM 20.00	RM 20.00	RM 25.70	RM 25.70	RM 23.50	RM 18.50
B	RM 30.60	RM 30.90	RM 30.90	RM 30.90	RM 37.50	RM 30.00
C	RM 0.00	RM 5.00	RM 15.30	RM 16.00	RM 16.00	RM 10.00

The price of the items will progressively change from time to time. For example, the price of item A on 23rd March 2020 is RM 25.70.

Partial code script using Python is provided in the solution box below, in which you will have to finalize and provide the missing codes for the function “get_price()”.

Question 3:

Develop a function code using Python that is able to convert USD to MYR currency for a specific value at a specific date. To achieve this you will utilize Bank Negara Malaysia’s public API.

API details:
URL	https://api.bnm.gov.my/public/exchange-rate/usd/date/{insert date here}?session=0900&quote=rm

Example full API URL for date 2023-01-10:
https://api.bnm.gov.my/public/exchange-rate/usd/date/2023-01-10?session=0900&quote=rm
Method	GET
Headers	Accept	application/vnd.BNM.API.v1+json

Sample response	Success	{
    "data": {
        "currency_code": "USD",
        "unit": 1,
        "rate": {
            "date": "2023-01-10",
            "buying_rate": 4.3700000000000001,
            "selling_rate": 4.3760000000000003,
            "middle_rate": 4.3730000000000002
        }
    },
    "meta": {
        "quote": "rm",
        "session": "0900",
        "last_updated": "2023-01-20 23:02:04",
        "total_result": 1
    }
}
Error	{
    "message": "No records found.",
    "code": 404
}

For full details of the API, you may visit https://apikijangportal.bnm.gov.my/openapi?category=Rates%20and%20Volumes, select “Exchange Rates”, Endpoint: By Currency And Date.

Once received a success response from the API, use the “buying_rate” value from the success response to convert USD to MYR currency.

Partial code script is provided in the solution box below, in which you will have to finalize and provide the missing codes for the function “get_usd_to_myr()”.
