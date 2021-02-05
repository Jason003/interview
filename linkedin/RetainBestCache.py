# -*- coding: utf-8 -*-
# @Time : 2020/12/10 21:42
# @Author : Jiefan

'''
package linkedin;
/*
 * For reference, here are the Rankable and DataSource interfaces.
 * You do not need to implement them, and should not make assumptions
 * about their implementations.
 */

import java.util.*;

/*
 * For reference, here are the Rankable and DataSource interfaces.
 * You do not need to implement them, and should not make assumptions
 * about their implementations.
 */

interface Rankable {
    /**
     * Returns the Rank of this object, using some algorithm and potentially
     * the internal state of the Rankable.
     */
    long getRank();
}

interface DataSource<K, T extends Rankable> {
    T get (K key);
}

public class RetainBestCache<K, T extends Rankable> {

    private TreeMap<T, Set<K>> rank2keys;
    private HashMap<K, T> key2val;
    private DataSource dataSource;
    private int capacity;

    /* Constructor with a data source (assumed to be slow) and a cache size */
    public RetainBestCache(DataSource<K, T> ds, int entriesToRetain) throws Exception {
        // Implementation here
        if (entriesToRetain < 1) {
            throw new RuntimeException("Invalid value!");
        }
        dataSource = ds;
        rank2keys = new TreeMap<>();
        key2val = new HashMap<>();
        capacity = entriesToRetain;
    }

    /*If the key to rank mapping can be many to 1, and keys are meant to be sufficiently randomly distributed,
    can it be assumed that key can be properly hashed to get a rank*/

    //  {1-> "abc", 4-> "abd" , 10-> "pqr"}, size =3, key="xyz->100"
    //{"abc"->1, "abd" -> 4, "pqr" ->10}

    /* Gets some data. If possible, retrieves it from cache to be fast. If the data is not cached,
     * retrieves it from the data source. If the cache is full, attempt to cache the returned data,
     * evicting the T with lowest rank among the ones that it has available
     * If there is a tie, the cache may choose any T with lowest rank to evict.
     */
    public T get(K key) {
        if (!key2val.containsKey(key)) {
            T res = (T) dataSource.get(key);
            key2val.put(key, res);
            if (key2val.size() > capacity) {
                T lowestRank = rank2keys.lastKey();
                K toRemove = rank2keys.get(lowestRank).iterator().next();
                rank2keys.get(lowestRank).remove(toRemove);
                if (rank2keys.get(lowestRank).size() == 0) {
                    rank2keys.remove(lowestRank);
                }
                key2val.remove(toRemove);
            }
            rank2keys.putIfAbsent(res, new HashSet<>());
            rank2keys.get(res).add(key);
            return res;
        }
        return key2val.get(key);
    }
}
'''