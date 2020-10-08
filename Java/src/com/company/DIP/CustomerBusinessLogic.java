package com.company.DIP;

public class CustomerBusinessLogic {
    private ICustomerDA _dataAccess;

    public CustomerBusinessLogic(ICustomerDA dataAccess) {
        this._dataAccess = dataAccess;
    }

    public String getCustomerName(int id) {
       return this._dataAccess.getCustomerName(id);
    }
}
