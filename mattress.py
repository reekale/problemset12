# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 15:54:51 2021

@author: Ria Kale

This function is designed to output the price a customer will have to pay for a mattress
after inputting variables

I completed this assignment individually
"""

prices = [[[1800,2200,2400],[1400,1800,200],[900,1300,1500]],[[2000,2500,3000],[1400,1900,2400],[1000,1500,2000]], [400,300,200,100], [100,300]]
identifiers = [["Sealy Mattress", "Simmons Mattress"], ["King Size", "Queen Size", "Full Size", "Twin Size"], ["Medium", "Firm", "Extra Firm"]]

def mattressPOS(prices):
    print("Welcome!")
    brand = input("Please select the mattress brand (1 - Sealy, 2 - Simmons):")
    while True: 
        if brand == "1" :
            brand = 0
            size = input("Please select the size (K = King, Q= Queen, T = Twin):")
            break
        elif brand == "2" :
            brand = 1
            size = input("Please select the size (K = King, Q= Queen, F = Full):")
            break
        else:
            print ("Please enter a valid response")
    
    while True:
        if size == "K" or size.lower() == "k":
            size = 0
            break
        elif size == "Q" or size.lower() == "q":
            size = 1
            break
        elif size == "T" or size.lower() == "t":
            size = 2
            break
        elif size == "F" or size.lower() == "f":
            size = 2
            break
        else:
            print("Please enter a valid response")
        
    while True:
        comfort = input("Please select comfort level (M - Medium, F - Firm, E - Extra Firm):")
        if comfort == "M" or comfort.lower() == "m":
            comfort = 0
            break
        elif comfort == "F" or comfort.lower() == "f":
            comfort = 1
            break
        elif comfort == "E" or comfort.lower() == "e":
            comfort = 2
            break
        else:
            print("Please enter a valid response")
        
    while True:
        box_spring = input("Would you like to add box springs (Y - Yes, N - No)?")
        if box_spring =="Y" or box_spring.lower() == "y":
            box_spring = prices[2][size]
            break
        elif box_spring =="N" or box_spring.lower() == "n":
            box_spring = "${:,.2f}".format(0)
            break
        else:
            print("Please enter a valid response")
    
    while True:
        shipping = input("Which shipping mode do you like (S - Standard, N - Next Day)?")
        if shipping =="S" or shipping.lower() == "s":
            shipping = 0
            break
        elif shipping =="N" or shipping.lower() == "n":
            shipping = 1
            break
        else:
            print("Please enter a valid response")
            
    promo_code = input("Promotion Code:")
    print(  )
    print(  )
        
        
    mattress_price = prices[brand][size][comfort]
    formatted_mattress_price = "${:,.2f}".format(mattress_price)
    
    if brand == 0 and size == 2:
        size = 3
    box_spring_price = prices[2][size]
    formatted_spring_price = "${:,.2f}".format(box_spring_price)
    
    if promo_code == "SLEEP" or promo_code.lower():
       promo_code = -((mattress_price + box_spring_price) * 0.1)
    else:
        promo_code = 0
    
    formatted_promo_code = "${:,.2f}".format(promo_code)
    
    subtotal = mattress_price + box_spring_price + promo_code
    formatted_subtotal = "${:,.2f}".format(subtotal)
    
    shipping_price = prices[3][shipping]
    formatted_shipping_price = "${:,.2f}".format(shipping_price)
    
    tax_rate = subtotal*0.0625
    formatted_tax = "${:,.2f}".format(tax_rate)
    
    total = subtotal + shipping_price + tax_rate
    formatted_total = "${:,.2f}".format(total)
    
    id_1 = identifiers[0][brand]
    id_2 = identifiers[1][size]
    id_3 = identifiers[2][comfort]
    
    print(id_1,",", id_2,",", id_3)
    print(  )
    print("="*15, "Order Summary", "="*15 )
    print(  )
    print(f"{'Mattress:':<24} {formatted_mattress_price:>8}")
    print(f"{'Box Springs:':<24} {formatted_spring_price:>8}")
    print(f"{'Discount:':<24} {formatted_promo_code:>8}")
    print(f"{'Subtotal:':<24} {formatted_subtotal:>8}")
    print(f"{'Shipping:':<24} {formatted_shipping_price:>8}")
    print(f"{'Tax:':<24} {formatted_tax:>8}")
    print("-"*46)
    print(f"{'Total:':<24} {formatted_total:>8}")
    
mattressPOS(prices)