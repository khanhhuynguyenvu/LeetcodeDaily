package com.company;

import java.util.*;

public class Solution {
    public static String minWindow(String s, String t) {
        Map<Character, Integer> cnt_t = new HashMap<>();
        Map<Character, Integer> cnt_curr = new HashMap<>();
        for (char c : t.toCharArray()) {
            cnt_t.merge(c, 1, Integer::sum);
        }
        Deque<Integer> q = new ArrayDeque<>();
        int l = 0, r = s.length();
        s += ".";
        boolean isValid = false;
        int key = 0;
        Set<Character> keySet = new HashSet<>();
        for (int i = 0; i < s.length(); i++) {
            while (!q.isEmpty()
                    && (!cnt_t.containsKey(s.charAt(q.peek()))
                    || cnt_curr.get(s.charAt(q.peek())) > cnt_t.get(s.charAt(q.peek())))) {
                if (cnt_curr.containsKey(s.charAt(q.peek()))) {
                    cnt_curr.merge(s.charAt(q.peek()), -1, Integer::sum);
                    if (cnt_curr.get(s.charAt(q.peek())) == 0) {
                        cnt_curr.remove(s.charAt(q.peek()));
                    }
                }
                if (cnt_t.containsKey(s.charAt(q.peek()))
                        && cnt_curr.getOrDefault(s.charAt(q.peek()), 0) < cnt_t.get(s.charAt(q.peek()))) {
                    key--;
                    if (cnt_t.getOrDefault(s.charAt(q.peek()), 0) == 0) keySet.remove(s.charAt(q.peek()));
                }
                q.pop();
            }
            if (!q.isEmpty()
                    && key >= cnt_t.keySet().size()
                    && r - l + 1 > q.size()) {
                l = q.peek();
                r = i;
                isValid = true;
            }
            q.add(i);
            cnt_curr.merge(s.charAt(i), 1, Integer::sum);
            if (cnt_t.containsKey(s.charAt(i))
                    && cnt_curr.get(s.charAt(i)) >= cnt_t.get(s.charAt(i))
                    && !keySet.contains(s.charAt(i))) {
                key++;
                keySet.add(s.charAt(i));
            }
        }
        return isValid ? s.substring(l, r) : "";
    }

    public static void main(String[] args) {
        System.out.println(minWindow("bba", "ab"));
    }
}
