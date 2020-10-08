package com.company.DIP;

public class SpecificCustomerDA implements ICustomerDA {
    public SpecificCustomerDA() {

    }

    @Override
    public String getCustomerName(int id) {
        return "Huy " + "from company X";
    }
}
