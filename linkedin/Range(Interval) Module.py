'''
package linkedin;

import java.util.HashSet;
import java.util.Map;
import java.util.TreeMap;

class RangeModule {
    private TreeMap<Integer, Integer> map = new TreeMap<>();
    private int covered = 0;
    public RangeModule() {

    }

    public void addRange(int left, int right) { // O(logn + k)
        if(left >= right) return;
        Integer lo = map.floorKey(left);
        Integer hi = map.floorKey(right);
        if(lo == null && hi == null) {
            map.put(left, right);
            covered += right - left;
        }
        else if(lo != null && map.get(lo) >= left) {
            int before = map.get(lo);
            map.put(lo, Math.max(right, Math.max(map.get(lo), map.get(hi))));
            covered += map.get(lo) - before;
        }
        else {
            map.put(left, Math.max(right, map.get(hi)));
            covered += map.get(left) - left;
        }

        Map<Integer, Integer> subMap = map.subMap(left, false, right, true);
        for (int key : subMap.keySet()) {
            covered -= subMap.get(key) - key;
        }
        map.keySet().removeAll(new HashSet<>(subMap.keySet()));
    }

    public boolean queryRange(int left, int right) {
        Integer lo = map.floorKey(left);
        if(lo == null) return false;
        return map.get(lo) >= right;
    }

    public void removeRange(int left, int right) {
        if(left >= right) return;
        Integer lo = map.floorKey(left);
        Integer hi = map.floorKey(right);
        if(hi != null && map.get(hi) > right) {
            map.put(right, map.get(hi));
            covered += map.get(right) - right;
        }

        if(lo != null && map.get(lo) > left) {
            int before = map.get(lo);
            map.put(lo, left);
            covered -= before - left;
        }

        Map<Integer, Integer> subMap = map.subMap(left, true, right, false);
        for (int key : subMap.keySet()) {
            covered -= subMap.get(key) - key;
        }
        map.keySet().removeAll(new HashSet<>(subMap.keySet()));
    }

    public int getCoveredSize() {
        return covered;
    }

    public static void main(String[] args) {
        RangeModule rangeModule = new RangeModule();
        rangeModule.addRange(0, 3);
        rangeModule.addRange(0, 1);
        rangeModule.addRange(2, 4);
        rangeModule.addRange(-1, 10);
        rangeModule.addRange(-1, 10);
        rangeModule.removeRange(0, 2);
        rangeModule.addRange(0, 1);
        System.out.println(rangeModule.getCoveredSize());
    }
}

/**
 * Your RangeModule object will be instantiated and called as such:
 * RangeModule obj = new RangeModule();
 * obj.addRange(left,right);
 * boolean param_2 = obj.queryRange(left,right);
 * obj.removeRange(left,right);
 */
'''