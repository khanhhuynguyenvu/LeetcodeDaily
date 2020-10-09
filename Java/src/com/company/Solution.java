package com.company;

public class Solution {
    public static double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int n1 = nums1.length;
        int n2 = nums2.length;
        int n = n1 + n2;
        int[] nums = new int[n];
        int l = 0, r = 0, inc = 0;
        while (l < n1 && r < n2) {
            if (nums1[l] < nums2[r]) {
                nums[inc] = nums1[l];
                l++;
            } else {
                nums[inc] = nums2[r];
                r++;
            }
            inc++;
        }
        while (l < n1) {
            nums[inc++] = nums1[l++];
        }
        while (r < n2) {
            nums[inc++] = nums2[r++];
        }
        if (n % 2 != 0) return nums[n / 2];
        else return (nums[n / 2] * 1.0 + nums[n / 2 - 1] * 1.0) / 2;
    }

    public static void main(String[] args) {
        int[] nums = new int[]{1, 3};
        int[] nums2 = new int[]{2};
        System.out.println(findMedianSortedArrays(nums, nums2));
    }
}
