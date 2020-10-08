package com.company.DIP;

public class Test {
    public static void main(String[] args) {
        CustomerBusinessLogic cbl = new CustomerBusinessLogic(new CustomerDA());
        System.out.println(cbl.getCustomerName(0));
        CustomerBusinessLogic cbl2 = new CustomerBusinessLogic(new SpecificCustomerDA());
        System.out.println(cbl2.getCustomerName(0));
    }
}
