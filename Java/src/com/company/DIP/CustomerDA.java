package com.company.DIP;

public class CustomerDA implements ICustomerDA {
    public CustomerDA() {

    }

    @Override
    public String getCustomerName(int id) {
        return "Huy" + "is a customer";
    }
}
