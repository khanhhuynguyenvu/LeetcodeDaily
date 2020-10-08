package com.company;

public class Main {
    public static void main(String[] args) {
        int[] givens = new int[]{1, 3, 0, 2, 1};
        for (int ele : findProduct(givens)) {
            System.out.println(ele);
        }
    }

    private static int[] findProduct(int[] arr) {
        int product = 1;
        int zero = 0;
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] != 0) product *= arr[i];
            else zero++;
        }
        int[] ans = new int[arr.length];
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == 0 && zero == 1) {
                ans[i] = product;
            } else if (arr[i] != 0 && zero > 0) {
                ans[i] = 0;
            } else {
                ans[i] = product / arr[i];
            }
        }
        return ans;
    }
}