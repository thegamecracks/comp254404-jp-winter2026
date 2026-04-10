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

    public record BenchmarkResults(double loadFactor, long elapsed, long totalElapsed) {
        public BenchmarkResults() {
            this(0.0, Long.MAX_VALUE, 0L);
        }
    }

    public static void main(String[] args) {
        BenchmarkResults fastestResults = new BenchmarkResults();

        for (double i = 1; i < 10; i += 1) {
            double loadFactor = i * 0.1;
            BenchmarkResults results = benchmarkMap(loadFactor);

            if (results.elapsed() < fastestResults.elapsed())
                fastestResults = results;
        }

        System.out.printf(
                "Fastest load factor: %.1f (%,dms)\n",
                fastestResults.loadFactor(),
                fastestResults.elapsed());
    }

    public static BenchmarkResults benchmarkMap(double loadFactor) {
        long fastest = Long.MAX_VALUE;
        long totalStart = System.currentTimeMillis();

        for (int iteration = 0; iteration < N_REPEAT; iteration++) {
            System.out.printf(
                    "Benchmarking ChainHashMap with load factor %.1f... (%2d/%2d)\r",
                    loadFactor, iteration + 1, N_REPEAT);

            long start = System.currentTimeMillis();
            AbstractHashMap<Integer, Integer> map = new ChainHashMap<>(CAPACITY, PRIME, loadFactor);
            for (int value = 0; value < N_ENTRIES; value++) {
                map.put(RAND.nextInt(), value);
            }
            long elapsed = System.currentTimeMillis() - start;

            fastest = Math.min(fastest, elapsed);
            /* System.out.printf("    %d. %dms\n", iteration + 1, elapsed); */
        }
        System.out.println();

        long totalElapsed = System.currentTimeMillis() - totalStart;
        System.out.printf("  Completed %d runs in %,dms\n", N_REPEAT, totalElapsed);
        System.out.printf("  Fastest run: %,dms\n", fastest);
        return new BenchmarkResults(loadFactor, fastest, totalElapsed);
    }
}
