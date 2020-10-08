package com.company;

import java.util.Stack;

public class StackOverview {
    public static void main(String[] args) {
        Stack<Integer> st = new Stack<>();
        st.add(1);
        st.add(2);
        st.add(3);
        while (!st.empty()) {
            System.out.println(st.pop());
        }
    }
}
