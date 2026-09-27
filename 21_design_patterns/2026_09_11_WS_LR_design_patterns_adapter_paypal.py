PaymentService Interface

==========

public interface PaymentService {

 void pay(double amountInEuro);

}




==========================

// Unsere Anwendung

// PaymentService

// pay(double amount)

 

public class Checkout {

 

    private PaymentService paymentService;

 

 public Checkout(PaymentService paymentService) {

  this.paymentService = paymentService;

  }

 

 

 // PayPal, CreditCard

 // [Bezahlen]

 

 public void checkout(double amountInEuro) {

  paymentService.pay(amountInEuro);

 }

}

=================

Unsere konkrete Nutzen (noch unser Code)

BankPayment

========

public class BankPayment implements PaymentService {

 

 private double balance;

 

 public BankPayment(double balance) {

  this.balance = balance;

 }

 

 @Override

 public void pay(double amount) {

  if(balance >= amount) {

   System.out.println("You balance was " + balance + " Euro");

   balance = balance - amount;

   System.out.println("You have transfered " + amount + " Euro");

   System.out.println("You current balance is now " + balance + " Euro");

   

  } else {

   System.out.println("You do not have sufficient funds in your bank account!");

   System.out.println("Thus the transfer will not be processed.");

  }

 }

}

====================

Unsere konkrete Nutzen (noch unser Code)

BankPayment

========

public class BankPayment implements PaymentService {

 

 private double balance;

 

 public BankPayment(double balance) {

  this.balance = balance;

 }

 

 @Override

 public void pay(double amount) {

  if(balance >= amount) {

   System.out.println("You balance was " + balance + " Euro");

   balance = balance - amount;

   System.out.println("You have transfered " + amount + " Euro");

   System.out.println("You current balance is now " + balance + " Euro");

   

  } else {

   System.out.println("You do not have sufficient funds in your bank account!");

   System.out.println("Thus the transfer will not be processed.");

  }

 }

}

====================

Nun kommt eine fremde Api von PayPal

===============

Klasse: PayPalApi,  Methode send(betrag_in_cent)

So ungefähre wäre der Code =====

// PayPal

// PayPalApi

// sendPayment(int cents)  

// PROBLEM: Nicht kompatibel zu unserer Anwendung PaymentService mit pay(double amountInEuro)

public class PayPalApi{

 

 public void sendPayment(int amountInCents) {

  System.out.println("PayPal-Zahlung: " + amountInCents + " Cents");

 }

}

=====================

PayPalApi ist nicht kompatibel mit unserem System mit PaymentService, die eine pay(amount) hat.

Lösung: Adapter Pattern

/ Adapter Pattern: implementiert meine eigene Service

public class PayPalAdapter implements PaymentService{

 

 private PayPalApi payPalApi;

 

 public PayPalAdapter(PayPalApi payPalApi) {

  this.payPalApi = payPalApi;

 }

 

 

 @Override

 public void pay(double amount) {

  // Nutze die PayPalApi Methode (Dienst/Schnittstelle)

  int cents = (int) Math.round(amount * 100);

  payPalApi.sendPayment(cents);

  

 }

 

}

=============

Nutzen Beispiel

=========

public class Main {

 

 public static void main(String[] args) {

  

  

  

  BankPayment bankPayment = new BankPayment(2000); 

  

  Checkout co = new Checkout(bankPayment);

  co.checkout(1000);

  

 

  System.out.println("=====================");

  

  // Eine Dienst, die ich brauche, aber inkompatible Schnittstelle zu meinem Program!

    PayPalApi payPalApi = new PayPalApi();  

  // Lösung: Adapter Pattern: das was nicht passt, wird passend gemacht!

   PayPalAdapter payPalAdapter = new PayPalAdapter(payPalApi); // self.pay_pal_api = pay_pal_api

   payPalAdapter.pay(1000);

   

   CreditCard cc = new CreditCard();

   CreditCardAdapter ccAdapter = new CreditCardAdapter(cc);

   

 }

 

}

