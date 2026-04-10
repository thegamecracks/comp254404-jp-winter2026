package xyz.thegamecracks.comp254.lab6;

import java.util.Random;

import xyz.thegamecracks.comp254.lab6.maps.AbstractHashMap;
import xyz.thegamecracks.comp254.lab6.maps.ChainHashMap;

public class Exercise1 {
    private static final Random RAND = new Random();
    private static final int CAPACITY = 10;
    private static final int PRIME = 109345121;
    private static final int N_ENTRIES = 500_000;
    private static final int N_REPEAT = 10;

    public static void main(String[] args) {
        for (double i = 1; i < 10; i += 1) {
            benchmarkMap(i * 0.1);
        }
    }

    public static void benchmarkMap(double loadFactor) {
        long fastest = Long.MAX_VALUE;
        long totalStart = System.currentTimeMillis();

        for (int iteration = 0; iteration < N_REPEAT; iteration++) {
            System.out.printf("Benchmarking ChainHashMap with load factor %.1f... (%2d/%2d)\r", loadFactor, iteration + 1, N_REPEAT);
            AbstractHashMap<Integer, Integer> map = new ChainHashMap<>(CAPACITY, PRIME, loadFactor);

            long start = System.currentTimeMillis();
            for (int value = 0; value < N_ENTRIES; value++) {
                map.put(RAND.nextInt(), value);
            }

            long elapsed = System.currentTimeMillis() - start;
            fastest = Math.min(fastest, elapsed);
            // System.out.printf("    %d. %dms\n", iteration + 1, elapsed);
        }
        System.out.println();

        long totalElapsed = System.currentTimeMillis() - totalStart;
        System.out.printf("  Completed %d runs in %,dms\n", N_REPEAT, totalElapsed);
        System.out.printf("  Fastest run: %,dms\n", fastest);
    }
}
