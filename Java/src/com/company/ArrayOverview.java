package com.company;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

public class ArrayOverview {
    public static void main(String[] args) {
//        // 1d
//        int[] matrix1d = new int[]{1, 2, 3, 4};
//        // 2d
//        int rows = 3;
//        int[][] matrix2d = new int[rows][];
//        matrix2d[1] = new int[]{2, 3, 1};
//        matrix2d[2] = new int[]{5, 6};
//        matrix2d[0] = new int[]{12};
//        // 3d
//        int[][][] matrix3d = new int[2][][];

//         P1: Remove even integers from an array
//        int[] given = new int[]{1, 2, 2, 3, 5, 6, 7};
//        for (int num : removeEven(given)) {
//            System.out.print(num + " ");
//        }
//         P2: Merge two sorted arrays
//        int[] arr1 = new int[]{1, 2, 2, 14};
//        int[] arr2 = new int[]{2, 6, 7, 8};
//        for (int num : mergeArrays(arr1, arr2)) {
//            System.out.print(num + " ");
//        }
//        P3: Find two numbers that add up to n
//        int[] arr = new int[]{1, 21, 3, 14, 5, 60, 7, 6};
//        int[] ans_3 = findSum(arr, 27);
//        System.out.println(ans_3[0] + " " + ans_3[1]);
//        P7: Find Second Maximum Value in an Array
//        int[] givens = new int[]{9,2,3,6};
//        System.out.println(findSecondMaximum(givens));
//        P8: Right Rotate the Array by One Index
//        int[] givens = new int[]{1, 2, 3, 4, 5};
//        rotateArray(givens);
//        P9: Re-arrange Positive & Negative Values
//        int[] givens = new int[]{10, -1, 20, 4, 5, -9, -6};
//        reArrange(givens);
        int[] givens = new int[]{1, 2, 3, 4, 5};
        maxMin(givens);
    }

    // P1
    private static int[] removeEven(int[] arr) {
        int countOdd = 0;
        for (int ele : arr) {
            if (ele % 2 != 0) countOdd += 1;
        }
        int[] ans = new int[countOdd];
        int itr = 0;
        for (int ele : arr) {
            if (ele % 2 != 0) {
                ans[itr] = ele;
                itr += 1;
            }
        }
        return ans;
    }

    // P2
    private static int[] mergeArrays(int[] arr1, int[] arr2) {
        int n = arr1.length + arr2.length;
        int l1 = 0, l2 = 0, itr = 0;
        int[] ans = new int[n];
        while (l1 < arr1.length && l2 < arr2.length) {
            if (arr1[l1] < arr2[l2]) {
                ans[itr++] = arr1[l1++];
            } else {
                ans[itr++] = arr2[l2++];
            }
        }
        while (l1 < arr1.length) {
            ans[itr++] = arr1[l1++];
        }
        while (l2 < arr2.length) {
            ans[itr++] = arr2[l2++];
        }
        return ans;
    }

    // P3
    private static int[] findSum(int[] arr, int n) {
        Map<Integer, Integer> used = new HashMap<>();
        for (int i = 0; i < arr.length; i++) {
            used.put(arr[i], i);
        }
        int[] ans = new int[2];
        for (int i = 0; i < arr.length; i++) {
            if (used.getOrDefault(n - arr[i], -1) != -1) {
                ans = new int[]{n - arr[i], arr[i]};
            }
        }
        return ans;
    }

    // P7
    private static int findSecondMaximum(int[] arr) {
        if (arr.length < 2) return arr[0];
        for (int i = 0; i < 2; i++) {
            for (int j = i + 1; j < arr.length; j++) {
                if (arr[i] < arr[j]) {
                    int temp = arr[i];
                    arr[i] = arr[j];
                    arr[j] = temp;
                }
            }
        }
        return arr[1];
    }

    //P8
    private static void rotateArray(int[] arr) {
        int last = arr[arr.length - 1];
        for (int i = arr.length - 1; i > 0; i--) {
            arr[i] = arr[i - 1];
        }
        arr[0] = last;
    }

    //P9
    private static void reArrange(int[] arr) {
        int l = 0;
        for (int r = 1; r < arr.length; r++) {
            if (arr[l] >= 0 && arr[r] < 0) {
                int tmp = arr[r];
                arr[r] = arr[l];
                arr[l] = tmp;
                l++;
            }
        }
    }

    //P10
    private static void maxMin(int[] arr) {
        int[] ans = new int[arr.length];
        for (int i = 0, down = arr.length - 1; i < arr.length; i += 2) {
            ans[i] = arr[down--];
        }
        for (int i = 1, up = 0; i < arr.length; i += 2) {
            ans[i] = arr[up++];
        }
        for (int ele : ans) {
            System.out.print(ele + " ");
        }
    }
}
