package com.company;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;

public class SortingOverview {
    public static void main(String[] args) {
//        int[] arr = new int[]{5, 4, 3, 2, 12, 9};
//        Arrays.sort(arr);
//        for (int ele : arr) {
//            System.out.print(ele + " ");
//        }
        ArrayList<Node> nodes = new ArrayList<>(Arrays.asList(new Node(2, 3),
                new Node(9, 6), new Node(4, 1),
                new Node(3, 12), new Node(3, 4)));
//        nodes.sort(Comparator.comparing((Node x) -> x.v2));
        ArrayList<Integer> indexes = new ArrayList<>();
        for (int i = 0; i < nodes.size(); i++) indexes.add(i);
        indexes.sort(Comparator.comparing((Integer x) -> nodes.get(x).v1).
                thenComparing((Integer x) -> nodes.get(x).v2));
        for (Integer id : indexes) {
            System.out.println(id + " and " + nodes.get(id).toString());
        }
    }
}
