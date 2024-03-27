'''
Created on Jun 8, 2022

@author: bborade
'''
import json

json_data = {
  "TransRequest" : {
    "ADSDKSpecVer" : "6.13.8",
    "CRMToken" : "",
    "CorpID" : "25405",
    "EcommerceIndicator" : "Y",
    "POSEnvironmentIndicator" : "",
    "KI" : "",
    "CardType" : "",
    "CardNumber" : "",
    "DomainId" : "",
    "URLType" : "",
    "TemplateId" : "",
    "SubCardType" : "",
    "CardExpiryDate" : "0728",
    "CustomerFirstName" : "Duo",
    "CustomerLastName" : "Lingo",
    "CustomerEmail" : "duolingo@exmaple.com",
    "TransAmountDetails" : {
      "TaxAmount" : "0.00",
      "Discount" : "0.00",
      "ProductTotalAmount" : "0.00",
      "TenderAmount" : "0.00",
      "TransactionTotal" : "1.00"
    },
    "ECOMMInfo" : {
      "MerchantIdentifier" : "100000092723",
      "StoreId" : "210001",
      "TerminalId" : "31420964",
      "CardIdentifier" : "",
      "OneTimeToken" : "",
      "OneOrderToken" : "",
      "CVV" : ""
    },
    "ECOMMFingerPrintInfo" : null,
    "FraudScoreInfo" : {
      "DeviceFingerPrintId" : null,
      "LoggedInState" : null,
      "MDDF" : null,
      "PickupState" : null,
      "PickupStore" : null,
      "RnfInquiry" : "00",
      "ShippingCompany" : null,
      "ShippingMethod" : null
    },
    "TransactionType" : "04",
    "SubTransType" : "",
    "InvoiceNumber" : "",
    "ReferenceNumber" : "",
    "LanguageIndicator" : "00",
    "PostAuthSequenceNo" : "",
    "PostAuthCount" : "",
    "BillingAddress" : {
      "BillingAddressLine1" : "5950 Colwell Blvd",
      "BillingAddressLine2" : "",
      "BillingCity" : "TX",
      "BillingCountry" : "United States",
      "BillingEmailId" : "test@example.com",
      "BillingFirstName" : "Duo",
      "BillingLastName" : "Lingo",
      "BillingMobileNumber" : "",
      "BillingState" : "MA",
      "BillingZip" : "75039"
    },
    "ShippingInfo" : null,
    "OrigTransactionIdentifier" : "",
    "OrigAurusPayTicketNum" : "",
    "CurrencyCode" : "840",
    "TransactionDate" : "",
    "TransactionTime" : "",
    "Level3ProductsData" : null,
    "ClerkID" : "",
    "PONumber" : "",
    "PODate" : ""
  }
}