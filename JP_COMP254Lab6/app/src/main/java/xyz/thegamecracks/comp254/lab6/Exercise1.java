package xyz.thegamecracks.comp254.lab6;

import java.util.Random;

import xyz.thegamecracks.comp254.lab6.maps.AbstractHashMap;
import xyz.thegamecracks.comp254.lab6.maps.ChainHashMap;

public class Exercise1 {
    private static final Random RAND = new Random();
    private static final int CAPACITY = 10;
    private static final int PRIME = 109345121;
    private static final int N_ENTRIES = 1_000_000;

    public static void main(String[] args) {
        for (double i = 1; i < 10; i += 1) {
            benchmarkMap(i * 0.1);
        }
    }

    public static void benchmarkMap(double loadFactor) {
        System.out.printf("Benchmarking ChainHashMap with load factor %.1f...\n", loadFactor);
        AbstractHashMap<Integer, Integer> map = new ChainHashMap<>(CAPACITY, PRIME, loadFactor);

        long start = System.currentTimeMillis();
        for (int value = 0; value < N_ENTRIES; value++) {
            map.put(RAND.nextInt(), value);
        }

        long elapsed = System.currentTimeMillis() - start;
        System.out.printf("  Completed in %dms\n", elapsed);
    }
}
