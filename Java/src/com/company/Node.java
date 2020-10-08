package com.company;

public class Node {
    int v1;
    int v2;

    public Node(int v1, int v2) {
        this.v1 = v1;
        this.v2 = v2;
    }

    @Override
    public String toString() {
        return "Node{ " +
                "v1= " + v1 +
                ", v2= " + v2 +
                " }";
    }
}
