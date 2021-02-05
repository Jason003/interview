'''
class RangeModule {
    TreeMap<Integer, Integer> map = new TreeMap<>();
    public RangeModule() {

    }

    public void addRange(int left, int right) {
        if(left >= right) return;
        Integer lo = map.floorKey(left);
        Integer hi = map.floorKey(right);
        if(lo == null && hi == null) map.put(left, right);
        else if(lo != null && map.get(lo) >= left)
            map.put(lo, Math.max(right, Math.max(map.get(lo), map.get(hi))));
        else map.put(left, Math.max(right, map.get(hi)));

        Map<Integer, Integer> subMap = map.subMap(left, false, right, true);
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
        if(hi != null && map.get(hi) > right)
            map.put(right, map.get(hi));
        if(lo != null && map.get(lo) > left)
            map.put(lo, left);

        Map<Integer, Integer> subMap = map.subMap(left, true, right, false);
        map.keySet().removeAll(new HashSet<>(subMap.keySet()));
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