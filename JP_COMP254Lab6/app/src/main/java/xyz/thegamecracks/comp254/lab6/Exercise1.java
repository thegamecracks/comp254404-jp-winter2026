package xyz.thegamecracks.comp254.lab6;

import xyz.thegamecracks.comp254.lab6.maps.AbstractHashMap;
import xyz.thegamecracks.comp254.lab6.maps.ChainHashMap;

public class Exercise1 {
    public static void main(String[] args) {
        int capacity = 10;
        int prime = 109345121;
        for (double loadFactor = 0.1; loadFactor < 1.0; loadFactor += 0.1) {
            AbstractHashMap<Integer, String> map = new ChainHashMap<>(capacity, prime, loadFactor);
            benchmarkMap(map);
        }
    }

    public static void benchmarkMap(AbstractHashMap<Integer, String> map) {
        // TODO: use random values and measure performance
        for (int key = 0; key < 100; key++) {
            map.put(key, String.format("Hello world #%d!", key));
        }
    }
}
